.. _Version_History:

===============
Version History
===============

.. WARNING: DO NOT MANUALLY EDIT THIS FILE.

   Release notes are now managed using towncrier.
   The following comment marks the start of the automatically managed content.
   For help in how to create the "news fragments" see the README page in the
   doc directory.

   Do not remove the following comment line.

.. towncrier release notes start

v23.3.2 (2025-08-14)
====================
Package Level
-------------

Other Changes and Additions
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Added the M1M3 ThermocoupleTable table. (`DM-50884 <https://rubinobs.atlassian.net/browse/DM-50884>`_)


Interface Changes
-----------------

MTM1M3
~~~~~~

- Fix M1M3 thermocouple table values. (`DM-51385 <https://rubinobs.atlassian.net/browse/DM-51385>`_, `DM-52055 <https://rubinobs.atlassian.net/browse/DM-52055>`_)


23.3.1 (2025-08-08)
===================
Package Level
-------------

No significant changes.


Interface Changes
-----------------

HVAC
~~~~

- Find a better name for external and ambient temperature parameter of HVAC_lowerAHU0XP05 topics. (`DM-49940 <https://rubinobs.atlassian.net/browse/DM-49940>`_)


v23.3.0 (2025-08-08)
====================
Package Level
-------------

No significant changes.


Interface Changes
-----------------

HVAC
~~~~

- HVAC: Updated commands, events and telemetry. (`OSW-823.hvac <https://rubinobs.atlassian.net/browse/OSW-823.hvac>`_)

Performance Enhancement
~~~~~~~~~~~~~~~~~~~~~~~

MTAOS
~~~~~

- Added visitId and extraId topic to MTAOS events.
  Added gains topics to degree of freedom events in MTAOS. (`DM-52031 <https://rubinobs.atlassian.net/browse/DM-52031>`_)


v23.2.0 (2025-05-20)
====================
Package Level
-------------

Bug Fixes
~~~~~~~~~

- Fixed issue with version file. (`DM-50524 <https://rubinobs.atlassian.net/browse/DM-50524>`_)
- Fixed issue with version import in __init__.py. (`DM-50524 <https://rubinobs.atlassian.net/browse/DM-50524>`_)


Other Changes and Additions
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- FCUTable center_distance method, revive MTM1M3TS.applySetpoint command (`DM-50734 <https://rubinobs.atlassian.net/browse/DM-50734>`_)


Interface Changes
-----------------

MTM1M3
~~~~~~

- * distance method for M1M3 FA data (class). (`DM-48237-II <https://rubinobs.atlassian.net/browse/DM-48237-II>`_)


MTM1M3TS
~~~~~~~~

- Add FCU heater target temperature to the M1M3TS applySetpoint command. (`DM-49538 <https://rubinobs.atlassian.net/browse/DM-49538>`_)
- * Event for target FCU values.
  * Split logging of glycol and FCU heater's target temperatures. (`DM-49538-II <https://rubinobs.atlassian.net/browse/DM-49538-II>`_)


v23.1.0 (2025-03-19)
====================
Package Level
-------------

Documentation
~~~~~~~~~~~~~

- Update RuntimeLanguages in SALSubsystems.xml to replace IDL with Python. (`DM-48864 <https://rubinobs.atlassian.net/browse/DM-48864>`_)


Interface Changes
-----------------

ATSpectrograph
~~~~~~~~~~~~~~

- Added new filterChangePermitted event which publishes whether a filter can be changed. (`DM-49435 <https://rubinobs.atlassian.net/browse/DM-49435>`_)


ESS
~~~

- Add particulate sensor telemetry to ESS. (`DM-49395 <https://rubinobs.atlassian.net/browse/DM-49395>`_)
- Added ringssMeasurement event to ESS for SOAR RINGSS data. (`DM-49413 <https://rubinobs.atlassian.net/browse/DM-49413>`_)
- Add new interface for generator set devices. (`DM-49415 <https://rubinobs.atlassian.net/browse/DM-49415>`_)


HVAC
~~~~

- Add glycol sensors telemetry for white room and clean room. (`DM-49494 <https://rubinobs.atlassian.net/browse/DM-49494>`_)


LinearStage
~~~~~~~~~~~

- Made position field inside of position topic into array. (`DM-48609 <https://rubinobs.atlassian.net/browse/DM-48609>`_)


MTAOS
~~~~~

- * Add `command_startClosedLoop`, `command_stopClosedLoop`, and `logevent_closedLoopState` to the `MTAOS` interface. (`DM-49035 <https://rubinobs.atlassian.net/browse/DM-49035>`_)


MTCamera
~~~~~~~~

- Changes for final (first photon) MTCamera configuration (`CAP-1073 <https://rubinobs.atlassian.net/browse/CAP-1073>`_)


MTDome
~~~~~~

- Change the unit of torque to be Nm. (`DM-48969 <https://rubinobs.atlassian.net/browse/DM-48969>`_)


MTM1M3
~~~~~~

- Add MinimalDistance for bump tests, removed timestamp and actuatorId from BumpTestStatus. (`DM-48237 <https://rubinobs.atlassian.net/browse/DM-48237>`_)


MTM1M3TS
~~~~~~~~

- Add FCU heater target temperature to the M1M3TS applySetpoint command. (`DM-49538 <https://rubinobs.atlassian.net/browse/DM-49538>`_)


MTMount
~~~~~~~

- Adds capacitor bank telemetry. (`DM-49468 <https://rubinobs.atlassian.net/browse/DM-49468>`_)


MTRotator
~~~~~~~~~

- Add the new error code to the MTRotator ErrorCode enum. (`DM-48161 <https://rubinobs.atlassian.net/browse/DM-48161>`_)


Scheduler
~~~~~~~~~

- Adds blockId to the Scheduler observation event. (`DM-39506 <https://rubinobs.atlassian.net/browse/DM-39506>`_)
- Adds expected physical rotator angle to the Scheduler target event. (`DM-39506 <https://rubinobs.atlassian.net/browse/DM-39506>`_)


v23.0.0 (2025-02-13)
====================
Package Level
-------------

New Features
~~~~~~~~~~~~

- CSC for the Multi Beam Optical Seeing Sensor (MOSS) (`DM-46263 <https://rubinobs.atlassian.net/browse/DM-46263>`_)
- * add hardpointBalanceForcesOnInActiveState to ForceActuatorSettings (`DM-47803 <https://rubinobs.atlassian.net/browse/DM-47803>`_)
- Add C++ runtime asset flags for MTM1M3TS and MTVMS (`DM-47996 <https://rubinobs.atlassian.net/browse/DM-47996>`_)
- Updated TopicInfo to no longer raise an exception when data arrays lenght are different from the defined in the xml. This will now issue a warning but will no longer fail. (`DM-48149 <https://rubinobs.atlassian.net/browse/DM-48149>`_)


Bug Fixes
~~~~~~~~~

- Fix the container username in Jenkinfile. (`DM-47806 <https://rubinobs.atlassian.net/browse/DM-47806>`_)


Other Changes and Additions
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Remove DM-43821 from test_TopicDescription.py as the MTMount was fixed. (`DM-46026 <https://rubinobs.atlassian.net/browse/DM-46026>`_)
- Switched to astropy-base instead of astropy in conda recipe. (`DM-47999 <https://rubinobs.atlassian.net/browse/DM-47999>`_)
- Updated pyproject to add astropy and lxml as dependencies and allow package to be fully installed with pip. (`DM-48681 <https://rubinobs.atlassian.net/browse/DM-48681>`_)
- Add Java to the list of runtime languages for MTMount. (`DM-48681 <https://rubinobs.atlassian.net/browse/DM-48681>`_)


Interface Changes
-----------------

Bug Fixes
~~~~~~~~~

- Make Description and EFDB_Topic mandatory for Command/Event/TelemetryType in schema (`DM-43829 <https://rubinobs.atlassian.net/browse/DM-43829>`_)


ATAOS
~~~~~

- Add temperature attribute to ATAOS_command_applyCorrection and to CorrectionStarted and CorrectionCompleted ATAOS_logevents. (`DM-46190 <https://rubinobs.atlassian.net/browse/DM-46190>`_)


