subsystemData.csv:
	python generateCSVTable.py

.PHONY: html
html: subsystemData.csv
	package-docs -d . build
