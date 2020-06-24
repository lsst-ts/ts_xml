import xml.etree.ElementTree as ET

def main():
    tree = ET.parse("../sal_interfaces/SALSubsystems.xml")
    root = tree.getroot()
    csc_info = open("csc_information.rst", "w")
    csc_info.write(
        """***************
CSC Information
***************\n
""")
    for subsystem in root:
        for attribute in subsystem:
            if attribute.tag == "Name":
                csc_info.write(f"\n.. _{attribute.text.lower()}:\n")
                heading_string = "="
                csc_info.write(f"\n{attribute.text}\n")
                csc_info.write(f"{heading_string * len(attribute.text)}\n\n")
            else:
                csc_info.write(f":{attribute.tag}: {attribute.text}\n")
    csc_info.close()

if __name__ == "__main__":
    main()
