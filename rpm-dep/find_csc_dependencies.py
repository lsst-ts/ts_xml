#!/usr/bin/env python

"""
Analyse the dependencies between a set of codes communicating using SAL

The "set of codes" will usually be CSCs
"""
import ast
import glob
import os
import re
import sys
import xml.etree.ElementTree as ElementTree
import yaml


def patch_csc_name(name):
    """Patch a component name which we guessed originally

    Controlled by --patchCscNames

    Parameters
    ----------
    name : `str`
        The name of the CSC

    Returns
    -------
    patchedName : `str`
        The rewritten CSC name
    """

    return name


class Component:
    """A Controller or Remote"""
    def __init__(self, name, path="unknown", lineNo=-1, line=""):

        name = patch_csc_name(name)

        self.name = name
        self._name = name               # we may patch self.name later
        self.path = path
        self.lineNo = lineNo
        self.line = re.sub(r"\s*$", "", line)  # strip any newline


class Controller(Component):
    pass


class Remote(Component):
    pass


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def extractCscs(xmlfile):
    """Extract the list of CSCs from a file containing <SALSubsystems> entries

    Parameters
    ----------
    path : `str`
        The name of the file
    extensions : `str`
        List of desired extension (n.b. no "."; e.g. "py")

    Returns
    -------
    csc_list : `list` of `str`
        A list of all the <SALSubsystems> in the file
    """

    tree = ElementTree.parse(xmlfile)
    root = tree.getroot()

    cscs = []
    for ss in root.findall("SALSubsystem"):
        cscs.append(ss.find("Name").text)

    return cscs


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
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


def isCpp(path):
    """Does a file contain C++?

    Parameters
    ----------
    path : `str`
        The name of the file

    Returns
    -------
    config_dir : `bool`
        True iff path is java
    """
    return hasExtension(path, ["cpp", "h"])


def isJava(path):
    """Does a file contain java?

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
    """Does a file contain jsx?

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


def isLabView(path):
    """Does a file contain labview code?

    Parameters
    ----------
    path : `str`
        The name of the file

    Returns
    -------
    config_dir : `bool`
        True iff path is labview
    """
    return hasExtension(path, ["vi"])


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


def isSal(path):
    """Does a file contain sal definitions?

    Apparently only used by the CCS

    Parameters
    ----------
    path : `str`
        The name of the file

    Returns
    -------
    config_dir : `bool`
        True iff path is java
    """
    return hasExtension(path, ["sal"])


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


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def doCpp(path, verbose=0, **kwargs):
    """Process a C++ file, looking for Controllers and Remotes

    Parameters
    ----------
    path : `str`
        The name of the file
    verbose : `int`
        How verbose should I be?  The larger the chattier

    Returns
    -------
    controllers : `list` of `Controller`
        List of names of all controllers provided by this file
    remotes : `list` of `Remote`
        List of names of all remotes used by this file

    """
    if verbose > 2:
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

            line = re.sub(r"(^|[^\\])//.*", "", line[:-1])   # remove inline comments (and newline)
            if line == "":
                continue
            #
            # Look for Remotes
            #
            for cptName in re.findall(r"^\s*#\s*include\s+[\"<][^\">]*SAL_(\w+)(?:\.h)[\">]", line):
                if False and line.startswith(" * ") and cptName in ["camera"]:  # found in a comment
                    continue
                remotes.append(Remote(cptName, path, lineNo, line))

    return controllers, remotes


