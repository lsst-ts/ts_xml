#!/usr/bin/env python

import os
import re
import sys

import graphviz
import yaml

# --------------------------------------------


def isMT(name):
    """Does this CSC or SAL component belong to the 8.4m telescope?

    Parameters
    ----------
    name : `str`
        The name of the CSC or SAL component

    Returns
    -------
    boolean : `bool`
        True iff name belongs to the 8.4m
    """

    if (
            re.search(r"^(ts_)?(CC|M1M3|MT)", name, re.IGNORECASE) or
            name == "NewMTMount" or
            name == "ts_hexrotcomm" or
            name == "dome_eie" or
            name == "ts_m1m3supporteui" or
            name == "dm_ccarchiver" or
            name == "ts_CBP" or
            name == "ts_Dome" or
            name == "ts_dsm" or
            name == "ts_eas" or
            name == "ts_hexapod" or
            name == "ts_m2" or
            name == "ts_TunableLaser" or
            False
    ):
        return True

    return False


def nodeOpts(csc):
    """Return node options for graphviz

    Parameters
    ----------
    csc : `str`
        The name of a CSC

    Returns
    -------
    options : `dict`
        Options to be passed to `dot.node`
    """

    fillcolors = dict(
    )
    styles = dict(
        ts_externalscripts="dashed",
        ts_notebooks="dashed",
    )

    if "LOVE" in csc:
        styles[csc] = "filled"
        fillcolors[csc] = "pink"

    if "Simulator" in csc:
        styles[csc] = "filled"

    return dict(
        fillcolor=fillcolors.get(csc),
        style=styles.get(csc),
    )


def edgeOpts(cpt):
    """Return edge options for graphviz

    Parameters
    ----------
    cpt : `str`
        The name of a SAL component

    Returns
    -------
    options : `dict`
        Options to be passed to `dot.edge`
    """
    colors = dict(
        ATAOS='violet',
        ATCamera='red',
        ATDome='blue',
        ATMCS='chartreuse2',
        ATHexapod='brown',
        ATSpectrograph='orange',
        Environment='cyan',
    )
    styles = dict(
        Dome='dashed',
        EFD='dashed',
        Hexapod='dashed',
    )

    return dict(
        color=colors.get(cpt),
        style=styles.get(cpt),
    )


def ignoreCsc(name):
    """Return True if we should ignore a package

    You can add to this list from the command line with --ignore

    Parameters
    ----------
    package : `str`
        The name of package (e.g. "ts_watcher")

    Returns
    -------
    boolean : `bool`
        True iff we should ignore the package
    """
    if (
            re.search(r"^LOVE-(commander|producer|simulator|integration-tools)$", name) or
            name == "dm_csc_base" or
            name == "ts_labview_salApi" or
            name == "m2.py" or
            False
    ):
        return True
    else:
        return False


def ignoreSalCpt(name):
    """Return True for SAL components that we should ignore

    Parameters
    ----------
    name : `str`
        The name of sal component (e.g. "ATCamera")

    Returns
    -------
    boolean : `bool`
        True iff we should ignore the component
    """
    if name in ["name", "Test"]:
        return True
    else:
        return False


def requiredCsc(name):
    """Only draw nodes connected to nodes for which we return True

    Return None or "" to draw all otherwise-selected nodes

    N.b. list may be set from the command line using --required

    Parameters
    ----------
    name : `str`
        The name of CSC component (e.g. "HeaderService")

    Returns
    -------
    boolean : `bool`
        True iff we require name
    """

    return None


