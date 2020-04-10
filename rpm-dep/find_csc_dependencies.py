#!/usr/bin/env python

"""
Analyse the dependencies between a set of codes communicating using SAL

The "set of codes" will usually be CSCs
"""
import glob
import os
import re
import sys

class Component:
    def __init__(self, name, path, lineNo, line=None):
        self.name = name
        self.path = path
        self.lineNo = lineNo
        self.line = line

class Controller(Component):
    pass

class Remote(Component):
    pass

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#
# N.b. we use functions such as `isPython` in case we ever want to be cleverer
# than just the extension
#
def hasExtension(path, extensions):
    """Does a file have one of the specified extensions?

    Parameters
    ----------
    path : `str`
        The name of the file
    extensions : `str`
        List of desired extension (n.b. no "."; e.g. "py")

    Returns
    -------
    config_dir : `bool`
        True iff path has the extension
    """
    ext = os.path.splitext(path)[1]

    for e in extensions:
        if ('.' + e) == ext:
            return True

    return False

def isJava(path):
    """Does a file contain java

    Parameters
    ----------
    path : `str`
        The name of the file

    Returns
    -------
    config_dir : `bool`
        True iff path is java
    """
    return hasExtension(path, ["java"])


def isJavaScript(path):
    """Does a file contain javascript?

    Parameters
    ----------
    path : `str`
        The name of the file

    Returns
    -------
    config_dir : `bool`
        True iff path is yaml
    """
    return hasExtension(path, ["js"])


def isJSX(path):
    """Does a file contain jsx??

    Parameters
    ----------
    path : `str`
        The name of the file

    Returns
    -------
    config_dir : `bool`
        True iff path is jsx
    """
    return hasExtension(path, ["jsx"])


def isPython(path, include_notebooks=False):
    """Does a file contain python source?

    Parameters
    ----------
    path : `str`
        The name of the file
    include_notebooks : `bool`
        Should I include [python] jupyter notebooks?

    Returns
    -------
    config_dir : `bool`
        True iff path is python source
    """
    extensions = ["py"]
    if include_notebooks:
        extensions.append("ipynb")

    return hasExtension(path, extensions)

def isYaml(path):
    """Does a file contain yaml?

    Parameters
    ----------
    path : `str`
        The name of the file

    Returns
    -------
    config_dir : `bool`
        True iff path is yaml
    """
    return hasExtension(path, ["yaml"])


#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def doJava(path, verbose=True):
    """Process a java file, looking for Controllers and Remotes

    Parameters
    ----------
    path : `str`
        The name of the file

    Returns
    -------
    controllers : `list` of `Controller`
        List of names of all controllers provided by this file
    remotes : `list` of `Remote`
        List of names of all remotes used by this file

    """
    if verbose:
        print(f"   Processing {path}")

    controllers = []
    remotes = []

    with open(path) as fd:
        lineNo = 0
        while True:
            break

            line = fd.readline()
            if line == "":
                break
            lineNo += 1

            line = re.sub(r"(^|[^\\])#.*", "", line[:-1])   # remove comments (and newline)
            if line == "":
                continue
            #
            # Look for Remotes
            #
            for cptName in re.findall(r"\s*name\s*:\s*['\"](\S+)['\"]\s*,\s*salindex\s*:\s*\d+\s*},?\s*",
                                      line):
                remotes.append(Remote(cptName, path, lineNo, line))

    return controllers, remotes


def doJavaScript(path, verbose=True):
    """Process a JS file, looking for Controllers and Remotes

    Parameters
    ----------
    path : `str`
        The name of the file

    Returns
    -------
    controllers : `list` of `Controller`
        List of names of all controllers provided by this file
    remotes : `list` of `Remote`
        List of names of all remotes used by this file

    """
    if verbose:
        print(f"   Processing {path}")

    controllers = []
    remotes = []

    with open(path) as fd:
        lineNo = 0
        while True:
            line = fd.readline()
            if line == "":
                break
            lineNo += 1

            line = re.sub(r"(^|[^\\])#.*", "", line[:-1])   # remove comments (and newline)
            if line == "":
                continue
            #
            # Look for Remotes
            #
            for cptName in re.findall(r"\s*name\s*:\s*['\"](\S+)['\"]\s*,\s*salindex\s*:\s*\d+\s*},?\s*",
                                      line):
                remotes.append(Remote(cptName, path, lineNo, line))

    return controllers, remotes