def doJava(path, verbose=0, **kwargs):
    """Process a java file, looking for Controllers and Remotes

    Parameters
    ----------
    path : `str`
        The name of the file
    verbose : `int`
        How verbose should I be?  The larger the chattier

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

            line = re.sub(r"(^|[^\\])//.*", "", line[:-1])   # remove inline comments (and newline)
            if line == "":
                continue
            #
            # Look for Remotes
            #
            for cptName in re.findall(r"org.lsst.sal.SAL_(\w+)", line):
                if line.startswith(" * ") and cptName in ["camera"]:  # found in a comment
                    continue
                remotes.append(Remote(cptName, path, lineNo, line))

    return controllers, remotes


def doJavaScript(path, verbose=0, **kwargs):
    """Process a JS file, looking for Controllers and Remotes

    Parameters
    ----------
    path : `str`
        The name of the file
    verbose : `int`
        How verbose should I be?  The larger the chattier

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

            line = re.sub(r"(^|[^\\])//.*", "", line[:-1])   # remove inline comments (and newline)
            if line == "":
                continue
            #
            # Look for Remotes
            #
            for cptName in re.findall(r"\s*name\s*:\s*['\"](\S+)['\"]\s*,\s*salindex\s*:\s*\d+\s*},?\s*",
                                      line):
                remotes.append(Remote(cptName, path, lineNo, line))

    return controllers, remotes


def doJsx(path, verbose=0, **kwargs):
    """Process a JSX file, looking for Controllers and Remotes

    Parameters
    ----------
    path : `str`
        The name of the file
    verbose : `int`
        How verbose should I be?  The larger the chattier

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

            line = re.sub(r"(^|[^\\])//.*", "", line[:-1])   # remove inline comments (and newline)
            if line == "":
                continue
            #
            # Look for Remotes
            #
            for prefix, cptName in re.findall(r"['\"]([^-'\"]+)-(\w+)-[^-'\"]+-[^-'\"]+['\"]", line):
                if prefix in ["heartbeat", "time"] or \
                   cptName in ["Heartbeat", "'Test'"]:
                    continue

                if prefix not in ["event", "telemetry"]:
                    if verbose:
                        print(f"Unexpected prefix '{prefix}' at {path}:{lineNo}", file=sys.stderr)
                        print(f"      {line}", file=sys.stderr)

                remotes.append(Remote(cptName, path, lineNo, line))

    return controllers, remotes


def doLabView(path, verbose=0, **kwargs):
    """Process a labView file, looking for Controllers and Remotes

    Parameters
    ----------
    path : `str`
        The name of the file
    verbose : `int`
        How verbose should I be?  The larger the chattier

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

    with open(path, "rb") as fd:
        lineNo = 0
        while True:
            line = fd.readline().decode(errors='ignore')

            if line == "":
                break
            lineNo += 1

            line = line[:-1]            # remove newline
            if line == "":
                continue
            #
            # Look for Controllers (assume that that's what labView does)
            #
            for cptName in re.findall(r"SALLV_(\w+)", line):
                if cptName in ["EXA", "EXA_Messaging"]:
                    continue
                controllers.append(Remote(cptName, path, lineNo, "(text omitted)"))

    return controllers, remotes