def makeGraph(yamlData, show_MT=False, show_orphans=True, verbose=0):
    """Make a graphviz file from the yaml produced by find_csc_dependencies

    Parameters
    ----------
    yamlData : `dict` of `dict`
        top level keys are "controllers" and "remotes"
    show_MT : `bool`
        Should I show main telescope components in addition to auxTel?
    show_orphans : `bool`
        Should I CSCs that have no remotes?
    verbose : `bool`
        Should I be chatty?

    Returns
    -------
    boolean : `graphviz.Graph`
        The desired graph
    """
    #
    # Start by finding all the SAL components provided by the controllers
    #
    # "packages" are the git or other containers of source code that implement
    # controllers; e.g.
    #     packages['ATMonochromator'] == ['ts_atmonochromator']
    #
    # Ideally the list would have only one element, but when there are both
    # old and new versions of CSCs being analysed (which shouldn't happen), or
    # the analysis code is confused (e.g. ts_mtm2) you can get things like
    #     packages['MTM2'] == ['ts_m2', 'ts_mtm2']
    # It is not this package's job to fix these inconsistencies, but we do
    # complain
    #
    packages = {}
    for package in yamlData["controllers"]:
        if ignoreCsc(package):
            continue

        for salCpt in yamlData["controllers"][package]:
            if ignoreSalCpt(salCpt):
                continue

            if salCpt not in packages:
                packages[salCpt] = []
            packages[salCpt].append(package)
    #
    # Prepare to make our dependency graph
    #
    dot = graphviz.Graph(comment='CSC Dependencies')

    nodes = {}                          # graphviz nodes that we've created
    for salCpt in sorted(packages):
        sources = packages[salCpt]
        if len(sources) != 1:
            print(f"Warning: {salCpt:20} is generated by {sources}", file=sys.stderr)

        cscLabel = sources[0]

        if (not show_MT and isMT(cscLabel)) or ignoreCsc(cscLabel):
            continue
        #
        # go through all the "packages" (e.g. ts_ATDomeTrajectory)
        # looking for their remotes
        #
        for package in yamlData["remotes"]:
            if package == cscLabel:     # some CSC packages talk to themselves (e.g. GUIs)
                continue

            if (not show_MT and isMT(package)) or ignoreCsc(package):
                continue

            for message in yamlData["remotes"][package]:
                if ignoreSalCpt(message):
                    continue

                if message == salCpt:
                    if ignoreCsc(cscLabel) or ignoreCsc(package):
                        continue

                    # If requiredCsc() is configured only show nodes connected
                    # to the required ones
                    if requiredCsc(cscLabel) is not None or requiredCsc(package) is not None:
                        if not (requiredCsc(cscLabel) or requiredCsc(package)):
                            continue

                    if cscLabel not in nodes:
                        nodes[cscLabel] = True
                        dot.node(cscLabel, shape='box', **nodeOpts(cscLabel))

                    if package not in nodes:
                        nodes[package] = True
                        dot.node(package, shape='box', **nodeOpts(package))

                    dot.edge(cscLabel, package, message, dir='forward', **edgeOpts(message))

    #
    # Show disconnected SAL components
    #
    if show_orphans:
        for salCpt in packages:
            cscLabel = packages[salCpt][0]

            if (not show_MT and isMT(cscLabel)) or ignoreCsc(cscLabel):
                continue

            if cscLabel not in nodes:
                nodes[cscLabel] = True
                dot.node(cscLabel, shape='box', **nodeOpts(cscLabel))

    return dot

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


if __name__ == "__main__":

    import argparse
    parser = argparse.ArgumentParser(description="""\
    Process the yaml file produced by find_csc_dependencies to generate a graphviz file

    This may be converted to e.g. pdf with e.g.

        dot -Tpdf foo.gv > foo.pdf
    """,
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('yamlFile', help="File generated by find_csc_dependencies")
    parser.add_argument('--format', help="Format for rendered graph", default="pdf")
    parser.add_argument('--ignore', dest="ignore_packages", metavar="package", nargs="*",
                        help="Ignore these packages", default=["LOVE-frontend"])
    parser.add_argument('--list_components', action="store_true",
                        help="List mapping of CSCs to SAL components", default=False)
    parser.add_argument('--orphans', dest="show_orphans", action="store_true",
                        help="Show CSCs without remotes", default=False)
    parser.add_argument('--output', '-o', metavar="dotFile", help="Generated file for graphviz",
                        default="CSCs.gv")
    parser.add_argument('--show-MT', action="store_true", help="Show MT components?", default=False)
    parser.add_argument('--required', metavar="CSC", nargs="*",
                        help="Only show CSCs connected to ones on this list", default=[])
    parser.add_argument('--verbose', '-v', action="store_true", help="How chatty should I be?", default=False)

    args = parser.parse_args()

    with open(args.yamlFile) as fd:
        yamlData = yaml.load(fd, yaml.CLoader)
    #
    # Only show CSCs with one degree of separation from args.required;
    # e.g. HeaderService
    #
    if args.required:
        def requiredCsc(name):          # noqa: F811
            return name in args.required
    #
    # Ignore certain packages; e.g. ts_notebooks
    #
    if args.ignore_packages:
        _ignoreCsc = ignoreCsc

        def ignoreCsc(name):
            return name in args.ignore_packages or _ignoreCsc(name)

    if args.list_components:
        for csc in sorted(yamlData["controllers"]):
            if not ignoreCsc(csc):
                salCpts = [c for c in yamlData['controllers'][csc] if not ignoreSalCpt(c)]
                if salCpts:
                    print(f"{csc:40} {salCpts}")
    #
    # Do the work
    #
    dot = makeGraph(yamlData, show_MT=args.show_MT, show_orphans=args.show_orphans, verbose=args.verbose)
    #
    # Write to disk, and render to e.g. pdf
    #
    format = "pdf"
    renderedFile = dot.render(args.output, view=False, format=args.format)

    fixedRenderedFile = f"{os.path.splitext(args.output)[0]}.{args.format}"
    os.rename(renderedFile, fixedRenderedFile)  # otherwise it's e.g. foo.gv.pdf

    if args.verbose:
        print(f"Wrote {fixedRenderedFile}")
