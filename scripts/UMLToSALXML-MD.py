
import sys
import xml.etree.ElementTree

ignoreGlobals = True
globalCommands = ["Start", "Enable", "Disable", "Standby"]
globalEvents = ["ErrorCode", "SummaryState", "SettingVersions", "AppliedSettingsMatchStart", "SettingsApplied"]

class UMLParser:
    def Open(self, subsystem, version, umlFile):
        tempUMLFile = umlFile + ".tmp"
        with open(tempUMLFile, "w") as tempFile:
            with open(umlFile, "r") as inputFile:
                for line in inputFile:
                    tempFile.write(line.replace("<UML:", "<").replace("</UML:", "</").replace("xmi:id","xmiid"))

        self.subsystem = subsystem
        self.version = version
        self.uml = xml.etree.ElementTree.parse(tempUMLFile)
        
    def Parse(self, outputDirectory):
        self.outputDirectory = outputDirectory
        self.WriteCommands(self.GetCommands())
        self.WriteEvents(self.GetEvents())
        self.WriteTelemetry(self.GetTelemetry())
        
    def WriteCommands(self, commands):
        header = """<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="http://lsst-sal.tuc.noao.edu/schema/SALCommandSet.xsl"?>
<SALCommandSet xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:noNamespaceSchemaLocation="http://lsst-sal.tuc.noao.edu/schema/SALCommandSet.xsd">"""
        footer = """</SALCommandSet>"""
        with open("%s\\%s_Commands.xml" % (self.outputDirectory, self.subsystem), "w") as commandFile:  
            commandFile.write(header)
            for item in commands:
                if item.name != "Command":
                    if not (ignoreGlobals and item.name in globalCommands):
                        commandFile.write(item.CreateSALXML())
            commandFile.write(footer)          
            
    def WriteEvents(self, events):
        header = """<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="http://lsst-sal.tuc.noao.edu/schema/SALEventSet.xsl"?>
<SALEventSet xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:noNamespaceSchemaLocation="http://lsst-sal.tuc.noao.edu/schema/SALEventSet.xsd">"""
        footer = """</SALEventSet>"""
        with open("%s\\%s_Events.xml" % (self.outputDirectory, self.subsystem), "w") as eventFile:  
            eventFile.write(header)
            for item in events:
                if item.name != "Event":
                    if not (ignoreGlobals and item.name in globalEvents):
                        eventFile.write(item.CreateSALXML())
            eventFile.write(footer)     

    def WriteTelemetry(self, telemetry):
        header = """<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="http://lsst-sal.tuc.noao.edu/schema/SALTelemetrySet.xsl"?>
<SALTelemetrySet xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:noNamespaceSchemaLocation="http://lsst-sal.tuc.noao.edu/schema/SALTelemetrySet.xsd">"""
        footer = """</SALTelemetrySet>"""
        with open("%s\\%s_Telemetry.xml" % (self.outputDirectory, self.subsystem), "w") as telemetryFile:  
            telemetryFile.write(header)
            for item in telemetry:
                if item.name != "Telemetry":
                    telemetryFile.write(item.CreateSALXML())
            telemetryFile.write(footer)     

    def GetCommands(self):
        commands = []
        for item in self.GetCommandList():
            commands.append(self.CreateSALCommand(item))
        return commands
        
    def GetEvents(self):
        events = []
        for item in self.GetEventList():
            events.append(self.CreateSALEvent(item))
        return events
        
    def GetTelemetry(self):
        telemetry = []
        for item in self.GetTelemetryList():
            telemetry.append(self.CreateSALTelemetry(item))
        return telemetry
        
    def CreateSALCommand(self, command):
        basePath = ".//packagedElement[@name='SAL interface']/packagedElement[@name='Command']/packagedElement[@name='%s']/ownedAttribute" % (command)
        author = ""#self.GetValue(self.uml.find(basePath % "author"), "UNDEFINED")
        parameters = []
        for parameter in self.GetCommandParameterList(command):
            parameters.append(self.CreateSALParameter("Command", command, parameter))
        return SALCommand(self.subsystem, self.version, author, command, parameters)
        
    def CreateSALEvent(self, event):
        basePath = ".//packagedElement[@name='SAL interface']/packagedElement[@name='Event']/packagedElement[@name='%s']/ownedAttribute" % (event)
        author = ""#self.GetValue(self.uml.find(basePath), "UNDEFINED")
        parameters = []
        for parameter in self.GetEventParameterList(event):
            parameters.append(self.CreateSALParameter("Event", event, parameter))
        return SALEvent(self.subsystem, self.version, author, event, parameters)
        
    def CreateSALTelemetry(self, telemetry):
        basePath = ".//packagedElement[@name='SAL interface']/packagedElement[@name='Telemetry']/packagedElement[@name='%s']/ownedAttribute" % (telemetry)
        author = ""#self.GetValue(self.uml.find(basePath % "author"), "UNDEFINED")
        parameters = []
        for parameter in self.GetTelemetryParameterList(telemetry):
            parameters.append(self.CreateSALParameter("Telemetry", telemetry, parameter))
        return SALTelemetry(self.subsystem, self.version, author, telemetry, parameters)

    def CreateSALParameter(self, type, command, parameter):
        basePath = ".//packagedElement[@name='SAL interface']/packagedElement[@name='%s']/packagedElement[@name='%s']/ownedAttribute[@name='%s']%s" % (type, command, parameter,'%s')
        description = self.GetValueByName(self.uml.find(basePath % "/ownedComment"), "body", "")
        description = description.replace("<html><pre>", "").replace("</html></pre>", "")
		
        typeID = self.GetValueByName(self.uml.find(basePath % ""), "type", "UNDEFINED")
        type = self.TypeIDtoType(typeID)
        
        units = self.GetValueByName(self.uml.find(basePath % ""),"unit", " ") 
        units = "" if units is None else units
		
        if type == "string":
            count = self.GetValueByName(self.uml.find(basePath % "/upperValue"),"value", "256")
            return SALParameterString(parameter, description, type, units, count)
        else:
            count = self.GetValueByName(self.uml.find(basePath % "/upperValue"),"value", "1")
            return SALParameter(parameter, description, type, units, count)
        
    def GetCommandList(self):
        return [command.get("name") for command in self.uml.findall(".//packagedElement[@name='SAL interface']/packagedElement[@name='Command']/packagedElement")]
  
    def GetCommandParameterList(self, command):
        return [parameter.get("name") for parameter in self.uml.findall(".//packagedElement[@name='SAL interface']/packagedElement[@name='Command']/packagedElement[@name='%s']/ownedAttribute" % command)]

    def GetEventList(self):
        return [event.get("name") for event in self.uml.findall(".//packagedElement[@name='SAL interface']/packagedElement[@name='Event']/packagedElement")]
        
    def GetEventParameterList(self, event):
        return [parameter.get("name") for parameter in self.uml.findall(".//packagedElement[@name='SAL interface']/packagedElement[@name='Event']/packagedElement[@name='%s']/ownedAttribute" % event)]
                
    def GetTelemetryList(self):
        return [telemetry.get("name") for telemetry in self.uml.findall(".//packagedElement[@name='SAL interface']/packagedElement[@name='Telemetry']/packagedElement")]
        
    def GetTelemetryParameterList(self, telemetry):
        return [parameter.get("name") for parameter in self.uml.findall(".//packagedElement[@name='SAL interface']/packagedElement[@name='Telemetry']/packagedElement[@name='%s']/ownedAttribute" % telemetry)]      

    def GetValue(self, node, default):
        return node.get("value") if node is not None else default

    def GetValueByName(self, node, value, default):
        return node.get(value) if node is not None else default

    def TypeIDtoType(self, typeID):
        path = ".//packagedElement[@name='IDL Datatype']/packagedElement[@xmiid='%s']" % typeID 
        node = self.uml.find(path)
        return node.get("name") if node is not None else 'Error'