def doPythonRe(path, verbose=0, isNotebook=False, **kwargs):
    """Process a python file, looking for Controllers and Remotes

    Parameters
    ----------
    path : `str`
        The name of the file
    verbose : `int`
        How verbose should I be?  The larger the chattier

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

    def nextLine():
        r"""Return the nextlogical line, having handled \ continuations"""
        line = fd.readline()

        if isNotebook:
            mat = re.search(r'^\s*"(.*)",\s*$', line)
            if mat:
                line = mat.group(1)
                if line[-2:] == r"\n":
                    line = line[:-2]

        return line

    with open(path) as fd:
        lineNo = 0
        while True:
            line = nextLine()
            lineNo += 1

            if line == "":
                break

            if line[-1] == '\n':
                line = line[:-1]

            line = re.sub(r"(^|[^\\])#.*", "", line)   # remove inline comments
            #
            # Look for lines ending [(,] and append the next line.  Hack hack!
            #
            while re.search(r"[,\(]\s*$", line):
                line += nextLine()
                lineNo += 1

            if line == "":
                continue
            #
            # Look for controllers
            #
            for regex in [
                    r"super\(\)\.__init__\(\s*(?:name\s*=\s*)?['\"]([^'\"]+)['\"]\s*,",
                    r"Controller\(\s*['\"]([^'\"]+)['\"]\s*\)",
                    r"^\s*class\s+(\w+)\s*\((?:salobj\.)?(BaseCsc|ConfigurableCsc)\s*\)\s*:\s*$",
                    r"^\s*import\s+SALPY_(\w+)",
            ]:
                match = re.search(regex, line)

                if match:
                    cptName = match.group(1)

                    if isNotebook and "SALPY_" in regex:
                        if verbose:
                            print(f"Ignoring {cptName} based on SALPY_ match in a notebook")
                        continue

                    controllers.append(Controller(cptName, path, lineNo, line))
            #
            # Look for Remotes
            #
            for regex in [
                    r"Remote\([^,]+,\s*(?:name\s*=\s*)?['\"]([^'\"]+)['\"]",
                    r"Remote\(\s*SALPY_+(\w+)[\s)]",   # old-style salobj
                    r"^\s*class\s+([^(\s]+)\s*\((?:salobj.)?Remote\s*\)\s*:\s*$",
            ]:
                match = re.search(regex, line)

                if match:
                    cptName = match.group(1)
                    remotes.append(Remote(cptName, path, lineNo, line))

    return controllers, remotes


class AnalyseCsc(ast.NodeVisitor):
    """A class to be analyse a python Abstract Syntax Tree (AST)"""
    def __init__(self, path, sourceCode, verbose=0):
        self.path = path
        self.sourceCode = sourceCode
        self.verbose = verbose
        self.controllers = []
        self.remotes = []

    def getNodeArgs(self, n):
        """Return a node n's arguments"""
        args = []
        for arg in n.args:
            args.append(arg)

        for k in n.keywords:
            args.append(k.value)

        for i, arg in enumerate(args):
            arg0 = None
            while arg != arg0:
                arg0 = arg
                arg = (arg.attr        if isinstance(arg, ast.Attribute) else     # noqa: E272
                       arg.func        if isinstance(arg, ast.Call) else          # noqa: E272
                       "ast.JoinedStr" if isinstance(arg, ast.JoinedStr) else
                       "ast.List"      if isinstance(arg, ast.List) else          # noqa: E272
                       arg.id          if isinstance(arg, ast.Name) else          # noqa: E272
                       arg.value       if isinstance(arg, ast.NameConstant) else  # noqa: E272
                       arg.n           if isinstance(arg, ast.Num) else           # noqa: E272
                       arg.s           if isinstance(arg, ast.Str) else           # noqa: E272
                       arg)

            args[i] = arg

            if isinstance(arg, ast.AST):
                raise RuntimeError(f"Failed to convert {arg} to a value at {self.path}:{n.lineno}:\n"
                                   f"{self.sourceCode[n.lineno - 1]}")

        return args

    def visit_Call(self, n):
        func = n.func

        if isinstance(func, ast.Subscript):  # i.e. Remote_get[name]()
            func = func.value

        funcName = (func.id   if isinstance(func, ast.Name) else    # noqa: E272
                    func.func if isinstance(func, ast.Call) else
                    func.attr if isinstance(func, ast.Attribute) else
                    func)

        if funcName == "Remote":
            args = self.getNodeArgs(n)

            if len(args) < 2 or \
               args[0] and re.search(r"^SALPY_", args[0]):  # salpy
                self.generic_visit(n)
                return

            cptName = args[1]

            if self.verbose > 0:
                print(funcName, cptName)

            self.remotes.append(Remote(cptName, self.path, n.lineno, self.sourceCode[n.lineno - 1]))

        self.generic_visit(n)

    def visit_ClassDef(self, n):
        #
        # We only detect Controllers derived from these classes
        #
        cscBaseClasses = [
            "ArchiverCSC",
            "BaseCsc",
            "dm_csc",
            "dm_csc_base",
            "ConfigurableCsc",
            "Controller",
        ]

        superName = None
        for super in n.bases:
            superName = super.id if isinstance(super, ast.Name) else super.attr
            if superName in cscBaseClasses:
                break

        if self.verbose:
            print(n.name, superName)

        if superName not in cscBaseClasses:
            self.generic_visit(n)
            return

        for member in n.body:  # includes """descr. strings""" and such like too
            if not isinstance(member, ast.FunctionDef):
                continue

            if member.name != "__init__":
                continue

            for e in member.body:
                if isinstance(e, ast.Expr) and isinstance(e.value, ast.Call):  # might be a super() call
                    e = e.value   # unpack the RHS from the expr
                    func = e.func

                    value = (func.id if isinstance(func, ast.Name) else
                             func.value)
                    value = (value.attr if isinstance(value, ast.Attribute) else
                             value.func if isinstance(value, ast.Call) else
                             value)
                    funcName0 = (value.id   if isinstance(value, ast.Name) else  # noqa: E272
                                 value.attr if isinstance(value, ast.Attribute) else value)

                    funcName = func.id if isinstance(func, ast.Name) else func.attr

                    args = self.getNodeArgs(e)
                    cptName = args[0] if len(args) > 0 else None

                    if funcName0 == "super" and funcName == "__init__":
                        if cptName is not None:
                            self.controllers.append(Controller(cptName, self.path, e.lineno,
                                                               self.sourceCode[e.lineno - 1]))

        self.generic_visit(n)

    def visit_Import(self, n):
        for mod in n.names:
            modName = mod.name

            match = re.search(r"^SALPY_(\w+)", modName)
            if match:
                cptName = match.group(1)

                self.controllers.append(Controller(cptName, self.path, n.lineno,
                                                   self.sourceCode[n.lineno - 1]))

        self.generic_visit(n)