ATBuilding
~~~~~~~~~~

- Added maximumDriveFrequency event and driveVoltage telemetry for ATBuilding. (`DM-47930 <https://rubinobs.atlassian.net/browse/DM-47930>`_)


ATCamera
~~~~~~~~

- Implement generic command (`CAP-1062 <https://rubinobs.atlassian.net/browse/CAP-1062>`_)
- Updates for CCS changes. (`CAP-1065 <https://rubinobs.atlassian.net/browse/CAP-1065>`_)
- Fix missing descriptions. (`DM-43793 <https://rubinobs.atlassian.net/browse/DM-43793>`_)


ATPneumatics
~~~~~~~~~~~~

- Add command descriptions. (`DM-43798 <https://rubinobs.atlassian.net/browse/DM-43798>`_)


CCCamera
~~~~~~~~

- Implement generic command (`CAP-1062 <https://rubinobs.atlassian.net/browse/CAP-1062>`_)
- Fix filter changer descriptions and states (`CAP-1064 <https://rubinobs.atlassian.net/browse/CAP-1064>`_)
- Updates for CCS changes. (`CAP-1065 <https://rubinobs.atlassian.net/browse/CAP-1065>`_)
- Fix missing descriptions. (`DM-43804 <https://rubinobs.atlassian.net/browse/DM-43804>`_)


DIMM
~~~~

- Applied modifications for DIMM to bring the interface in line with DIMM as actually implemented. (`DM-48784 <https://rubinobs.atlassian.net/browse/DM-48784>`_)
- Remove some of the commands and events from DM-48784 and postpone them for later consideration. (`DM-48917 <https://rubinobs.atlassian.net/browse/DM-48917>`_)


EPM
~~~

- Merge EPM enums and telemetry into ESS. (`DM-46348 <https://rubinobs.atlassian.net/browse/DM-46348>`_)


ESS
~~~

- Add Raritan PDU telemetry. (`DM-46041 <https://rubinobs.atlassian.net/browse/DM-46041>`_)
- Add aircraft tracking data to the ESS. (`DM-46087 <https://rubinobs.atlassian.net/browse/DM-46087>`_)
- Merge EPM enums and telemetry into ESS. (`DM-46348 <https://rubinobs.atlassian.net/browse/DM-46348>`_)


HVAC
~~~~

- Add OperatingMode and UnitState enums.
  Translate all topics, items and descriptions to proper English. (`DM-46739 <https://rubinobs.atlassian.net/browse/DM-46739>`_)
- Add Chiller04 and Dynalene telemetry.
  Add and remove enums. (`DM-48157 <https://rubinobs.atlassian.net/browse/DM-48157>`_)
- Add glycol sensor telemetry. (`DM-48157 <https://rubinobs.atlassian.net/browse/DM-48157>`_)


MTAOS
~~~~~

- Remove `annularZernikeCoeff` event from MTAOS xml. (`DM-48750 <https://rubinobs.atlassian.net/browse/DM-48750>`_)


MTCamera
~~~~~~~~

- Implement generic command (`CAP-1062 <https://rubinobs.atlassian.net/browse/CAP-1062>`_)
- Fix filter changer descriptions and states and update the telemetry and events (`CAP-1064 <https://rubinobs.atlassian.net/browse/CAP-1064>`_)
- Updates for CCS changes. (`CAP-1065 <https://rubinobs.atlassian.net/browse/CAP-1065>`_)
- Add MTCamera_logevent_rebCond (`CAP-1066 <https://rubinobs.atlassian.net/browse/CAP-1066>`_)
- Fix missing descriptions. (`DM-43816 <https://rubinobs.atlassian.net/browse/DM-43816>`_)


MTM1M3
~~~~~~

- Rective misleading comment in MTM1M3 DetailedState documentation. (`DM-46022 <https://rubinobs.atlassian.net/browse/DM-46022>`_)
- Gyroscope velocities are reported in deg/sec. (`DM-47616 <https://rubinobs.atlassian.net/browse/DM-47616>`_)


MTMount
~~~~~~~

- Add new interface to lock/unlock motion. (`DM-48681 <https://rubinobs.atlassian.net/browse/DM-48681>`_)


MTRotator
~~~~~~~~~

- Remove the deprecated states in ControllerState and EnabledSubstate in MTRotator.py. (`DM-45603 <https://rubinobs.atlassian.net/browse/DM-45603>`_)
- Update the ErrorCode enum in MTRotator.py. (`DM-47994 <https://rubinobs.atlassian.net/browse/DM-47994>`_)
- Add new interface to lock/unlock motion. (`DM-48681 <https://rubinobs.atlassian.net/browse/DM-48681>`_)


Scheduler
~~~~~~~~~

- Add failureStrategy parameter to the addBlock command and blockStatus event.
  This parameter allows users to specify how the Scheduler should handle script failures when executing a block. (`DM-48100 <https://rubinobs.atlassian.net/browse/DM-48100>`_)


TunableLaser
~~~~~~~~~~~~

- Adding in Optical Configuration enum for TunableLaser (`DM-46165 <https://rubinobs.atlassian.net/browse/DM-46165>`_)


v22.1.0 (2024-08-23)
====================
Package Level
-------------

New Features
~~~~~~~~~~~~

- The XML Conda package build will now use the XmlPipeline.groovy script. (`DM-45496 <https://rubinobs.atlassian.net/browse/DM-45496>`_)


Interface Changes
-----------------

ATBuilding
~~~~~~~~~~

- Make ATBuilding a configurable CSC. (`DM-45395 <https://rubinobs.atlassian.net/browse/DM-45395>`_)


ATCamera
~~~~~~~~

- Remove obsolete ATCamera_logevent_shutterMotionProfile (`CAP-1050 <https://rubinobs.atlassian.net/browse/CAP-1050>`_)
- Make initGuiders roiSpec length 1 (unlimited) (`CAP-1051 <https://rubinobs.atlassian.net/browse/CAP-1051>`_)
- Update ATCamera xml for XML 22.1 (`CAP-1056 <https://rubinobs.atlassian.net/browse/CAP-1056>`_)


ATMonochromator
~~~~~~~~~~~~~~~

- Updated grating enumeration for ATMonochromator (`DM-45475 <https://rubinobs.atlassian.net/browse/DM-45475>`_)


CCCamera
~~~~~~~~

- Make initGuiders roiSpec length 1 (unlimited) (`CAP-1051 <https://rubinobs.atlassian.net/browse/CAP-1051>`_)
- Update CCCamera xml for XML 22.1 (`CAP-1056 <https://rubinobs.atlassian.net/browse/CAP-1056>`_)


Electrometer
~~~~~~~~~~~~

- Add Voltage and Resistance to UnitToRead enum. (`DM-45177 <https://rubinobs.atlassian.net/browse/DM-45177>`_)


LEDProjector
~~~~~~~~~~~~

- Swapped the ON/OFF enumeration for the LEDProjector. They are currently switched (`DM-45766 <https://rubinobs.atlassian.net/browse/DM-45766>`_)


LinearStage
~~~~~~~~~~~

- Included axis in the move commands (`DM-45754 <https://rubinobs.atlassian.net/browse/DM-45754>`_)


MTAOS
~~~~~

- Add support for sparse zernike coefficients to MTAOS_command_addAberration, MTAOS_logevent_wavefrontError and MTAOS_logevent_rejectedWavefrontError. (`DM-45883 <https://rubinobs.atlassian.net/browse/DM-45883>`_)
- Add pubEvent to publish calculated mirror stresses from MTAOS. (`DM-45890 <https://rubinobs.atlassian.net/browse/DM-45890>`_)


MTCamera
~~~~~~~~

- Make initGuiders roiSpec length 1 (unlimited) (`CAP-1051 <https://rubinobs.atlassian.net/browse/CAP-1051>`_)
- Update MTCamera xml for XML 22.1 (`CAP-1056 <https://rubinobs.atlassian.net/browse/CAP-1056>`_)


MTHexapod
~~~~~~~~~

