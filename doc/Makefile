csc_info:
	python generate_csc_information.py
	python generateCSVTable.py
	python generate_cet.py

.PHONY: html
html: csc_info
	package-docs -d . build

clean: 
	package-docs clean
	rm csc_information.rst subsystemData.csv orderedSubsystemData.csv
	rm -rf sal_interfaces
