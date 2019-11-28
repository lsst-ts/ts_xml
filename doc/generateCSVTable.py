import xml.etree.ElementTree as ET
import operator
import csv
import bisect

tree = ET.parse("../sal_interfaces/SALSubsystems.xml")
root = tree.getroot()

# open file for writing

subsystem_data = open('subsystemData.csv', 'w')

# create the csv writer object

csvwriter = csv.writer(subsystem_data)
subsystem_head = []

count = 0
for member in root.findall('SALSubsystem'):
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

		simulator = member.find('Simulator').tag
		subsystem_head.append('Simulator')

		jenkins_test_results = member.find('JenkinsTestResults').tag
		subsystem_head.append("Jenkins Test Results")

		LSSTPoC = member.find('LSSTPoC').text
		subsystem_head.append('LSST PoC')

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

		error_code = member.find('ErrorCode').tag
		subsystem_head.append('Error Code')

		configurable = member.find('Configurable').tag
		subsystem_head.append('Configurable')

		csvwriter.writerow(subsystem_head)
		count = count + 1

	name = member.find('Name').text
	subsystem.append(f" :ref:`{name.lower()}`")

	active_developers = member.find('ActiveDevelopers').text
	subsystem.append(active_developers)

	principal_csc_owner = member.find('PrincipalCSCOwner').text
	subsystem.append(principal_csc_owner)

	github = member.find('Github').text
	subsystem.append(github)

	simulator = member.find('Simulator').text
	subsystem.append(simulator)

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

	error_code = member.find('ErrorCode').text
	subsystem.append(error_code)

	configurable = member.find('Configurable').text
	subsystem.append(configurable)

	csvwriter.writerow(subsystem)

subsystem_data.close()

# We have converted an xml table into a csv file with a header, however it is
# not alphabetized. We do this here.
with open('subsystemData.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	line_count = 0
	i=0

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
			line_count+=1

		# Place the rest of the rows into an ordered list based off the 1st ele
		else:			
			index = 0
			for each_ordered_row in ordered_data:
				if row[0] < ordered_data[index][0]: #a
											
					break
				index+=1
			ordered_data.insert(index, row)

	# Write the ordered data into file
	subsystem_data = open('orderedSubsystemData.csv', 'w')
	csvwriter = csv.writer(subsystem_data)
	csvwriter.writerow(header)

	for row in ordered_data:
		csvwriter.writerow(row)