- Remove the MTHexapod_logevent_controllerState.offlineSubstate and add the MTHexapod_logevent_configuration.drivesEnabled.
  Remove the OfflineSubstate enum in MTHexapod and MTRotator. (`DM-45566 <https://rubinobs.atlassian.net/browse/DM-45566>`_)


MTM1M3
~~~~~~

- Changed and corrected M1M3's FCUTable. (`DM-45598 <https://rubinobs.atlassian.net/browse/DM-45598>`_)


MTM2
~~~~

- Add the MTM2_command_enableLutTemperature. (`DM-45202 <https://rubinobs.atlassian.net/browse/DM-45202>`_)


MTMount
~~~~~~~

- Update MTMount openMirrorCovers command to allow specifying a single leaf to open. (`DM-45874 <https://rubinobs.atlassian.net/browse/DM-45874>`_)
- Update telemetry with the lastest version provided by Tekniker. (`DM-45874 <https://rubinobs.atlassian.net/browse/DM-45874>`_)


MTRotator
~~~~~~~~~

- Add the MTRotator_logevent_lowFrequencyVibration. (`DM-45758 <https://rubinobs.atlassian.net/browse/DM-45758>`_)


Scheduler
~~~~~~~~~

- Add civil, nautical and astronomical twilight information to the generalInfo event. (`DM-45499 <https://rubinobs.atlassian.net/browse/DM-45499>`_)
- Add additional metadata to the target event. (`DM-45499 <https://rubinobs.atlassian.net/browse/DM-45499>`_)
- Add support for execution id. (`DM-45686 <https://rubinobs.atlassian.net/browse/DM-45686>`_)


Script
~~~~~~

- Add support for execution id. (`DM-45686 <https://rubinobs.atlassian.net/browse/DM-45686>`_)


ScriptQueue
~~~~~~~~~~~

- Add support for execution id. (`DM-45686 <https://rubinobs.atlassian.net/browse/DM-45686>`_)


v22.0.0 (2024-07-11)
====================
Package Level
-------------

New Features
~~~~~~~~~~~~

- Updated definition of AvailableFilters logevent (`AvailableFilters <https://rubinobs.atlassian.net/browse/AvailableFilters>`_)
- Add lint GitHub workflow. (`DM-44918 <https://rubinobs.atlassian.net/browse/DM-44918>`_)
- Add enumaration consistency test. (`DM-45170 <https://rubinobs.atlassian.net/browse/DM-45170>`_)


Bug Fixes
~~~~~~~~~

- Make sure that the doc build GitHub workflow only runs once for PR pushes. (`DM-44980 <https://rubinobs.atlassian.net/browse/DM-44980>`_)


ATCamera
~~~~~~~~

- Update ATCamera xml for XML 22 (`CAP-1047 <https://rubinobs.atlassian.net/browse/CAP-1047>`_)


CCCamera
~~~~~~~~

- Update CCCamera xml for XML 22 (`CAP-1047 <https://rubinobs.atlassian.net/browse/CAP-1047>`_)


MTCamera
~~~~~~~~

- Update MTCamera xml for XML 22 (`CAP-1047 <https://rubinobs.atlassian.net/browse/CAP-1047>`_)


Interface Changes
-----------------

EAS
~~~

- Add topics descriptions. (`DM-43809 <https://rubinobs.atlassian.net/browse/DM-43809>`_)


EPM
~~~

- Improve PDU and XUPS telemetry. (`DM-44577 <https://rubinobs.atlassian.net/browse/DM-44577>`_)


Electrometer
~~~~~~~~~~~~

- Add optional groupID to startScan and startScanDt. (`DM-44757 <https://rubinobs.atlassian.net/browse/DM-44757>`_)


FiberSpectrograph
~~~~~~~~~~~~~~~~~

- Add optional groupID to the expose command. (`DM-44757 <https://rubinobs.atlassian.net/browse/DM-44757>`_)


LinearStage
~~~~~~~~~~~

- Add ErrorCode enum. (`DM-45062 <https://rubinobs.atlassian.net/browse/DM-45062>`_)


MTAirCompressor
~~~~~~~~~~~~~~~

- Add URL for MTAirCompressor configuration (`DM-47000.rst <https://rubinobs.atlassian.net/browse/DM-47000.rst>`_)


MTDome
~~~~~~

- Add event for the capacitor banks state. (`DM-44289 <https://rubinobs.atlassian.net/browse/DM-44289>`_)


MTEEC
~~~~~

- Add topics descriptions. (`DM-43817 <https://rubinobs.atlassian.net/browse/DM-43817>`_)


MTReflector
~~~~~~~~~~~

- Adding MTReflector xml which allows opening and closing the flatfield reflector (`DM-43456 <https://rubinobs.atlassian.net/browse/DM-43456>`_)


TunableLaser
~~~~~~~~~~~~

- Fix black formatting. (`DM-44918 <https://rubinobs.atlassian.net/browse/DM-44918>`_)


21.0.0 (2024-05-24)
===================
Package Level
-------------

New Features
~~~~~~~~~~~~

- Add topic description test. (`DM-43452 <https://rubinobs.atlassian.net/browse/DM-43452>`_)
- Add duplicate topic name test. (`DM-43452 <https://rubinobs.atlassian.net/browse/DM-43452>`_)
- Adding ability for ledprojector to adjust DAC values of labjack (`dm-43459 <https://rubinobs.atlassian.net/browse/dm-43459>`_)


Bug Fixes
~~~~~~~~~

- Fix the github action for building the documentation. (`DM-43452 <https://rubinobs.atlassian.net/browse/DM-43452>`_)


Documentation
~~~~~~~~~~~~~

- Add guide dependency group to documenteer dependency. (`DM-43861 <https://rubinobs.atlassian.net/browse/DM-43861>`_)


Other Changes and Additions
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Format code with black. (`DM-43452 <https://rubinobs.atlassian.net/browse/DM-43452>`_)
- Fix the Jira URL in pyproject.toml (`DM-43452 <https://rubinobs.atlassian.net/browse/DM-43452>`_)
- Fix mypy typing issue. (`DM-43452 <https://rubinobs.atlassian.net/browse/DM-43452>`_)
- Remove myst_nb and sphinx-rediraffe from ci.yaml and make package install one line by installing both groups. (`DM-43861 <https://rubinobs.atlassian.net/browse/DM-43861>`_)
- Add dependabot checks on GitHub actions. (`DM-44359 <https://rubinobs.atlassian.net/browse/DM-44359>`_)
- Ignore dependabot branches for news fragments. (`DM-44359 <https://rubinobs.atlassian.net/browse/DM-44359>`_)
- Fixed GitHub Actions configuration. (`DM-44359 <https://rubinobs.atlassian.net/browse/DM-44359>`_)
- Fixed GitHub Actions configuration, again. (`DM-44359_2 <https://rubinobs.atlassian.net/browse/DM-44359_2>`_)


MTAirCompressor
~~~~~~~~~~~~~~~

- Added missing description entries to XML. (`DM-43815 <https://rubinobs.atlassian.net/browse/DM-43815>`_)


MTM1M3
~~~~~~

- Add missing Description XML entries. (`DM-43819 <https://rubinobs.atlassian.net/browse/DM-43819>`_)


Interface Changes
-----------------

ATAOS
~~~~~

- Add topics descriptions. (`DM-43789 <https://rubinobs.atlassian.net/browse/DM-43789>`_)


ATBuilding
~~~~~~~~~~

- Add missing descriptions to event and telemetry topics. (`DM-43792 <https://rubinobs.atlassian.net/browse/DM-43792>`_)


ATHexapod
~~~~~~~~~

- Add missing descriptions to event, telemetry & command topics. (`DM-43794 <https://rubinobs.atlassian.net/browse/DM-43794>`_)


ATMonochromator
~~~~~~~~~~~~~~~

- Add topics description. (`DM-43795 <https://rubinobs.atlassian.net/browse/DM-43795>`_)


ATOODS
~~~~~~

- Add required description to ATOODS event (`DM-43797 <https://rubinobs.atlassian.net/browse/DM-43797>`_)