def doPythonAst(path, verbose=0, **kwargs):
    """Process a python file, looking for Controllers and Remotes

    This code uses ast to generate a syntax tree which it then analyses.
    If you're processing notebooks use doPythonRe instead; it's less robust

    Parameters
    ----------
    path : `str`
        The name of the file
    verbose : `int`
        How verbose should I be?  The larger the chattier

    Returns
    -------
    controllers : `list` of `Controller`
        List of names of all controllers provided by this file
    remotes : `list` of `Remote`
        List of names of all remotes used by this file

    """
    if verbose:
        print(f"   Processing {path}")

    with open(path) as fd:
        source = fd.readlines()

    try:
        tree = ast.parse("".join(source))
    except SyntaxError as e:
        print(f"Unable to parse {path}: {e}")
        return [], []

    analyseCsc = AnalyseCsc(path, source, verbose)
    analyseCsc.visit(tree)

    return analyseCsc.controllers, analyseCsc.remotes


def doSal(path, verbose=0, **kwargs):
    """Process a "sal" interface file, looking for Controllers and Remotes

    Parameters
    ----------
    path : `str`
        The name of the file
    verbose : `int`
        How verbose should I be?  The larger the chattier

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

            line = re.sub(r"(^|[^\\])//.*", "", line[:-1])   # remove inline comments (and newline)
            if line == "":
                continue
            #
            # Look for Remotes
            #
            for cptName in re.findall(r"org.lsst.sal.SAL_(\w+)", line):
                if line.startswith(" * ") and cptName in ["camera"]:  # found in a comment
                    continue
                remotes.append(Remote(cptName, path, lineNo, line))

    return controllers, remotes


def doYaml(path, verbose=0, **kwargs):
    """Process a yaml file, looking for Controllers and Remotes

    Parameters
    ----------
    path : `str`
        The name of the file
    verbose : `int`
        How verbose should I be?  The larger the chattier

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

            line = re.sub(r"(^|[^\\])#.*", "", line[:-1])   # remove inline comments (and newline)
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
            for regex in [
                    r"^\s*device\s*:\s*(\S+)",
            ]:
                match = re.search(regex, line)

                if match:
                    cptName = match.group(1)
                    remotes.append(Remote(cptName, path, lineNo, line))

    return controllers, remotes

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


