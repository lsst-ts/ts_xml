csc_info:
	python generateCSVTable.py
	python generate_cet.py

.PHONY: html
html: csc_info
	package-docs -d . build

clean: 
	package-docs clean
	rm subsystemData.csv orderedSubsystemData.csv
	rm -rf sal_interfaces
	rm sal_generics.rst