ATSpectrograph
~~~~~~~~~~~~~~

- Add topics description and remove unnecessary topic attributes to empty topics. (`DM-43803 <https://rubinobs.atlassian.net/browse/DM-43803>`_)


Authorize
~~~~~~~~~

- Remove Authorize CSC. (`DM-44340 <https://rubinobs.atlassian.net/browse/DM-44340>`_)
- Remove AuthList references from unit tests, documentation and SALGenerics and SALSubsystems.xml. (`DM-44359 <https://rubinobs.atlassian.net/browse/DM-44359>`_)


CBP
~~~

- Add missing descriptions to telemetry topics. (`DM-43806 <https://rubinobs.atlassian.net/browse/DM-43806>`_)


CCOODS
~~~~~~

- Add required description to CCOODS event (`DM-43805 <https://rubinobs.atlassian.net/browse/DM-43805>`_)


DIMM
~~~~

- Add required descriptions to DIMM topics. (`DM-43807 <https://rubinobs.atlassian.net/browse/DM-43807>`_)


DSM
~~~

- Add required descriptions to DSM topics. (`DM-43808 <https://rubinobs.atlassian.net/browse/DM-43808>`_)


EPM
~~~

- Add EPM CSC. (`DM-44117 <https://rubinobs.atlassian.net/browse/DM-44117>`_)


Electrometer
~~~~~~~~~~~~

- Add missing descriptions to event topics. (`DM-43811 <https://rubinobs.atlassian.net/browse/DM-43811>`_)


GIS
~~~

- Add missing descriptions to event topics. (`DM-43812 <https://rubinobs.atlassian.net/browse/DM-43812>`_)


GenericCamera
~~~~~~~~~~~~~

- Add required descriptions to GenericCamera topics. (`DM-43810 <https://rubinobs.atlassian.net/browse/DM-43810>`_)


HVAC
~~~~

- Add glycol sensor telemetry. (`DM-43775 <https://rubinobs.atlassian.net/browse/DM-43775>`_)
- Add more glycol sensor telemetry. (`DM-44356 <https://rubinobs.atlassian.net/browse/DM-44356>`_)


LaserTracker
~~~~~~~~~~~~

- Add required descriptions to LaserTracker topics. (`DM-43813 <https://rubinobs.atlassian.net/browse/DM-43813>`_)


LinearStage
~~~~~~~~~~~

- Add missing descriptions for command, event & telemetry topics. (`DM-43814 <https://rubinobs.atlassian.net/browse/DM-43814>`_)
- Remove LinearStage from description check test. (`DM-43814-1 <https://rubinobs.atlassian.net/browse/DM-43814-1>`_)


MTDome
~~~~~~

- Add setPowerManagementMode command and event and PowerManagementMode enum. (`DM-43676 <https://rubinobs.atlassian.net/browse/DM-43676>`_)
- Add missing descriptions to all topics. (`DM-43676 <https://rubinobs.atlassian.net/browse/DM-43676>`_)


MTHexapod
~~~~~~~~~

- Add the missing description of MTHexapod, and remove the MTHexapod-Telemetry from check_for_issues(). (`DM-43823 <https://rubinobs.atlassian.net/browse/DM-43823>`_)


MTM1M3TS
~~~~~~~~

- Add missing Description entries. (`DM-43820 <https://rubinobs.atlassian.net/browse/DM-43820>`_)


MTM2
~~~~

- Add the MTM2_logevent_disabledILC event. (`DM-42566 <https://rubinobs.atlassian.net/browse/DM-42566>`_)


MTMount
~~~~~~~

- Add required descriptions to MTMount topics. (`DM-43821 <https://rubinobs.atlassian.net/browse/DM-43821>`_)


MTOODS
~~~~~~

- Add required description to MTOODS event (`DM-43822 <https://rubinobs.atlassian.net/browse/DM-43822>`_)
- Remove MTOODS from descriptions check test. (`DM-43822-1 <https://rubinobs.atlassian.net/browse/DM-43822-1>`_)


MTRotator
~~~~~~~~~

- Add the missing description of MTRotator, and remove the MTRotator-Telemetry from check_for_issues(). (`DM-43823 <https://rubinobs.atlassian.net/browse/DM-43823>`_)


OCPS
~~~~

- Add descriptions for the two OCPS events. (`DM-43824 <https://rubinobs.atlassian.net/browse/DM-43824>`_)


PMD
~~~

- Add missing descriptions to event and telemetry topics. (`DM-43825 <https://rubinobs.atlassian.net/browse/DM-43825>`_)


SummitFacility
~~~~~~~~~~~~~~

- Add missing descriptions to telemetry topics. (`DM-43826 <https://rubinobs.atlassian.net/browse/DM-43826>`_)


TunableLaser
~~~~~~~~~~~~

- Add missing descriptions to command and event topics. (`DM-43827 <https://rubinobs.atlassian.net/browse/DM-43827>`_)
- Changed state names for TunableLaser (`DM-44083 <https://rubinobs.atlassian.net/browse/DM-44083>`_)


Watcher
~~~~~~~

- Add command to create a narrative log entry for one or more alarms. (`DM-44066 <https://rubinobs.atlassian.net/browse/DM-44066>`_)


WeatherForecast
~~~~~~~~~~~~~~~

- Add missing descriptions to telemetry topics. (`DM-43828 <https://rubinobs.atlassian.net/browse/DM-43828>`_)


v20.3.0 (2024-03-22)
====================
Package Level
-------------

New Features
~~~~~~~~~~~~

- Fix many missing units/descriptions
  Add mpm subsystem for MTCamera
  Update MTCamera telemetry/events for filter changer subsystem
  Update MTCamera telemetry/events for shutter subsystem
  Update MTCamera telemetry/events for refrig/chiller subsystems (`CAP-1029 <https://rubinobs.atlassian.net/browse/CAP-1029>`_)
- Add support for towncrier to manage release notes. (`DM-42658 <https://rubinobs.atlassian.net/browse/DM-42658>`_)
- Remove support for null values for float and double.
  After investigating the issue, we realized that AVRO supports setting the values to NaN (as well as +/-Infinity), which covers the conditions we were trying to support with the null values. (`DM-42789 <https://rubinobs.atlassian.net/browse/DM-42789>`_)
- Update the version of the ts-conda-build dependency to 0.4. (`DM-43331 <https://rubinobs.atlassian.net/browse/DM-43331>`_)
- Adding 2 events and 1 telemetry for the Interlock Monitor to capture when the fan turns on/off, interlock turns on/off, and the rolling average of all probes on the temperature scanner. (`dm-42237 <https://rubinobs.atlassian.net/browse/dm-42237>`_)


Documentation
~~~~~~~~~~~~~

- Adds a reference to the XML Unit Standards policy to README.md. (`DM-43089 <https://rubinobs.atlassian.net/browse/DM-43089>`_)


Interface Changes
-----------------

ATBuilding
~~~~~~~~~~

- Add interfaces for upcoming auxtel vent gate and fan automation. (`DM-43428 <https://rubinobs.atlassian.net/browse/DM-43428>`_)


CCCamera
~~~~~~~~

- Add new telemetry for the refrigeration pathfinder (considered part of ComCam) (`CAP-1026 <https://rubinobs.atlassian.net/browse/CAP-1026>`_)


ESS
~~~

- Add telemetry for the Q330 earthquake monitor. (`DM-43018 <https://rubinobs.atlassian.net/browse/DM-43018>`_)


Electrometer
~~~~~~~~~~~~

- Add logicTimerStart and logicTimerEnd events. (`DM-42856 <https://rubinobs.atlassian.net/browse/DM-42856>`_)


GIS
~~~

- Fix gnetAuxFree item count in auxCpuInputs. (`DM-43260 <https://rubinobs.atlassian.net/browse/DM-43260>`_)


GenericCamera
~~~~~~~~~~~~~

- Add new event ``endOfStreaming`` to denote that camera has stopped streaming but image file(s) not constructed yet.

  Add ``imageName`` attribute to ``logevent_streamingModeStarted`` and ``logevent_streamingModeStopped``. (`DM-43360 <https://rubinobs.atlassian.net/browse/DM-43360>`_)