class SALParameter:
    template = """
    <item>
        <EFDB_Name>%s</EFDB_Name>
        <Description>%s</Description>
        <IDL_Type>%s</IDL_Type>
        <Units>%s</Units>
        <Count>%s</Count>
        <Explanation>http://sal.lsst.org</Explanation>
    </item>"""
    
    def __init__(self, name, description, type, units, count):
        self.name = name
        self.description = description
        self.type = type
        self.units = units
        self.count = count
        
    def CreateSALXML(self):
        return self.template % (self.name, self.description, self.type, self.units, self.count)

class SALParameterString:
    template = """
    <item>
        <EFDB_Name>%s</EFDB_Name>
        <Description>%s</Description>
        <IDL_Type>%s</IDL_Type>
        <IDL_Size>%s</IDL_Size>
        <Units>%s</Units>
        <Count>%s</Count>
        <Explanation>http://sal.lsst.org</Explanation>
    </item>"""
    
    def __init__(self, name, description, type, units, count):
        self.name = name
        self.description = description
        self.type = type
        self.units = units
        self.count = count
        
    def CreateSALXML(self):
        return self.template % (self.name, self.description, self.type, self.count, self.units, '1')
		
class SALCommand:
    template = """
<SALCommand>
    <Subsystem>%s</Subsystem>
    <Version>%s</Version>
    <Author>%s</Author>
    <EFDB_Topic>%s</EFDB_Topic>
    <Alias>%s</Alias>
    <Explanation>http://sal.lsst.org</Explanation>%s
</SALCommand>"""
    
    def __init__(self, subsystem, version, author, name, parameters):
        self.subsystem = subsystem
        self.version = version
        self.author = author
        self.name = name
        self.parameters = parameters
        
    def CreateSALXML(self):
        topic = "%s_command_%s" % (self.subsystem, self.name)
        alias = self.name
        items = ""
        for parameter in self.parameters:
            items = items + parameter.CreateSALXML()
        return self.template % (self.subsystem, self.version, self.author, topic, alias, items)

