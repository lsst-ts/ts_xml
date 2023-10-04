.. _Version_History:

===============
Version History
===============
v21.0.0
-------

* Interface updates:

  * LEDProjector

    * Add turnAllLEDsOn, turnAllLEDsOff, turnOnLED, turnOffLED.
    * Add LEDStates telemetry.
    * Add labjackConnect, labjackState, ledStates, and ledOnMinutes events.



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