MTCamera
~~~~~~~~

- Add support for filter changer low power mode (`CAP-1024 <https://rubinobs.atlassian.net/browse/CAP-1024>`_)
- Add support for filter changer degraded mode (`CAP-1025 <https://rubinobs.atlassian.net/browse/CAP-1025>`_)
- Fix issues related to MTCamera thermal patterns for rtd and trim heaters (`CAP-1030 <https://rubinobs.atlassian.net/browse/CAP-1030>`_)


MTDome
~~~~~~

- Add new and correct existing MotionState enum values. (`DM-42686 <https://rubinobs.atlassian.net/browse/DM-42686>`_)


MTMount
~~~~~~~

- Update MTMount interface with latest telemetry from Tekniker.
  Add new commands to reset and load new settings, as well as commands to park and unpark the telescope.
  Add new enumeration with park positions. (`DM-43192 <https://rubinobs.atlassian.net/browse/DM-43192>`_)
- Fix MTMount telemetry interface. (`DM-43192 <https://rubinobs.atlassian.net/browse/DM-43192>`_)


MTRotator
~~~~~~~~~

- Add configureJerk command. (`DM-43265 <https://rubinobs.atlassian.net/browse/DM-43265>`_)


Scheduler
~~~~~~~~~

- Update SalIndex Scheduler enumeration to include the "OCS" instance of the scheduler, with index=3. (`DM-42183 <https://rubinobs.atlassian.net/browse/DM-42183>`_)


ScriptQueue
~~~~~~~~~~~

- Update SalIndex ScriptQueue enumeration to include the "OCS" instance with index=3. (`DM-42183 <https://rubinobs.atlassian.net/browse/DM-42183>`_)


TunableLaser
~~~~~~~~~~~~

- Added new command ``setOpticalConfiguration`` to change the optical alignment configuration.
  Added new log event ``opticalConfiguration`` which reflects the set optical alignment configuration. (`DM-41678 <https://rubinobs.atlassian.net/browse/DM-41678>`_)
- Fix duplicate temperature topic by renaming one to scannerTemperature. (`DM-43446 <https://rubinobs.atlassian.net/browse/DM-43446>`_)
- Add missing descriptions to all TunableLaser telemetry topics. (`DM-43446 <https://rubinobs.atlassian.net/browse/DM-43446>`_)


? (2024-03-21)
==============
Package Level
-------------

New Features
~~~~~~~~~~~~

- Fix many missing units/descriptions
  Add mpm subsystem for MTCamera
  Update MTCamera telemetry/events for filter changer subsystem
  Update MTCamera telemetry/events for shutter subsystem
  Update MTCamera telemetry/events for refrig/chiller subsystems (`CAP-1029 <https://rubinobs.atlassian.net/browse/CAP-1029>`_)
- Add support for towncrier to manage release notes. (`DM-42658 <https://rubinobs.atlassian.net/browse/DM-42658>`_)
- Remove support for null values for float and double.
  After investigating the issue, we realized that AVRO supports setting the values to NaN (as well as +/-Infinity), which covers the conditions we were trying to support with the null values. (`DM-42789 <https://rubinobs.atlassian.net/browse/DM-42789>`_)
- Update the version of the ts-conda-build dependency to 0.4. (`DM-43331 <https://rubinobs.atlassian.net/browse/DM-43331>`_)
- Adding 2 events and 1 telemetry for the Interlock Monitor to capture when the fan turns on/off, interlock turns on/off, and the rolling average of all probes on the temperature scanner. (`dm-42237 <https://rubinobs.atlassian.net/browse/dm-42237>`_)


Interface Changes
-----------------

ATBuilding
~~~~~~~~~~

- Add interfaces for upcoming auxtel vent gate and fan automation. (`DM-43428 <https://rubinobs.atlassian.net/browse/DM-43428>`_)


CCCamera
~~~~~~~~

- Add new telemetry for the refrigeration pathfinder (considered part of ComCam) (`CAP-1026 <https://rubinobs.atlassian.net/browse/CAP-1026>`_)


ESS
~~~

- Add telemetry for the Q330 earthquake monitor. (`DM-43018 <https://rubinobs.atlassian.net/browse/DM-43018>`_)


Electrometer
~~~~~~~~~~~~

- Add logicTimerStart and logicTimerEnd events. (`DM-42856 <https://rubinobs.atlassian.net/browse/DM-42856>`_)


GIS
~~~

- Fix gnetAuxFree item count in auxCpuInputs. (`DM-43260 <https://rubinobs.atlassian.net/browse/DM-43260>`_)


GenericCamera
~~~~~~~~~~~~~

- Add new event ``endOfStreaming`` to denote that camera has stopped streaming but image file(s) not constructed yet.

  Add ``imageName`` attribute to ``logevent_streamingModeStarted`` and ``logevent_streamingModeStopped``. (`DM-43360 <https://rubinobs.atlassian.net/browse/DM-43360>`_)


MTCamera
~~~~~~~~

- Add support for filter changer low power mode (`CAP-1024 <https://rubinobs.atlassian.net/browse/CAP-1024>`_)
- Add support for filter changer degraded mode (`CAP-1025 <https://rubinobs.atlassian.net/browse/CAP-1025>`_)
- Fix issues related to MTCamera thermal patterns for rtd and trim heaters (`CAP-1030 <https://rubinobs.atlassian.net/browse/CAP-1030>`_)


MTDome
~~~~~~

- Add new and correct existing MotionState enum values. (`DM-42686 <https://rubinobs.atlassian.net/browse/DM-42686>`_)


MTMount
~~~~~~~

- Update MTMount interface with latest telemetry from Tekniker.
  Add new commands to reset and load new settings, as well as commands to park and unpark the telescope.
  Add new enumeration with park positions. (`DM-43192 <https://rubinobs.atlassian.net/browse/DM-43192>`_)


MTRotator
~~~~~~~~~

- Add configureJerk command. (`DM-43265 <https://rubinobs.atlassian.net/browse/DM-43265>`_)


Scheduler
~~~~~~~~~

- Update SalIndex Scheduler enumeration to include the "OCS" instance of the scheduler, with index=3. (`DM-42183 <https://rubinobs.atlassian.net/browse/DM-42183>`_)


ScriptQueue
~~~~~~~~~~~

- Update SalIndex ScriptQueue enumeration to include the "OCS" instance with index=3. (`DM-42183 <https://rubinobs.atlassian.net/browse/DM-42183>`_)


TunableLaser
~~~~~~~~~~~~

- Added new command ``setOpticalConfiguration`` to change the optical alignment configuration.

  Added new log event ``opticalConfiguration`` which reflects the set optical alignment configuration. (`DM-41678 <https://rubinobs.atlassian.net/browse/DM-41678>`_)


v20.2.0
-------

* Added qudrant property to M1M3 FATable.

* Fix documentation build.

* Interface updates:

  * MTDome

    * Add fans and inflate commands, calibration screen status telemetry and thermal control statuses.
    * Fix SubSystemId enum values.

  * MTM2

    * Improve the description of ``MTM2_forceErrorTangent`` topic.

  * CBP

    * Added command for mask rotation.

  * MTRotator

    * Add the new commands: ``MTRotator_command_configureEmergencyAcceleration`` and ``MTRotator_command_configureEmergencyJerk``.

  * ScriptQueue

    * Improve support for executing blocks of scripts.

    * Update ``nextVisit`` event to add ``startTime``.

      This attribute will contain the estimated start time for the script.

  * Script

    * Improve support for publishing block id.

  * ATCamera/CCCamera/MTCamera

    * Update to https://github.com/lsst-camera-ccs/org-lsst-ccs-camera-sal-xml version 1.0.3
    * Release notes: https://jira.slac.stanford.edu/issues/?jql=project%20%3D%20LCOBM%20AND%20fixVersion%20%3D%20XML-1.0.3

  * TunableLaser

    * Adding 3 commands to TunableLaser: ``changeTempCtrlSetpoint``, ``turnOnTempCtrl``, and ``turnOffTempCtrl``.
    * Adding 3 events to TunableLaser: ``setPointChanged``, ``tempCtrlOn``, and ``tempCtrlOff``.

