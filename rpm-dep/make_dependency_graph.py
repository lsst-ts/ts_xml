#!/usr/bin/env python

import glob
import os
import re
import graphviz
import yaml

# --------------------------------------------

def isMT(name):
    """Does this CSC or SAL component belong to the 8.4m telescope?"""
    if (#False and
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
        name == "ts_TunableLaser" or
        False
       ):
        return True
    
    return False

def nodeOpts(csc):
    fillcolors = dict(
    )
    styles = dict(
        Simulator = "filled",
        ts_externalscripts = "dashed",
        ts_notebooks = "dashed",
    )

    if "LOVE" in csc:
        styles[csc] = "filled"
        fillcolors[csc] = "pink"

    return dict(
        fillcolor=fillcolors.get(csc),
        style=styles.get(csc),
    )

def edgeOpts(message):
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
        color=colors.get(message),
        style=styles.get(message),
    )

def ignoreCsc(name):
    """Return True if we should ignore name"""
    if (re.search(r"^LOVE-(commander|producer|simulator|integration-tools)$", name) or
        name == "LOVE-frontend" or
        #name == "ts_notebooks" or            
        #name == "ts_scripts" or
        name == "dm_csc_base" or
        name == "ts_labview_salApi" or
        isMT(name) or
        False
        ):
        return True
    else:
        return False
    
def specialCsc(name):
    """Only draw nodes connected to special nodes for which we return True
    
    Return None or "" to draw all otherwise-selected nodes
    """

    return name in ["HeaderService"] if False else None


def makeGraph(yamlData, verbose=0):
    """Given a yaml file produced by find_csc_dependencies, make a graphviz .gv file

    """
    #
    # Start by finding all the SAL components provided by the controllers
    #
    salCpts = {}
    packages = {}
    for package in yamlData["controllers"]:
        for salCpt in yamlData["controllers"][package]:
            if salCpt in ["name"]:
                continue

            salCpts[salCpt] = salCpt

            if salCpt not in packages:
                packages[salCpt] = []
            packages[salCpt].append(package)

    if verbose > 0:
        for p, salCpts in packages.items():
            if len(salCpts) != 1:
                print(f"{p:40} {salCpts}")


    dot = graphviz.Graph(comment='VRO')

    cscNodes = {}
    edges = {}
    nodes = {}
    for salCpt in salCpts:
        cscLabel = packages[salCpt][0]

        if isMT(salCpt):
            continue
        #
        # go through all the "packages" (e.g. ts_ATDomeTrajectory) looking for their remotes
        #
        for package in yamlData["remotes"]:
            if package == cscLabel:     # some CSCs talk to themselves (e.g. GUIs)
                continue

            if ignoreCsc(package):
                continue

            for message in yamlData["remotes"][package]:
                if isMT(message) or message in ["name", "Test"]:
                    continue

                if message == salCpt:
                    if ignoreCsc(cscLabel) or ignoreCsc(package):
                        continue

                    # just show nodes connected to specialCsc if it's set
                    if specialCsc(cscLabel) is not None or specialCsc(package) is not None: 
                        if not (specialCsc(cscLabel) or specialCsc(package)):
                            continue

                    if isMT(package):
                        continue

                    if cscLabel not in nodes:
                        nodes[cscLabel] = True
                        dot.node(cscLabel, shape='box', **nodeOpts(cscLabel))

                    if package not in nodes:
                        nodes[package] = True
                        dot.node(package, shape='box', **nodeOpts(package))

                    dot.edge(cscLabel, package, message, dir='forward', **edgeOpts(message))

    #
    # Show disconnected SalCpts
    #
    for salCpt in salCpts:
        for package in yamlData["remotes"]:
            cscLabel = packages[salCpt][0]

            if isMT(cscLabel) or ignoreCsc(cscLabel):
                continue

            if cscLabel not in nodes:
                nodes[cscLabel] = True
                dot.node(cscLabel, shape='box', **nodeOpts(cscLabel))

    dot.render(f'CSCs.gv', view=False)

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


import argparse
parser = argparse.ArgumentParser(description="")

parser.add_argument('yamlFile', type=str, help="File generated by find_csc_dependencies")
parser.add_argument('--verbose', '-v', action="store_true", help="How chatty should I be?", default=False)

args = parser.parse_args()

with open(args.yamlFile) as fd:
    yamlData = yaml.load(fd, yaml.CLoader)

yamlData["controllers"]["ATCamera"] = ["ATCamera"]
yamlData["controllers"]["CCCamera"] = ["CCCamera"]
yamlData["controllers"]["MTCamera"] = ["MTCamera"]
yamlData["controllers"]["HeaderService"] = ["ATHeaderService"]  # was "name"
yamlData["controllers"]["ts_MTAOS"] = ["MTAOS"]                 # was "cscName"


makeGraph(yamlData, verbose=args.verbose)
