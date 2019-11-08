#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astropy.units

class Unit_Validator():

	def check_unit(self, unit_str):
		try:
			return astropy.units.Quantity("1 " + unit_str)
		except ValueError:
			return "ValueError: " + unit_str + " is not a valid unit."
		except:
			return "UnknownError: " + unit_str

if __name__ == "__main__":
	Unit_Validator.main()