def doJsx(path, verbose=True):
    """Process a JSX file, looking for Controllers and Remotes

    Parameters
    ----------
    path : `str`
        The name of the file

    Returns
    -------
    controllers : `list` of `Controller`
        List of names of all controllers provided by this file
    remotes : `list` of `Remote`
        List of names of all remotes used by this file

    """
    if verbose:
        print(f"   Processing {path}")

    controllers = []
    remotes = []

    with open(path) as fd:
        lineNo = 0
        while True:
            line = fd.readline()
            if line == "":
                break
            lineNo += 1

            line = re.sub(r"(^|[^\\])#.*", "", line[:-1])   # remove comments (and newline)
            if line == "":
                continue
            #
            # Look for Remotes
            #
            for prefix, cptName,in re.findall(r"['\"]([^-'\"]+)-([a-zA-Z0-9]+)-[^-'\"]+-[^-'\"]+['\"]", line):
                if prefix  in ["heartbeat", "time"] or \
                   cptName in ["Heartbeat", "'Test'"]:
                    continue

                if prefix not in ["event", "telemetry"]:
                    print(f"Unexpected prefix '{prefix}' at {path}:{lineNo}", file=sys.stderr)
                    print(f"      {line}", file=sys.stderr)

                remotes.append(Remote(cptName, path, lineNo, line))

    return controllers, remotes


def doPython(path, verbose=True):
    """Process a python file, looking for Controllers and Remotes

    Parameters
    ----------
    path : `str`
        The name of the file

    Returns
    -------
    controllers : `list` of `Controller`
        List of names of all controllers provided by this file
    remotes : `list` of `Remote`
        List of names of all remotes used by this file

    """
    if verbose:
        print(f"   Processing {path}")

    controllers = []
    remotes = []

    with open(path) as fd:
        lineNo = 0
        while True:
            line = fd.readline()
            if line == "":
                break
            lineNo += 1

            line = re.sub(r"(^|[^\\])#.*", "", line[:-1])   # remove comments (and newline)
            if line == "":
                continue
            #
            # Look for controllers
            #
            for regex in [r"super\(\)\.__init__\(\s*['\"]([^'\"]+)['\"]\s*,",
                          r"Controller\(\s*['\"]([^'\"]+)['\"]\s*\)",
                          r"^\s*class\s+([^(\s]+)\s*\((?:salobj.)?(BaseCsc|ConfigurableCsc)\s*\)\s*:\s*$",
            ]:
                match = re.search(regex, line)
                
                if match:
                    cptName = match.group(1)
                    controllers.append(Controller(cptName, path, lineNo, line))
            #
            # Look for Remotes
            #

            for regex in [r"Remote\([^,]+,\s*['\"]([^'\"]+)['\"]\s*\)",
                          r"^\s*class\s+([^(\s]+)\s*\((?:salobj.)?Remote\s*\)\s*:\s*$",
                              ]:
                match = re.search(regex, line)
            
                if match:
                    cptName = match.group(1)
                    remotes.append(Remote(cptName, path, lineNo, line))

    return controllers, remotes


def doYaml(path, verbose=True):
    """Process a yaml file, looking for Controllers and Remotes

    Parameters
    ----------
    path : `str`
        The name of the file

    Returns
    -------
    controllers : `list` of `Controller`
        List of names of all controllers provided by this file
    remotes : `list` of `Remote`
        List of names of all remotes used by this file

    """
    if verbose:
        print(f"   Processing {path}")

    controllers = []
    remotes = []

    with open(path) as fd:
        lineNo = 0
        while True:
            line = fd.readline()
            if line == "":
                break
            lineNo += 1

            line = re.sub(r"(^|[^\\])#.*", "", line[:-1])   # remove comments (and newline)
            if line == "":
                continue
            #
            # Look for controllers
            #
            for regex in []:
                match = re.search(regex, line)
                
                if match:
                    cptName = match.group(1)
                    controllers.append(Controller(cptName, path, lineNo, line))
            #
            # Look for Remotes
            #
            for regex in [r"^\s*device\s*:\s*(\S+)",
                              ]:
                match = re.search(regex, line)
            
                if match:
                    cptName = match.group(1)
                    remotes.append(Remote(cptName, path, lineNo, line))

    return controllers, remotes

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


