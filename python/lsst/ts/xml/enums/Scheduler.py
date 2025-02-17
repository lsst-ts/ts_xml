# This file is part of ts_xml.
#
# Developed for Vera Rubin Observatory.
# This product includes software developed by the LSST Project
# (https://www.lsst.org).
# See the COPYRIGHT file at the top-level directory of this distribution
# for details of code ownership.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License

__all__ = [
    "SalIndex",
    "DetailedState",
    "FailureStrategy",
]

import enum


class SalIndex(enum.IntEnum):
    """Allowed SAL indices."""

    MAIN_TEL = 1
    AUX_TEL = 2
    OCS = 3


class DetailedState(enum.IntEnum):
    """Detailed state enumeration for the Scheduler."""

    # Scheduler is idle. This will be the detailed state when the Scheduler is
    # not in ENABLED state or is in enabled but not running.
    IDLE = enum.auto()
    # Scheduler is running but not doing anything in particular.
    RUNNING = enum.auto()
    # Scheduler is running and waiting for the "next_target_timer_task" to
    # finish. This condition happens when there is no target to observe, the
    # scheduler estimates how long until there is a target to observe and
    # create a timer to wait for.
    WAITING_NEXT_TARGET_TIMER_TASK = enum.auto()
    # Scheduler is generating the target queue. This consists of processing the
    # telemetry data to produce the targets to observe.
    GENERATING_TARGET_QUEUE = enum.auto()
    # Scheduler is computing the predicted queue.
    COMPUTING_PREDICTED_SCHEDULE = enum.auto()
    # Scheduler is queueing targets.
    QUEUEING_TARGET = enum.auto()


class FailureStrategy(enum.IntEnum):
    """Strategy to employ when there is a script failure
    while executing block.
    """

    # No error recoverable.
    # This is the current behavior and causes the Scheduler to remove all
    # scripts from the queue and mark the execution as failed.
    NONE = enum.auto()
    # Will preserve the scripts currently queue and continue to queue them
    # if the queue makes progress. If a script is stopped the scheduler will
    # cleanup the remaining scripts, stop the block execution and mark it as
    # failed.
    ON_SCRIPT_FAILURE = enum.auto()
    # This will basically instruct the scheduler to ignore any type of error
    # or interruption. It will continue to put scripts in the queue until all
    # scripts from a block finished.
    KEEP_GOING = enum.auto()