v20.1.0
-------

* Added GPLv3 license file.

* Added .gitattributes and .gitarchive to support getting version information from setuptools_scm for a git tarball.

* Updated the contents of the README.

* In ``get_component_info.py``:

  * Copy the component xml files alongside the avro schema files and also generate the generics xml file.
  * Write a file with the list of revcodes.
  * Update path to where avro schema is written to add the component name to the path.

* In ``tests/test_component_info.py``, small patch to support running the tests now that float/double can also be "null".

* In ``field_info.py``:

  * Add support for floating point values to be set as ``None``.
  * Fix SAL to AVRO type conversion for SAL-long type.
    According to AVRO documentation SAL-long is actually AVRO-int.

* Fix style violation in ``enums/LEDProjector.py``.

* Use Astropy infrastructure to formally add new units. Enabled Imperial units to support use of the gallon unit.

* Interface updates:

  * ATMCS

    * Fix typo in the ``ATMCS_nasmyth_m3_mountMotorEncoders`` telemetry topic name.

  * MTRotator

    * Add FaultSubstate enumeration (updated).
    * Add the new item ``copleyFaultStatus`` in ``MTRotator_electrical`` topic.
    * Rename the item ``offlineSubstate`` to ``faultSubstate`` in ``MTRotator_logevent_controllerState`` topic.
    * Add the new item ``drivesEnabled`` to ``MTRotator_logevent_configuration`` topic.

  * MTHexapod

    * Fix and improve the description in ``MTHexapod_actuators`` topic.
    * Add the new item ``copleyFaultStatus`` and improve the description in ``MTHexapod_electrical`` topic.

  * MTM2

    * Reuse the enum **BumpTest** in MTM1M3.
    * Add the topics: ``MTM2_logevent_actuatorBumpTestStatus``, ``MTM2_command_killActuatorBumpTest``, and ``MTM2_command_setHardpointList``.

  * ATCamera/CCCamera/MTCamera
    * Full refresh of camera Events/Telemetry XML based on currently installed CCS subsystems
    * XML now based derived from https://github.com/lsst-camera-ccs/org-lsst-ccs-camera-sal-xml
    * Current release: https://github.com/lsst-camera-ccs/org-lsst-ccs-camera-sal-xml/releases/tag/org-lsst-ccs-camera-sal-xml-parent-1.0.1
    * Reviewing changes for individual CCS subsystem is possible by comparing to previous XML release., e.g. https://github.com/lsst-camera-ccs/org-lsst-ccs-camera-sal-xml/compare/refactor_XML_20...org-lsst-ccs-camera-sal-xml-parent-1.0.1#diff

v20.0.0
-------

* Update the package ``__init__.py`` file to properly export the package version.
* Copy enumerations for ts-idl into a new enums submodule.
* Allow components to still define SummaryState enumerations in their xml files while generic enumerations are not supported by C/C++ SAL.
* Move the code that defines SAL topics structure and generate avro-schema files from the kafka version of salobj.
  * Add private_revCode back to the generic fields.
  * Add support for computing rev_code.
* Make ATMCS and ATPneumatics configurable in preparation for switching to Python CSCs.
* Update enumerations to match the definitions from the enums submodule (see interface updates).
* Remove SALPY from the list of valid runtime language.
* Remove support for octet and char types.
* Remove "kafka" from the topic namespace.
* Add missing private fields to ``BaseMsgType``.
* Add version field to documentation conf.py.
* Removed support for the ``unsigned long`` and ``unsigned long long`` data types.

* Interface updates:

  * Generics

    * Add SummaryState enumeration.

  * ATBuilding

    * Remove unused detailedState event and enumeration.

  * ATHexapod

    * Remove unnecessary summaryState enumeration.

  * ATMonochromator

    * Remove unnecessary summaryState enumeration.
    * Add ErrorCode enumeration.

  * ATSpectrograph

    * Add DisperserPosition and FilterPosition enumerations.

  * EAS

    * Remove unused detailedState event and enumeration.

  * Electrometer

    * Remove unnecessary summaryState enumeration.

  * ESS

    * Add "Item" to telemetry item names to avoid clashes with topic names.

  * HVAC

    * Move DeviceIndex, DEVICE_GROUPS and DEVICE_GROUP_IDS to ts_hvac.
    * Add alarm and status events for all systems but Dynalene.

  * LaserTracker

    * Add AlignComponent enumeration.

  * LEDProjector

    * Add LEDBasicState enumeration.
    * Add turnAllLEDsOn, turnAllLEDsOff, turnOnLED, turnOffLED.
    * Add LEDProjector_logevent_ledState event.

  * MTAirCompressor

    * Remove unnecessary summaryState enumeration.

  * MTDome

    * Set aperture shutter positionCommanded to two values.
    * Add rear access door status telemetry and enum.

  * MTHexapod

    * Add ErrorCode enumeration.

  * MTM1M3

    * Commands to pause and resume mirror raising or lowering
    * Add ILCState enumeration.
    * Settings fields for raising M1M3 at low elevation
    * Improved slew control and reporting - SlewControllerState, name for PID settings
    * Added various M1M3 support and thermal systems constants - lsst.ts.xml.tables

  * MTRotator

    * Add ErrorCode enumeration.

  * TunableLaser

    * Replace detailedState enumeration with LaserDetailedState.
    * Add new LaserErrorCode enumeration.

  * ATCamera/CCCamera/MTCamera

    * Add DAQ monitoring statistics (CAP-703)
    * Fix for image_handling configuration (CAP-1006)
    * Update focal-plane configuration and telemetry (CAP-1011)
    * Update MTCamera for new cold/chiller/hex systems (CAP-1008)
    * Bug fixes (CAP-1013)

  * MTM2

    * Use the ``string`` data type to replace the ``unsigned long`` and ``unsigned long long`` data types.

  * Test

    * Removed ``unsigned long`` and ``unsigned long long`` attributes from all topics.

v19.0.0
-------
* Remove the unrecognized pytest flags in **pyproject.toml**.
* Add documentation to README for adding, renaming or deleting a CSC from the interface.
* Interface updates:

  * GIS:

    * Add gisCPUInputs, gisCpuOutputs, gisCpuReserve, afeDecentralizedIOInputs, afeDecentralizedIOOutputs, afeDecentralizedIOFree, laserDecentralizedIOInput, laserDecentralizedIOOutputs, laserDecentralizedIOFree, m2cDecentralizedIOInputs, m2cDecentralizedIOOutput, m2cDecentralizedIOFree, pfDecentralizedIoInputs, pfDecentralizedIoOutput, pfDecentralizedIoFree, auxCpuInputs, auxCpuOutputs, domeCpuInputs, domeCpuOutputs, m1m3CpuInputs, m1m3CpuOutputs, tmaCpuInputs, tmaCpuOutputs, causes, causes2, causesOverride, causes2Override, effects, effects2 events.

  * HVAC:

    * Add Dynalene commands and related events.

  * MTOODC:

    * Add CSC
    * Add CSC to testutils.py and to SALSubsystems.xml

  * MTM2:

    * Update the MTM2 interface to have the similar functionality as EUI.

  * DIMM:

    * Update timestamp and expiresAt types in dimmMeasurement event to double.

  * MTAOS:

    * Add ``MTAOS_command_offsetDOF`` to allow users to apply offsets to the degrees of freedom.
    * Add ``MTAOS_command_resetOffsetDOF`` to allow users to reset offsets.
    * Update ``MTAOS_logevent_degreeOfFreedom`` to include user offsets.
    * Add telemetry files for MTAOS to publish measured bending modes for M1M3 and M2.

  * LaserTracker:

    * Fixing units of offsetsPublish and positionPublish events.

v18.0.0
-------
* Removed the IOTA CSC.
* Interface updates:

  * M1M3:

    * set/clear slewFlag commands, forceControllerState event
    * useAccelerometers added to ForceActuatorSettings.

  * HVAC:

    * Add more Dynalene events and telemetry.

