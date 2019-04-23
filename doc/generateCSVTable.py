import xml.etree.ElementTree as ET
import csv

tree = ET.parse("../sal_interfaces/SALSubsystems.xml")
root = tree.getroot()

# open file for writing

subsystem_data = open('subsystemData.csv', 'w')

# create the csv writer object

csvwriter = csv.writer(subsystem_data)
subsystem_head = []

count = 0
for member in root.findall('Subsystem'):
	subsystem = []


	# Here we add the table header. It may be redundent to fine the names of the
	# XML tag however I do it anyways to be sure we arent adding a header for an
	# XML tag that is non-existent. 
	if count == 0:
		name = member.find('Name').tag
		subsystem_head.append('Subystem')
		
		active_developers = member.find('ActiveDevelopers').tag
		subsystem_head.append("Active Developers")

		principal_csc_owner = member.find('PrincipalCSCOwner').tag
		subsystem_head.append('Principal CSC Owner')

		github = member.find('Github').tag
		subsystem_head.append('Github')

		jenkins_test_results = member.find('JenkinsTestResults').tag
		subsystem_head.append("Jenkins Test Results")

		CSCDocs = member.find('CSCDocs').tag
		subsystem_head.append('CSC Docs')

		product_owner = member.find('ProductOwner').tag
		subsystem_head.append('Product Owner')

		related_documents = member.find('RelatedDocuments').tag
		subsystem_head.append('Related Documents')

		software_language = member.find('SoftwareLanguage').tag
		subsystem_head.append('Software Language')

		vendor_PoC = member.find('VendorPoC').tag
		subsystem_head.append('Vendor PoC')

		csvwriter.writerow(subsystem_head)
		count = count + 1

	name = member.find('Name').text
	subsystem.append(name)

	active_developers = member.find('ActiveDevelopers').text
	subsystem.append(active_developers)

	principal_csc_owner = member.find('PrincipalCSCOwner').text
	subsystem.append(principal_csc_owner)

	github = member.find('Github').text
	subsystem.append(github)

	jenkins_test_results = member.find('JenkinsTestResults').text
	subsystem.append(jenkins_test_results)

	LSSTPoC = member.find('LSSTPoC').text
	subsystem.append(LSSTPoC)

	CSCDocs = member.find('CSCDocs').text
	subsystem.append(CSCDocs)

	product_owner = member.find('ProductOwner').text
	subsystem.append(product_owner)

	related_documents = member.find('RelatedDocuments').text
	subsystem.append(related_documents)

	software_language = member.find('SoftwareLanguage').text
	subsystem.append(software_language)

	vendor_PoC = member.find('VendorPoC').text
	subsystem.append(vendor_PoC)

	csvwriter.writerow(subsystem)

subsystem_data.close()