__all__ = ["Subsystem"]

import enum


class Subsystem(enum.Enum):
    GISCPUINPUTS = enum.auto
    GISCPUOUTPUTS = enum.auto
    GISCPURESERVE = enum.auto
    ACCESSFIREEARTHQUAKEINPUTS = enum.auto
    ACCESSFIREEARTHQUAKEOUTPUTS = enum.auto
    ACCESSFIREEARTHQUAKEFREE = enum.auto
    LASERINPUTS = enum.auto
    LASEROUTPUTS = enum.auto
    LASERFREE = enum.auto
    M2INPUTS = enum.auto
    M2OUTPUTS = enum.auto
    M2FREE = enum.auto
    PFLOWINPUTS = enum.auto
    PFLOWOUTPUTS = enum.auto
    PFLOWFREE = enum.auto
    AUXCPUINPUTS = enum.auto
    AUXCPUOUTPUTS = enum.auto
    DOMEINPUTS = enum.auto
    DOMEOUTPUTS = enum.auto
    M1M3CPUINPUTS = enum.auto
    M1M3CPUOUTPUTS = enum.auto
    TMACPUINPUTS = enum.auto
    TMACPUOUTPUTS = enum.auto
    SAFETYCAUSESONE = enum.auto
    SAFETYCAUSESTWO = enum.auto
    SAFETYCAUSESONEOVERRIDE = enum.auto
    SAFETYCAUSESTWOOVERRIDE = enum.auto
    SAFETYEFFECTSONE = enum.auto
    SAFETYEFFECTSTWO = enum.auto