def process_tree(root, controllers, remotes, ignoredDirs=[".git"],
                 extensions=None,
                 include_notebooks=False, verbose=False, name=None):
    """process all the files in a directory tree

    Parameters
    ----------
    root : `str`
        The name of the directory tree to process
    name : `str`
        The name of the CSC represented by root; defaults to `root` if `None`
    
    """
    if name is None:
        name = root

    if verbose:
        print(f"Processing {root}")

    controllers[name] = {}
    remotes[name] = {}

    if os.path.isfile(root):
        if extensions is None or hasExtension(root, extensions):
            processFile(root, controllers[name], remotes[name],
                        include_notebooks=include_notebooks, verbose=verbose)
    else:
        for dirpath, dirnames, filenames in os.walk(root, topdown=True):
            # don't recurse into e.g. .git
            for ignoreDir in ignoredDirs:
                try:
                    i = dirnames.index(ignoreDir)
                except ValueError:
                    pass
                else:
                    del dirnames[i]

            for filename in filenames:
                if extensions is None or hasExtension(filename, extensions):
                    processFile(os.path.join(dirpath, filename), controllers[name], remotes[name],
                                include_notebooks=include_notebooks, verbose=verbose)

def processFile(filename, controllers, remotes, include_notebooks=False, verbose=False):
    """Process a file, looking for signs of being a Controller or Remote

    """
    #
    # files to ignore.
    #
    badFiles = {
        "PySourceColor.py" : "'utf-8' codec can't decode byte 0xfc in position 6306",
    }

    if os.path.basename(filename) in badFiles:
        if verbose:
            print(f"Ignoring {filename} as it is on badFiles list", file=sys.stderr)
        return
    
    if isJava(filename):
        doFile = doJava
    if isJavaScript(filename):
        doFile = doJavaScript
    elif isJSX(filename):
        doFile = doJsx
    elif isPython(filename, include_notebooks):
        doFile = doPython
    elif isYaml(filename):
        doFile = doYaml
    else:
        return

    controllers[filename], remotes[filename] = doFile(filename, verbose=verbose)

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="")

    parser.add_argument('directories', type=str, nargs="*",
                        help="Directories to analyse")
    parser.add_argument('--examples',  action="store_true",
                        help="Include examples in analysis?", default=False)
    parser.add_argument('--extensions', type=str, nargs="+",
                        help="Only process these extensions")
    parser.add_argument('--mocks',  action="store_true",
                        help="Include mocks in analysis?", default=False)
    parser.add_argument('--notebooks',  action="store_true",
                        help="Include notebooks in analysis?", default=False)
    parser.add_argument('--show_filenames',  action="store_true",
                        help="Print filenames where components were found", default=False)
    parser.add_argument('--show_lines',  action="store_true",
                        help="Print lines where components were found", default=False)
    parser.add_argument('--tests',  action="store_true",
                        help="Include tests in analysis?", default=False)
    parser.add_argument('--verbose', '-v',  action="store_true",
                        help="How chatty should I be?", default=False)

    args = parser.parse_args()

    if args.show_lines and not args.show_filenames:
        if args.verbose:
            print("--show_lines requires --show_filenames; setting")
        args.show_filenames = True

    dirs = args.directories
    if len(dirs) == 1 and dirs[0] == ".":  # we want the directory names
        dirs = glob.glob("*")

    ignoredDirs = [".git"]
    if not args.examples:
        ignoredDirs.append("examples")
    if not args.mocks:
        ignoredDirs.append("mock")
    if not args.tests:
        ignoredDirs.append("tests")

    controllers = {}
    remotes = {}        
    for d in dirs:
        name = os.path.basename(d)

        process_tree(d, controllers, remotes, ignoredDirs, name=name, extensions=args.extensions,
                     include_notebooks=args.notebooks, verbose=args.verbose)

    for name in controllers:
        ctrls = sum(controllers[name].values(), [])
        rems =  sum(remotes[name].values(), [])

        if ctrls:
            print(f"{name:40s} Controllers: {', '.join(set([cpt.name for cpt in ctrls]))}")

            if args.show_filenames:
                for cpt in ctrls:
                    print(f"{'':53} {cpt.name:20} {cpt.path}:{cpt.lineNo}")
                    if args.show_lines:
                        print(f"{'':63} {cpt.line}")

        if rems:
            print(f"{name:40s} Remotes:     {', '.join(set([cpt.name for cpt in rems]))}")

            if args.show_filenames:
                for cpt in rems:
                    print(f"{'':53} {cpt.name:20} {cpt.path}:{cpt.lineNo}")
                    if args.show_lines:
                        print(f"{'':63} {cpt.line}")
