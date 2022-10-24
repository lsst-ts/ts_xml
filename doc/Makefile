csc_info:
	python generateCSVTable.py
	python generate_cet.py

.PHONY: html
html: csc_info
	sphinx-build -b html . _build/html -j auto

clean: 
	package-docs clean
	rm subsystemData.csv orderedSubsystemData.csv
	rm -rf sal_interfaces
	rm sal_generics.rst
