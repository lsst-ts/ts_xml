.. _Version_History:

===============
Version History
===============

v17.0.0
-------

* MTMount: add 3 cabinet temperature fields to oilSupplySystem telemetry

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

    * added Telemetry and Event topics.
    * removed supportPercentage field from MTM1M3_logevent_forceActuatorState.
    * added fields to MTM1M3_logevent_hardpointActuatorWarning and MTM1M3_logevent_forceActuatorSettings topics.

  * WeatherForecast

    * updated <Configuration> value.

  * MTAirCompressor

    * removed loadedHours50Percent Event and compressorPowerConsumption Telemetry topics.
    * removed compressorPowerConsumption field from MTAirCompressor_analogData.
    * removed loadedHours50Percent from MTAirCompressor_logevent_compressorInfo.

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
  * MTM1M3TS
  * MTM1M3
  * Watcher
  * DIMM
  * LOVE
  * MTAirCompressor
  * GenericCamera
  * MTHexapod
  * Script
  * Scheduler
  * OCPS
  * MTVMS

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
