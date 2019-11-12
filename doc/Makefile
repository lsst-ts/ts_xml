subsystemData.csv:
	python generateCSVTable.py
	python generate_csc_information.py

.PHONY: html
html: subsystemData.csv
	package-docs -d . build