class SALEvent:
    template = """
<SALEvent>
    <Subsystem>%s</Subsystem>
    <Version>%s</Version>
    <Author>%s</Author>
    <EFDB_Topic>%s</EFDB_Topic>
    <Alias>%s</Alias>
    <Explanation>http://sal.lsst.org</Explanation>%s
</SALEvent>"""

    def __init__(self, subsystem, version, author, name, parameters):
        self.subsystem = subsystem
        self.version = version
        self.author = author
        self.name = name
        self.parameters = parameters

    def CreateSALXML(self):
        topic = "%s_logevent_%s" % (self.subsystem, self.name)
        alias = self.name
        items = ""
        for parameter in self.parameters:
            items = items + parameter.CreateSALXML()
        return self.template % (self.subsystem, self.version, self.author, topic, alias, items)

class SALTelemetry:
    template = """
<SALTelemetry>
    <Subsystem>%s</Subsystem>
    <Version>%s</Version>
    <Author>%s</Author>
    <EFDB_Topic>%s</EFDB_Topic>
    <Explanation>http://sal.lsst.org</Explanation>%s
</SALTelemetry>"""

    def __init__(self, subsystem, version, author, name, parameters):
        self.subsystem = subsystem
        self.version = version
        self.author = author
        self.name = name
        self.parameters = parameters
        
    def CreateSALXML(self):
        topic = "%s_%s" % (self.subsystem, self.name)
        items = ""
        for parameter in self.parameters:
            items = items + parameter.CreateSALXML()
        return self.template % (self.subsystem, self.version, self.author, topic, items)

        
if len(sys.argv) != 6:
    print """
Version: 1.1
    
usage: *.py <SubSystem> <SALVersion> <UMLFile> <OutputDirectory> <IgnoreGlobals(T/F)>
example: *.py m2ms 3.5.0 D:\Temp\SALTemp.xml D:\Temp T

Notes:
    1. Commands must be a direct child of a package named Command
    2. Commands must not be named Command, otherwise it will be ignored
    3. Events must be a direct child of a package named Event
    4. Events must not be named Event, otherwise it will be ignored
    5. Telemetry must be a direct child of a package named Telemetry
    6. Telemetry must not be named Telemetry, otherwise it will be ignored
    7. If you want parameters to have units defined, create a new tag named 'unit'"""
else:
    ignoreGlobals = sys.argv[5] == "T"
    print("Executing UML XMI 2.1 from MagicDraw to SAL XML")
    print("UML Parser...")
    uml = UMLParser()
    print("Opening XML Model...")
    uml.Open(sys.argv[1], sys.argv[2], sys.argv[3])
    print("Parsing...")
    uml.Parse(sys.argv[4])
    print("Completed succesfully...")