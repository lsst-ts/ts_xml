import xml.etree.ElementTree as ET
from lsst.ts.xml import testutils
import pathlib


def provide_ignored():
    ignored_attributes = ["EFDB_Name", "Description"]
    ignored_fields = ["Description", "Alias", "Device", "Property", "Action", "Value", "Subsystem", "Version", "Author", "Explanation"]
    return ignored_attributes, ignored_fields

def add_generics(cf, subsystem, set_name, has_generics, has_specific):
    ignored_attributes, ignored_fields = provide_ignored()
    if has_generics is True:
        gen_tree = ET.parse("../sal_interfaces/SALGenerics.xml")
        gen_root = gen_tree.getroot()
        for gen_set in gen_root:
            gen_set[:] = sorted(gen_set, key=lambda child: (child.tag, child.find("EFDB_Topic").text.split("_")[-1] if child.find("EFDB_Topic") is not None else child.tag))
            gen_set_name = gen_set.tag
            if gen_set_name == set_name:
                if gen_set_name[3:-3] not in has_specific:
                    cf.write(f"{gen_set_name[3:-3]}s\n")
                    cf.write(f"{'-'*len(gen_set_name[3:-3]+'s')}\n")
                for gen_topic in gen_set:
                    topic_name = gen_topic.find('EFDB_Topic').text
                    short_name = topic_name.split("_")[-1]
                    cf.write(f"{short_name}\n")
                    cf.write(f"{'~'*len(short_name)}\n")
                    gen_topic_description = gen_topic.find("Description")
                    if gen_topic_description is not None:
                        cf.write("**Description**: ")
                        cf.write(f"{gen_topic_description.text}\n")
                        cf.write(f"\n")
                    for gen_field in gen_topic:
                        if gen_field.tag == "item":
                            gen_field_name = gen_field.find('EFDB_Name')
                            gen_field_description = gen_field.find('Description')
                            cf.write("\n")
                            cf.write(f".. _{subsystem}:{short_name}:{gen_field_name.text}:\n\n")
                            cf.write(f"{gen_field_name.text}\n")
                            cf.write(f"{'*'*len(gen_field_name.text)}\n")
                            for gen_attribute in gen_field:
                                if gen_attribute.tag in ["Count", "IDL_Size"]:
                                    if gen_attribute.text == "1":
                                        pass
                                    else:
                                        cf.write(f":{gen_attribute.tag}: {gen_attribute.text}\n")
                                elif gen_attribute.tag in ignored_attributes:
                                    pass
                                else:
                                    cf.write(f":{gen_attribute.tag}: {gen_attribute.text}\n")
                            cf.write("\n")
                            cf.write("**Description**: ")
                            cf.write(f"{gen_field_description.text}\n")
                            cf.write("\n")
                        elif gen_field.tag in ignored_fields:
                            pass
                        else:
                            cf.write(f":{gen_field.tag}: {gen_field.text}\n")
                        cf.write("\n")
            else:
                pass

    elif has_generics is False:
        pass
    else:
        gen_tree = ET.parse("../sal_interfaces/SALGenerics.xml")
        gen_root = gen_tree.getroot()
        for gen_set in gen_root:
            gen_set[:] = sorted(gen_set, key=lambda child: (child.tag, child.find("EFDB_Topic").text.split("_")[-1] if child.find("EFDB_Topic") is not None else child.tag))
            gen_set_name = gen_set.tag
            if gen_set_name == set_name:
                if gen_set_name[3:-3] not in has_specific:
                    cf.write(f"{gen_set_name[3:-3]}s\n")
                    cf.write(f"{'-'*len(gen_set_name[3:-3]+'s')}\n")
                for gen_topic in gen_set:
                    gen_topic_name = gen_topic.find("EFDB_Topic")
                    gen_topic_short_name_array = gen_topic_name.text.split("_")[1:]
                    gen_topic_short_name = '_'.join(gen_topic_short_name_array)
                    if gen_topic_short_name in has_generics:
                        topic_name = gen_topic.find('EFDB_Topic').text
                        short_name = topic_name.split("_")[-1]
                        cf.write(f"{short_name}\n")
                        cf.write(f"{'~'*len(short_name)}\n")
                        gen_topic_description = gen_topic.find("Description")
                        if gen_topic_description is not None:
                            cf.write("**Description**: ")
                            cf.write(f"{gen_topic_description.text}\n")
                            cf.write(f"\n")
                        for gen_field in gen_topic:
                            if gen_field.tag == "item":
                                gen_field_name = gen_field.find('EFDB_Name')
                                gen_field_description = gen_field.find('Description')
                                cf.write("\n")
                                cf.write(f".. _{subsystem}:{short_name}:{gen_field_name.text}:\n\n")
                                cf.write(f"{gen_field_name.text}\n")
                                cf.write(f"{'*'*len(gen_field_name.text)}\n")
                                for gen_attribute in gen_field:
                                    if gen_attribute.tag in ["Count", "IDL_Size"]:
                                        if gen_attribute.text == "1":
                                            pass
                                        else:
                                            cf.write(f":{gen_attribute.tag}: {gen_attribute.text}\n")
                                    elif gen_attribute.tag in ignored_attributes:
                                        pass
                                    else:
                                        cf.write(f":{gen_attribute.tag}: {gen_attribute.text}\n")
                                cf.write("\n")
                                cf.write("**Description**: ")
                                cf.write(f"{gen_field_description.text}\n")
                                cf.write("\n")
                            elif gen_field.tag in ignored_fields:
                                pass
                            else:
                                cf.write(f":{gen_field.tag}: {gen_field.text}\n")
                            cf.write("\n")
                    else:
                        pass

