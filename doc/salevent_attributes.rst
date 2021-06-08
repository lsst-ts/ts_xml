**********************
SALEventSet Attributes
**********************

Below are the descriptions and content recommendations for SALEventSet.xml
attributes.

SALEventSet
===========

**Data Type**: eventSetType

This is a complex type for an abritrary set of SALEvent definitions

SALEvent
========

**Data Type**: eventType

This the complex type for the definition of a partcular event. 
It consists of a set of metatdata fields , plus an optional set of 
data item definitions.

SALEventItem
============

**Data Type**: eventItemType

This is an optional element which may be used an arbitrary number 
of times to add data items to a event definition.

EFDB_Name
=========

**Data Type**: string

This is the Engineering and Facility Database (EFD) column name used to 
store the historical record for this item. It is also used for the 
on-the-wire DDS topic field, and the item name in the 
SAL language specific API's. 

Description
===========

**Data Type**: string

This is a brief description of the purpose of the event. 

IDL_Type
========

**Data Type**: string

This is the Interface Definition Language (IDL) data type of 
the data item.

IDL_Size
========

**Data Type**: integer

For IDL string types this is used to specify the length in characters
(UTF-8 ie bytes). A special case is IDL_Size=1, which is interpreted as
variable/unlimited length string

Units
=====

**Data Type**: string

This is used to specify the units (as supported by the astropy unit
library), or unitless if it is not applicable.

Count
=====

**Data Type**: integer

This is used to specify the length of numerical array data types.
Arrays of string type are NOT supported.

eventType
=========

**Data Type**: complexType

This is a complex type for an SALEvent definition with an 
optional set of data items.

Subsystem
=========

**Data Type**: string

This is used to specify which subsystem the event is associated
with.

EFDB_Topic
==========

**Data Type**: string

This is the Engineering and Facility Database (EFD) table name used to 
store the historical record for this event. It is also used for the 
on-the-wire DDS topic name and type, and the structure name in the 
SAL language specific API's. 


Enumeration
===========

**Data Type**: comma-delimited list of names, key, value pairs or a string

This is a list of either items which will be assigned enumerated values
ie, 1,2,3...

OR

a list of item=value definitions, in which case the specified values
will be assigned to each named item.

An Enumeration may be specific (internal) to a data field definition <item>, 
or if it appears outside of the <EventSet>, it applies globally.