def process_tree(root, controllers, remotes, ignoredDirs=[".git"],
                 extensions=None, include_notebooks=False, use_ast=True, verbose=0, name=None):
    """process all the files in a directory tree

    Parameters
    ----------
    root : `str`
        The name of the directory tree to process
    controllers : `list` of `Controller`s
        List of Controllers that we've found
    remotes : `list` of `Remote`s
        List of Remotes that we've found
    ignoredDirs : `list` of `str`
        List of directories to ignore (default: [".git"])
    extensions : `list` of `str`
        List of extensions to process (e.g. "py"); default None => all
    include_notebooks : `bool`
        Process jupyter notebooks?
    use_ast : `bool`
        Use ast package to process python (always correct except when
        debugging
    verbose : `int`
        How verbose should I be?  The larger the chattier
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
                        include_notebooks=include_notebooks, use_ast=use_ast, verbose=verbose)
    else:
        skipTests = True if ("test" in ignoredDirs) else False

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
                if skipTests and re.search(r"fake|test", filename):
                    continue

                if extensions is None or hasExtension(filename, extensions):
                    processFile(os.path.join(dirpath, filename), controllers[name], remotes[name],
                                include_notebooks=include_notebooks, use_ast=use_ast, verbose=verbose)


def processFile(filename, controllers, remotes, include_notebooks=False, use_ast=True, verbose=False):
    """Process a file, looking for signs of being a Controller or Remote

    Parameters
    ----------
    filename : `str`
        The name of the file to process
    controllers : `list` of `Controller`s
        List of Controllers that we've found
    remotes : `list` of `Remote`s
        List of Remotes that we've found
    include_notebooks : `bool`
        Process jupyter notebooks?
    use_ast : `bool`
        Use ast package to process python (always correct except when
        debugging
    verbose : `int`
        How verbose should I be?  The larger the chattier
    """
    #
    # files to ignore.
    #
    badFiles = {
        "DynamicLoadSample.cpp":    "'utf-8' codec can't decode byte 0x93 in position 306",   # noqa: E241
        "FirstSteps.cpp":           "'utf-8' codec can't decode byte 0x93 in position 306",   # noqa: E241
        "PySourceColor.py":         "'utf-8' codec can't decode byte 0xfc in position 6306",  # noqa: E241
        "sg_catalog_generator.cpp": "'utf-8' codec can't decode byte 0xb1 in position 4973",
        "StaticLoadSample_DataRecorder.cpp": "'utf-8' codec can't decode byte 0x93 in position 306",
        "Wavegenerator.cpp":        "'utf-8' codec can't decode byte 0x93 in position 306",   # noqa: E241
    }

    if os.path.basename(filename) in badFiles:
        if verbose:
            print(f"Ignoring {filename} as it is on badFiles list", file=sys.stderr)
        return

    kwargs = {}
    if isCpp(filename):
        doFile = doCpp
    elif isJava(filename):
        doFile = doJava
    elif isJavaScript(filename):
        doFile = doJavaScript
    elif isJSX(filename):
        doFile = doJsx
    elif isLabView(filename):
        doFile = doLabView
    elif isPython(filename):
        doFile = doPythonAst if use_ast else doPythonRe
    elif isPython(filename, include_notebooks):
        doFile = doPythonRe
        kwargs["isNotebook"] = True
    elif isYaml(filename):
        doFile = doYaml
    else:
        return

    ctrls, rems = doFile(filename, verbose=verbose, **kwargs)

    if ctrls:
        controllers[filename] = ctrls
    if rems:
        remotes[filename] = rems

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="""\
    Process source code analysing the SAL components which
    connect controllers (CSCs) and remotes.
    """)

    parser.add_argument('directories', type=str, nargs="*",
                        help="Directories to analyse")
    checkCscList_grp = parser.add_mutually_exclusive_group()
    checkCscList_grp.add_argument('--checkCscList', dest="checkCscList", action="store_true",
                                  help="Check the list of CSCs against the XML (default)", default=True)
    checkCscList_grp.add_argument('--no-checkCscList', dest="checkCscList", action="store_false",
                                  help="Don't check the list of CSCs against the XML")
    parser.add_argument('--examples', action="store_true",
                        help="Include examples in analysis?", default=False)
    parser.add_argument('--extensions', metavar="ext", nargs="+",
                        help="Only process these extensions")
    fixCscComponents_grp = parser.add_mutually_exclusive_group()
    fixCscComponents_grp.add_argument('--fixCscComponents', dest="fixCscComponents", action="store_true",
                                      help="Fix some missing/incorrect mappings of "
                                      "components to CSCs (default)", default=True)
    fixCscComponents_grp.add_argument('--no-fixCscComponents', dest="fixCscComponents", action="store_false",
                                      help="Don't fix some missing/incorrect mappings of components to CSCs")
    parser.add_argument('--list-cscs', action="store_true",
                        help="List the CSCs that checkCscList would use, and exit", default=False)
    parser.add_argument('--missing-cscs', action="store_true",
                        help="Show missing CSCs?", default=False)
    parser.add_argument('--mocks', action="store_true",
                        help="Include mocks in analysis?", default=False)
    parser.add_argument('--notebooks', action="store_true",
                        help="Include notebooks in analysis?", default=False)
    parser.add_argument('--output', '-o', metavar="file.yaml", help="Write output to this file")
    parser.add_argument('--patchCscNames', action="store_true",
                        help="Attempt to patch CSC names to match known list", default=False)
    parser.add_argument('--SALSubsystems', metavar="SALSubsystems.xml", help="XML file defining known CSCs",
                        default="ts_xml/sal_interfaces/SALSubsystems.xml")
    parser.add_argument('--show-filenames', action="store_true",
                        help="Print filenames where components were found", default=False)
    parser.add_argument('--show-lines', action="store_true",
                        help="Print lines where components were found", default=False)
    parser.add_argument('--tests', action="store_true",
                        help="Include tests (and fakes) in analysis?", default=False)
    parser.add_argument('--use-re', dest="use_ast", action="store_false",
                        help="Use regexps (not python AST) to analyse .py files? Debugging only",
                        default=True)
    parser.add_argument('--verbose', '-v', action="count", help="How chatty should I be?", default=0)

    args = parser.parse_args()

    if args.show_lines and not args.show_filenames:
        if args.verbose:
            print("--show_lines requires --show_filenames; setting")
        args.show_filenames = True

    dirs = args.directories
    if len(dirs) == 1 and dirs[0] == ".":  # we want the directory names
        dirs = sorted(glob.glob("*"))

    ignoredDirs = []
    ignoredDirs.append(".git")
    # templates
    ignoredDirs.append("{{cookiecutter.repo_name}}")
    ignoredDirs.append("EUI-Template")
    ignoredDirs.append("Controller-Template")

    if not args.examples:
        ignoredDirs.append("examples")
    if not args.mocks:
        ignoredDirs.append("mock")
    if not args.tests:
        ignoredDirs.append("test")
        ignoredDirs.append("tests")

    if args.list_cscs:
        print(", ".join(sorted(extractCscs(args.SALSubsystems))))
        sys.exit(0)

    if args.output:
        if not hasExtension(args.output, ["yaml"]):
            print(f"Only yaml output files are currently supported; saw {args.output}", file=sys.stderr)
            sys.exit(1)

    if args.patchCscNames:
        #
        # this is at global scope, and replaces a no-op definition
        #
        def patch_csc_name(name):       # noqa: F811
            """Patch a component name which we guessed originally
            E.g.
               FooCsc    -> Foo
               SALPY_Goo -> Goo
            """
            for regex in [r"^(.*)(?<!_)(?i:csc)$",
                          r"^SALPY_(.*)$",
                          ]:
                mat = re.search(regex, name)
                if mat:
                    nname = mat.group(1)
                    if nname not in "CSC":  # just confusing
                        return nname

            return name
    #
    # Traverse all the specified directories looking for components
    #
    controllers = {}
    remotes = {}
    for d in dirs:
        name = os.path.basename(d)

        process_tree(d, controllers, remotes, ignoredDirs, name=name, extensions=args.extensions,
                     include_notebooks=args.notebooks, use_ast=args.use_ast, verbose=args.verbose)
    #
    # Remove potential CSCs that aren't listed in the XML list, after fixing
    # names that look plausible (e.g. if we don't find Foo but do find FooCsc
    # we'll rename the latter)
    #
    renamedCsc = {}
    if args.checkCscList or args.missing_cscs:
        try:
            cscs = extractCscs(args.SALSubsystems)
        except FileNotFoundError as e:
            print(f"{e}; skipping CSC checks", file=sys.stdout)
            cscs = []
            args.checkCscList = False

        foundControllers = set()
        if args.missing_cscs or args.patchCscNames:
            missingControllers = set(cscs)
            for name in controllers:
                for filename in controllers[name]:
                    for cpt in controllers[name][filename]:
                        missingControllers.discard(cpt.name)

            if args.missing_cscs:
                print(f"Failed to find some CSCs: {', '.join(sorted(list(missingControllers)))}" + "\n")
            #
            # See if we recognise the controllers
            #
            if args.checkCscList:
                for name in controllers:
                    for filename in controllers[name]:
                        for cpt in controllers[name][filename]:
                            controllers[name][filename] = \
                                [cpt for cpt in controllers[name][filename] if cpt.name in cscs]
                            if filename in remotes[name]:
                                remotes[name][filename] = \
                                    [cpt for cpt in remotes[name][filename] if cpt.name in cscs]
    #
    # Patch up some failures to understand some of the more complex CSCs
    #
    if args.fixCscComponents:
        #
        # Invent the CCS controllers from whole cloth
        #
        # Cheat a bit with the HeaderService, because the code base can
        # handle multiple cameras as it calls # all of them `name` in a
        # python loop
        #
        dummy = "dummy.file"

        controllers["HeaderService"] = {dummy: []}  # was ["filename"][Controller("name")]
        for cam in ["AT", "CC", "MT"]:
            controllers[f"{cam}Camera"] = {dummy: [Controller(f"{cam}Camera")]}

            if cam == "AT":
                controllers["HeaderService"][dummy].append(Controller(f"{cam}HeaderService"))
        #
        # Code has another layer of introspection and calls the
        # cptName "cscName"
        #
        controllers["ts_MTAOS"] = {dummy: [Controller("MTAOS")]}
    #
    # Write out our discoveries
    #
    if args.output:
        yamlData = dict(controllers={},
                        remotes={})

        for name in controllers:
            ctrls = sum(controllers[name].values(), [])
            rems =  sum(remotes[name].values(), []) if name in remotes else [] # noqa: #222

            if ctrls:
                yamlData["controllers"][name] = sorted(set([cpt.name for cpt in ctrls]))
            if rems:
                yamlData["remotes"][name] =     sorted(set([cpt.name for cpt in rems]))  # noqa: #222

        with open(args.output, "w") as fd:
            yaml.dump(yamlData, fd, yaml.CDumper)
    else:
        for name in controllers:
            ctrls = sum(controllers[name].values(), [])
            rems =  sum(remotes[name].values(), []) if name in remotes else [] # noqa: #222

            if ctrls:
                print(f"{name:40s} Controllers: {', '.join(sorted(set([cpt.name for cpt in ctrls])))}")

                if args.show_filenames:
                    for cpt in ctrls:
                        print(f"{'':53} {cpt.name:20} {cpt.path}:{cpt.lineNo}")
                        if args.show_lines:
                            print(f"{'':63} {cpt.line}")

            if rems:
                print(f"{name:40s} Remotes:     {', '.join(sorted(set([cpt.name for cpt in rems])))}")

                if args.show_filenames:
                    for cpt in rems:
                        print(f"{'':53} {cpt.name:20} {cpt.path}:{cpt.lineNo}")
                        if args.show_lines:
                            print(f"{'':63} {cpt.line}")