v17.1.0
-------
* Updated names after personnel departures.
* Interface updates:

  * M1M3:

    * useGyroscope added to ForceActuatorSettings.
    * add EnableDisableForceComponent command

  * ESS:

    * Add requirement of CPP runtime language.
    * Fix the units of accelerometerPSD.accelerationPSDX/Y/Z: /Hz instead of /Hz^2.
    * Also document that the minimum frequency is always 0 for this topic.

  * MTMount: add telemetryClientHeartbeat telemetry topic.
  * MTRotator:

    * Add a few new fields to the config event.
    * Rewrite the config event field descriptions.
    * Refine a few other event and command descriptions as well.

v17.0.1
-------
* ESS: Add requirement of CPP runtime language.

v17.0.0
-------
* Removed WeatherStation CSC.
* Interface updates:

  * MTMount: add 3 cabinet temperature fields to oilSupplySystem telemetry.
  * HVAC: split dynaleneSafeties bitmask event into individual events.
  * MTM1M3

    * MTM1M3_command_setAirSlewFlag replaced with MTM1M3_command_boosterValveClose and MTM1M3_command_boosterValveOpen
    * added MTM1M3_logevent_boosterValveSettings, MTM1M3_logevent_boosterValveStatus events
    * MTM1M3_logevent_forceActuatorState.slewFlag moved to MTM1M3_logevent_boosterValveStatus
    * MTM1M3_logevent_[primary|secondary]AxisMeasuredForceWarning renamed to in-mirror MTM1M3_measured[X|Y|Z]ForceWarning
    * MTM1M3_logevent_forceActuatorSettings ammended with measured and applied force warning settings

v16.0.0
-------
* Removed CatchupArchiver, ATArchiver and MTArchiver CSCs.
* ci.yaml: modernize to Python v3.11 for building the documentation.
* Implemented pre-commit.
* Interfaces updates.

  * LaserTracker

    * added LaserTracker_logevent_t2saStatus and LaserTracker_logevent_laserStatus topcis.

  * ATMonochromator

    * updated <Descriptions>, <Units> and <Enumeration> fields for the ATMonochromator_command_calibrateWavelength and ATMonochromator_command_updateMonochromatorSetup topics.

  * Script

    * added instrument field to Script_logevent_metadata.

  * ScriptQueue

    * added instrument field to ScriptQueue_logevent_nextVisit.

  * HVAC

    * added Dynalene Event and Telemetry topics.
    * updated <Units> field to Pa from bar.

  * ATWhiteLight

    * updated LampBasicState and LampControllerState enums in the Events interface.
    * added lightDetected field to ATWhiteLight_logevent_lampConnected.

  * GenericCamera

    * added fields to the GenericCamera_logevent_cameraInfo topic.
    * added Command and Event topics.

  * ATPtg

    * added ATPtg_logevent_observatoryLocation.
    * added CoordFrame_azel,CoordFrame_planet,CoordFrame_ephem enums for ATPtg Events.

  * MTPtg

    * MTPtg_logevent_observatoryLocation topics.

  * Watcher

    * add Watcher_logevent_notification.

  * MTDome

    * added MotionState enum to the Events interface.

  * ESS

    * fixed <IDL_Type> for several fields in the ESS_rainRate, ESS_snowRate, ESS_airFlow. ESS_lightningStrikeStatus and ESS_logevent_lightningStrike topics.
    * added ESS_spectrumAnalyzer topic.
    * added Java to the <RuntimeLanguages> field.
    * removed fields from ESS_accelerometerPSD topic.

  * ATDomeTrajectory/MTDomeTrajectory

    * added telescopeVignetted Events and enums.

  * MTMount

    * fixed spelling of the minL1LimitEnabled, maxL1LimitEnabled, minL2LimitEnabled and maxL2LimitEnabled fiels in the MTMount_logevent_cameraCableWrapControllerSettings topic.
    * renamed several thermal control related topics.
    * removed actualAcceleration field from MTMount_cameraCableWrap.

  * MTM1M3

    * added MTM1M3_logevent_raisingLoweringInfo
    * redesign FA following error handling - MTM1M3_logevent_forceActuatorFollowingErrorCounter, MTM1M3_logevent_forceActuatorSettings
    * publish FA followinng errors in MTM1M3_forceActuatorData
    * moved MTM1M3_logevent_forceActuatorState.supportPercentage field to MTM1M3_logevent_raisingLoweringInfo
    * added fields to MTM1M3_logevent_hardpointActuatorWarning and MTM1M3_logevent_forceActuatorSettings topics.

  * MTM1M3TS

    * removed setReheaterGain and reset commands
    * removed reHeaterGains Event topics

  * WeatherForecast

    * updated <Configuration> value.

  * MTAirCompressor

    * removed loadedHours50Percent Event and compressorPowerConsumption Telemetry topics.
    * removed compressorPowerConsumption field from MTAirCompressor_analogData.

v15.0.0
-------
* Renamed MTAlignment to LaserTracker. Made LaserTracker indexed.
* test_Units.py: remove mmH2O from NONSTANDARD_UNITS.
* Added logevent_clockOffset as a generic topic
* Interfaces updates.

  * MTM1M3TS: removed power, pumpStart, pumpStop, pumpFrequency, pumpReset and added fanCoilsHeatersPower, coolantPumpPower, coolantPumpStart, coolantPumpStop, coolantPumpFrequency, coolantPumpReset commands.

  * MTRotator

    * added MTRotator_logevent_clockOffset topic.

  * MTVMS

    * renamed MTVMS_command_changeSampleRate to MTVMS_command_changeSamplePeriod and updated fields.
    * renamed MTVMS_logevent_acquisitionRate to MTVMS_logevent_acquisitionPeriod and updated fields.
    * renamed MTVMS_logevent_acquisitionPeriod to MTVMS_logevent_fpgaState and updated fields.
    * added MTVMS_miscellaneous Telemetry topic.

  * TunableLaser

    * add PropagatingBurstModeWaitingForTrigger and PropagatingBurstModeTriggered to DetailedState enum.
    * renamed TunableLaser_command_setBurstCount to TunableLaser_command_triggerBurst.

  * MTMount

    * changed <Units> to mm in the oilLevelFacilities5001 field of MTMount_oSS topic.
    * renamed MTMount_oSS Telemetry topic to MTMount_oilSupplySystem.
    * updated fields in the MTMount_logevent_cameraCableWrapControllerSettings topic.
    * updated <IDL_Type> for the encoderHeadReadReferenceAZ and encoderHeadReadReferenceEL fields of the MTMount_encoder Telemetry topic.
    * renamed oilSupplySystemState.oilPowerState to oilSupplySystemState.circulationPumpPowerState.
    * added MTMount_logevent_clockOffset topic.

v14.0.0
-------
* Add WeatherForecast CSC.
* Converted package to use pyproject.toml.
* XML schema update for the Commands, Events and Telemetry <ItemType> attributes.
* Added a skip test if Jira ticket exists to tests/test_CSC_XML_Valid.py.
* Added Jenkinsfile.conda to build a Conda package for ts_xml.
* Interfaces updates.

  * MTCamera
  * CCCamera/ATCamera
  * MTMount
  * Electrometer
  * ESS

v13.0.0
-------
* Added the Command and Event topics and updated the Telemetry topics for the DREAM CSC.
* XML cleanup for AT/CC/MT Camera files.
* Interface updates.

  * ESS
  * MTDome
  * Scheduler
  * TunableLaser
  * MTDome
  * ATWhiteLight
  * MTM1M3

    * added hardpointActuator to MTM1M3_command_testHardpoint
    * removed MTM1M3_command_applyAberrationForces
    * removed abberation related Event topics
    * changed most of the forces from Event to Telemetry topic

  * MTM1M3TS

    * added pumpStart, pumpStop, pumpFrequency and pumpReset commands
    * added flowMeter Telemetry topic
    * added flowMeterMPUStatus, glycolPumpStatus and glycolPumpMPUStatus Event topics

  * MTVMS

    * added timeSynchronization Event topic
    * modify some units

  * Watcher
  * DIMM
  * LOVE
  * MTAirCompressor
  * GenericCamera
  * MTHexapod
  * Script
  * Scheduler
  * OCPS