def main():
    ignored_attributes, ignored_fields = provide_ignored()
    pathlib.Path("sal_interfaces").mkdir(parents=True, exist_ok=True)
    f = open(pathlib.Path("sal_interfaces/index.rst"), "w")
    f.write("##############\n")
    f.write("SAL Interfaces\n")
    f.write("##############\n")
    f.write("\n")
    f.write(".. note:: This page is generated by the following python script ``generate_cet.py``.\n\n")
    f.write("This page provides an html display of the SAL Interfaces for the CSCs.\n\n")
    f.write(".. toctree::\n  :glob:\n  :maxdepth: 1\n\n  *\n\n")
    subsystem_tree = ET.parse("../sal_interfaces/SALSubsystems.xml")
    for subsystem in testutils.subsystems:
        has_specific = []
        has_generics = False
        subsystem_tree_root = subsystem_tree.getroot()
        for sal_subsystem in subsystem_tree_root:
            sal_subsystem_name = sal_subsystem.find("Name").text
            if sal_subsystem_name == subsystem:
                generics_text = sal_subsystem.find("Generics").text
                break
        if generics_text == "yes":
            has_generics = True
        elif generics_text == "no":
            has_generics = False
        else:
            has_generics = generics_text
        pathlib.Path("sal_interfaces").mkdir(parents=True, exist_ok=True)
        cf = open(pathlib.Path(f"sal_interfaces/{subsystem}.rst"), "w")
        cf.write(":tocdepth: 3\n\n")
        cf.write(f"{'#'*len(subsystem)}\n")
        cf.write(f"{subsystem}\n")
        cf.write(f"{'#'*len(subsystem)}\n")
        cf.write("\n")
        cf.write(".. note:: This page is generated by the following python script ``generate_cet.py``.\n")
        cf.write("\n")
        cf.write(f":ref:`Back to table <index:master-csc-table:{subsystem.lower()}>`\n")
        cf.write("\n")
        for dds_type in ["Commands", "Events", "Telemetry"]:
            try:
                tree = ET.parse(f"../sal_interfaces/{subsystem}/{subsystem}_{dds_type}.xml")
                has_specific.append(dds_type[:-1])
            except FileNotFoundError:
                add_generics(cf, subsystem, set_name=f"SAL{dds_type[:-1]}Set", has_generics=has_generics, has_specific=has_specific)
                continue
            cf.write(f"{dds_type}\n")
            cf.write(f"{'-'*len(dds_type)}\n")
            root = tree.getroot()
            set_name = root.tag
            # root[:] = sorted(root, key=lambda child: child.get("EFDB_Topic").split("_")[-1] if child.get("EFDB_Topic") is not None else child.tag)
            root[:] = sorted(root, key=lambda child: (child.tag, child.find("EFDB_Topic").text.split("_")[-1] if child.find("EFDB_Topic") is not None else child.tag))
            for topic in root:
                if topic.tag == "Enumeration":
                    states = topic.text.split(',')
                    state_name = states[0].split("_")[0].lstrip()
                    cf.write(f"{state_name}\n")
                    cf.write(f"{'~'*len(state_name)}\n")
                    cf.write("\n")
                    for state in states:
                        cf.write(f"* {state.split('_')[1]}\n")
                    cf.write("------\n")
                    cf.write("\n")
                    continue
                topic_name = topic.find('EFDB_Topic').text
                if dds_type in ["Commands", "Events"]:
                    short_name = topic_name.split("_", 2)[-1]
                else:
                    short_name = topic_name.split("_", 1)[-1]
                cf.write(f".. _{subsystem}:{dds_type}:{short_name}:\n\n")
                cf.write(f"{short_name}\n")
                cf.write(f"{'~'*len(short_name)}\n")
                if topic.find('Description') is not None:
                    cf.write("**Description**: ")
                    cf.write(f"{topic.find('Description').text}\n")
                    cf.write("\n")
                for field in topic:
                    if field.tag == "item":
                        cf.write("\n")
                        cf.write(f".. _{subsystem}:{dds_type}:{short_name}:{field.find('EFDB_Name').text}:\n\n")
                        cf.write(f"{field.find('EFDB_Name').text}\n")
                        cf.write(f"{'*'*len(field.find('EFDB_Name').text)}\n")
                        for attribute in field:
                            if attribute.tag in ignored_attributes:
                                pass
                            elif attribute.tag in ["Count", "IDL_Size"]:
                                if attribute.text == "1":
                                    pass
                                else:
                                    cf.write(f":{attribute.tag}: {attribute.text}\n")
                            else:
                                cf.write(f":{attribute.tag}: {attribute.text}\n")
                        cf.write("\n")
                        cf.write("**Description**: ")
                        cf.write(f"{field.find('Description').text}\n")
                        cf.write("\n")
                    elif field.tag in ignored_fields:
                        pass
                    else:
                        cf.write(f":{field.tag}: {field.text}\n")
                    cf.write("\n")
            add_generics(cf, subsystem, set_name, has_generics, has_specific)


if __name__ == "__main__":
    main()
