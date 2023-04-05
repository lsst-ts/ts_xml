# This file is part of ts_xml
#
# Developed for the LSST Data Management System.
# This product includes software developed by the LSST Project
# (https://www.lsst.org).
# See the COPYRIGHT file at the top-level directory of this distribution
# for details of code ownership.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License

__all__ = ["generate_csv_table"]

import bisect
import csv
from xml.etree import ElementTree

from .utils import (
    find_in_xml,
    find_tag_in_xml,
    find_text_in_xml,
    get_pkg_root,
    get_sal_interfaces_dir,
)


def generate_csv_table() -> None:
    sal_interfaces_dir = get_sal_interfaces_dir()
    tree = ElementTree.parse(sal_interfaces_dir / "SALSubsystems.xml")
    root = tree.getroot()

    outpath = get_pkg_root() / "doc" / "subsystemData.csv"
    with open(outpath, "w") as subsystem_data:
        csvwriter = csv.writer(subsystem_data)
        subsystem_head: list[str] = []

        count = 0
        for member in root.findall("SALSubsystem"):
            subsystem: list[str | None] = []

            # Here we add the table header.
            # It may be redundant to find the names of the XML tag,
            # but it makes sure we aren't adding a header
            # for an XML tag that is non-existent.
            if count == 0:
                find_tag_in_xml(member, "Name")
                subsystem_head.append("Subystem")

                find_tag_in_xml(member, "ActiveDevelopers")
                subsystem_head.append("Active Developers")

                find_tag_in_xml(member, "Github")
                subsystem_head.append("Github")

                find_tag_in_xml(member, "Simulator")
                subsystem_head.append("Simulator")

                find_tag_in_xml(member, "JenkinsTestResults")
                subsystem_head.append("Jenkins Test Results")

                find_tag_in_xml(member, "RubinObsContact")
                subsystem_head.append("Rubin Observatory Contact")

                find_tag_in_xml(member, "CSCDocs")
                subsystem_head.append("CSC Docs")

                find_tag_in_xml(member, "ProductOwner")
                subsystem_head.append("Product Owner")

                find_tag_in_xml(member, "RelatedDocuments")
                subsystem_head.append("Related Documents")

                find_tag_in_xml(member, "SoftwareLanguage")
                subsystem_head.append("Software Language")

                find_tag_in_xml(member, "RuntimeLanguages")
                subsystem_head.append("Runtime Language")

                find_tag_in_xml(member, "VendorContact")
                subsystem_head.append("Vendor Contact")

                find_tag_in_xml(member, "Configuration")
                subsystem_head.append("Configuration")

                find_tag_in_xml(member, "IndexEnumeration")
                subsystem_head.append("IndexEnumeration")

                csvwriter.writerow(subsystem_head)
                count = count + 1

            # Use find_text_in_xml if field text is required,
            # find_in_xml if not
            name = find_text_in_xml(member, "Name")
            subsystem.append(
                f".. _index:csc-table:{name.lower()}:\n\n:doc:`/sal_interfaces/{name}`"
            )

            active_developers = find_text_in_xml(member, "ActiveDevelopers")
            subsystem.append(active_developers)

            github = find_text_in_xml(member, "Github")
            subsystem.append(github)

            simulator = find_text_in_xml(member, "Simulator")
            subsystem.append(simulator)

            jenkins_test_results = find_text_in_xml(member, "JenkinsTestResults")
            subsystem.append(jenkins_test_results)

            RubinObsContact = find_text_in_xml(member, "RubinObsContact")
            subsystem.append(RubinObsContact)

            CSCDocs = find_in_xml(member, "CSCDocs")
            subsystem.append(CSCDocs.text)

            product_owner = find_text_in_xml(member, "ProductOwner")
            subsystem.append(product_owner)

            related_documents = find_in_xml(member, "RelatedDocuments")
            subsystem.append(related_documents.text)

            software_language = find_in_xml(member, "SoftwareLanguage")
            subsystem.append(software_language.text)

            runtime_languages = find_text_in_xml(member, "RuntimeLanguages")
            subsystem.append(runtime_languages)

            vendor_contact = find_text_in_xml(member, "VendorContact")
            subsystem.append(vendor_contact)

            configuration = find_text_in_xml(member, "Configuration")
            subsystem.append(configuration)

            index_enumeration = find_text_in_xml(member, "IndexEnumeration")
            subsystem.append(index_enumeration)

            csvwriter.writerow(subsystem)

    # Alphabetize the CSV file.
    with open("subsystemData.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        line_count = 0

        header = []
        ordered_data = []

        for row in csv_reader:
            # Add the header
            if line_count == 0:
                header = row
                line_count += 1

            # Add our first row into the list, iterate onto the next row
            elif line_count == 1:
                ordered_data.append(row)
                line_count += 1

            # Place the rest of the rows into an ordered list based off the 1st
            # element
            else:
                # Note: the key function is only applied to elements
                # of the sorted list (first argument), not the item
                # being inserted (second argument).
                insertion_index = bisect.bisect_left(
                    ordered_data, row[0], key=lambda x: x[0]
                )
                ordered_data.insert(insertion_index, row)

    # Write the ordered data into file
    with open("orderedSubsystemData.csv", "w") as subsystem_data:
        csvwriter = csv.writer(subsystem_data)
        csvwriter.writerow(header)

        for row in ordered_data:
            csvwriter.writerow(row)
