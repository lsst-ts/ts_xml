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


	if count == 0:
		name = member.find('Name').tag
		subsystem_head.append(name)
		
		active_developers = member.find('ActiveDevelopers').tag
		subsystem_head.append(active_developers)

		CAM = member.find('CAM').tag
		subsystem_head.append(CAM)

		github = member.find('Github').tag
		subsystem_head.append(github)

		jenkins_test_results = member.find('JenkinsTestResults').tag
		subsystem_head.append(jenkins_test_results)

		LSSTPoC = member.find('LSSTPoC').tag
		subsystem_head.append(LSSTPoC)

		LSSTIO = member.find('LSSTIO').tag
		subsystem_head.append(LSSTIO)

		product_owner = member.find('ProductOwner').tag
		subsystem_head.append(product_owner)

		related_documents = member.find('RelatedDocuments').tag
		subsystem_head.append(related_documents)

		software_language = member.find('SoftwareLanguage').tag
		subsystem_head.append(software_language)

		vendor_PoC = member.find('VendorPoC').tag
		subsystem_head.append(vendor_PoC)

		XML = member.find('XML').tag
		subsystem_head.append(XML)

		principal_system = member.find('PrincipalSystem').tag
		subsystem_head.append(principal_system)

		csvwriter.writerow(subsystem_head)
		count = count + 1

	name = member.find('Name').text
	subsystem.append(name)

	active_developers = member.find('ActiveDevelopers').text
	subsystem.append(active_developers)

	CAM = member.find('CAM').text
	subsystem.append(CAM)

	github = member.find('Github').text
	subsystem.append(github)

	jenkins_test_results = member.find('JenkinsTestResults').text
	subsystem.append(jenkins_test_results)

	LSSTPoC = member.find('LSSTPoC').text
	subsystem.append(LSSTPoC)

	LSSTIO = member.find('LSSTIO').text
	subsystem.append(LSSTIO)

	product_owner = member.find('ProductOwner').text
	subsystem.append(product_owner)

	related_documents = member.find('RelatedDocuments').text
	subsystem.append(related_documents)

	software_language = member.find('SoftwareLanguage').text
	subsystem.append(software_language)

	vendor_PoC = member.find('VendorPoC').text
	subsystem.append(vendor_PoC)

	XML = member.find('XML').text
	subsystem.append(XML)

	principal_system = member.find('PrincipalSystem').text
	subsystem.append(principal_system)

	csvwriter.writerow(subsystem)

subsystem_data.close()