v12.0.0
-------
* Removed the AdamSensors CSC.
* test_NoReservedWords.py: check for field name salIndex.
* test_Count.py: test for Count > 1 for strings
* Interface updates.

  * MTMount
  * DIMM
  * MTAOS
  * ATWhiteLight
  * MTDome
  * MTM1M3

    * renamed airPressureWarningHigh, airPressureWarningLow to \*Fault\* Event topics.

  * ScriptQueue
  * CCCamera/MTCamera
  * Scheduler

v11.1.1
-------
* **HOTFIX**.

  * Added command_setAuthList, command_setLogLevel and logevent_authList topics to the <AddedGenerics> field for LOVE.

v11.1.0
-------
* Set <Configuration> to the correct URL for for configurable CSCs.
* test_enumeration.py: allow negative enum values, but only for decimal values not hex values.
* Interface updates.

  * MTM1M3
  * MTDome
  * MTAirCompressor
  * ATWhiteLight

v11.0.1
-------
* **HOTFIX**.

  * Added the SALGeneric_logevent_statusCode topic.
  * Removed the SALGeneric_command_setValue topic.
  * Added the GenericCamera_command_setValue and the logevent_statusCode topics.

v11.0.0
-------
* Removed the PromptProcessing CSC.
* Added ATCamera_bonn_shutter_Device topic.
* Added MTAOS_command_interruptWEP topic.
* Removed SALPY from <RuntimeLanguages> for Script and Test CSCs.
* Updated SALGenerics.xml.

  * Added SALGeneric_logevent_configurationApplied and SALGeneric_logevent_configurationsAvailable topics.
  * Removed the settingsToApply field from the SALGeneric_command_start topic.
  * Removed the SALGeneric_logevent_settingVersions, SALGeneric_logevent_appliedSettingsMatchStart and SALGeneric_logevent_settingsApplied topics.

* Marked LinearState as configurable in the <AddedGenerics> field.
* Updated MTHexapod_logevent_connected and MTRotator_logevent_connected topics to have only the connected attribute.
* Updated documentation.

v10.2.0
-------
* Removed VERSION file, in favor of using git tags for version control.
* Removed command_enterControl from <AddedGenerics> field for MTHexapod and MTRotator.
* Marked TunableLaser, EAS and MTEEC as configurable in the <AddeGenerics> field.
* Added ESS_pressure Telemetry topic.
* Removed MTHexapod_command_clearError and MTRotator_command_clearError topcs.
* Updated attributes for the MTHexapod_logevent_controllerState MTHexapod_logevent_interlock topics.
* Added MTM1M3_logevent_positionControllerSettings and MTM1M3_command_panic topics.
* Added MotionState enums to MTDome Events.
* Updated <IDL_Type> field for the MTAOS_command_preProcess and MTAOS_command_runWEP topics.
* Removed archiverName field from ATOODS_logevent_imageInOODS and CCOODS_logevent_imageInOODS topics.

v10.1.0
-------
* Consolidated all ESS multi-channel temperature topics into one.
* Fixed <Configuration> field for MTHexapod and MTRotator.
* Updated <Count> fields for MTCamera Event and Telemetry topics.
* Added all <Generics> topics for the Authorize CSC.
* Added the MTMount_logevent_cameraCableWrapControllerSettings,MTMount_logevent_elevationControllerSettings, MTMount_logevent_azimuthControllerSettings and MTMount_logevent_controllerSettingsName topics.
* Removed the MTM1M3_command_programILC and MTM1M3_logevent_modbusResponse topcis.
* MTM1M3TS interface updates.

  * Added the MTM1M3TS_logevent_mixingValveSettings, MTM1M3TS_logevent_thermalSettings, MTM1M3TS_command_setMixingValve and MTM1M3TS_mixingValve topics.
  * Added rawValvePosition attribute to MTM1M3TS_mixingValve topic.
  * Removed unused ILCType enum from MTM1M3TS_Events.xml.

* Added the MTM2_logevent_controllerState topic.
* Marked WeatherStation as not having a simulator.

v10.0.0
-------
* Added the GCHeaderService and GIS CSCs.
* Added MTAlignment Command topics.
* Removed the DREAM_dataProduct topic.
* MTMount: overhaul Enums and Events.
* MTHexapod interface updates.

  * Added timestamp field to actuators Telemetry
  * Updated motorVoltage[6] to busVoltage[3] in the MTHexapod_electrical topic.
  * Removed initial* fields from the MTHexapod_logevent_configuration topic.


* Test: removed char and octet fields.
* ESS: added telemetry items for the Omega HX85A and HX85BA humidity sensors.
* MTM1M3 interface udpates.

  * Added commands and event to disable/enable FA.
  * Added Event topics.

    * MTM1M3_logevent_forceActuatorSettings.
    * MTM1M3_logevent_hardpointActuatorSettings.
    * MTM1M3_logevent_displacementSensorSettings.
    * MTM1M3_logevent_pidSettings.
    * MTM1M3_logevent_accelerometerSettings.
    * MTM1M3_logevent_gyroSettings.
    * MTM1M3_logevent_inclinometerSettings.

* MTMount interface updates.

  * Added Event topics.

    * MTMount_logevent_availableSettings.
    * MTMount_logevent_azimuthSystemState.
    * MTMount_logevent_elevationSystemState.
    * MTMount_logevent_cameraCableWrapSystemState.
    * MTMount_logevent_balanceSystemState.
    * MTMount_logevent_mirrorCoversSystemState.
    * MTMount_logevent_mirrorCoverLocksSystemState.
    * MTMount_logevent_azimuthCableWrapSystemState.
    * MTMount_logevent_lockingPinsSystemState.
    * MTMount_logevent_deployablePlatformsSystemState.
    * MTMount_logevent_oilSupplySystemState.
    * MTMount_logevent_azimuthDrivesThermalSystemState.
    * MTMount_logevent_elevationDrivesThermalSystemState.
    * MTMount_logevent_az0101CabinetThermalSystemState.
    * MTMount_logevent_modbusTemperatureControllersSystemState.
    * MTMount_logevent_mainCabinetSystemState.
    * MTMount_logevent_mainAxesPowerSupplySystemState.
    * MTMount_logevent_topEndChillerSystemState.

  * Renamed MTMount_logevent_deployablePlatformMotionState to MTMount_logevent_deployablePlatformsMotionState.
  * Removed MTMount_logevent_elevationLimitPositions topic.
  * Updated Enumerations.

* MTRotator: added torque and current fields to MTRotator_motors and odometer field to MTRotator_rotation topics.
* HVAC: added many new Command, Event and Telemetry attributes.
* ATPtg/MTPtg interface updates.

  * Removed several fields from ATPtg_mountStatus and MTPtg_mountStatus Telemetry topics.
  * Removed topics.

    * ATPtg_command_setAccessMode.
    * ATPtg_command_guideAutoclear.
    * ATPtg_logevent_mountGuideMode.
    * ATPtg_logevent_inPositionEl.
    * ATPtg_logevent_axesTrackMode.
    * ATPtg_logevent_accessMode.
    * ATPtg_logevent_inPosition.
    * ATPtg_logevent_inPositionRot.
    * ATPtg_logevent_inPositionAz.
    * MTPtg_command_setAccessMode.
    * MTPtg_command_guideAutoclear.
    * MTPtg_logevent_mountGuideMode.
    * MTPtg_logevent_inPositionEl.
    * MTPtg_logevent_axesTrackMode.
    * MTPtg_logevent_accessMode.
    * MTPtg_logevent_inPosition.
    * MTPtg_logevent_inPositionRot.
    * MTPtg_logevent_inPositionAz.

* Made OCPS an indexed CSC.
* GenericCamera: added GenericCamera_command_startAutoExposure and GenericCamera_logevent_autoExposureStarted topics.
* Added Enumeration references to the documentation.

Additional versions
-------------------
**See commit history in the `repoistory <https://github.com/lsst-ts/ts_xml/commits/main>`_ for older versions.**
