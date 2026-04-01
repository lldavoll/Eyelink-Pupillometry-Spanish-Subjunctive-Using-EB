# -*- coding: utf-8 -*-
"""
Custom Experiment Builder class for sending live pupil-size updates to the
EyeLink Host PC during a trial.

This script is written to remain compatible with the Python environment used by
SR Research Experiment Builder. It:

- stores trial-level state
- polls the newest EyeLink sample at a controlled interval
- extracts pupil size from the available eye
- sends a status message to the Host PC with the current trial number and pupil size
"""

import sreb
import sreb.time
import pylink


class PupilToHost(sreb.EBObject):
    """
    Custom Experiment Builder object for periodically sending pupil-size updates
    to the EyeLink Host PC.
    """

    def __init__(self):
        sreb.EBObject.__init__(self)

        # Interval (ms) between pupil-size updates sent to the Host PC.
        self.updateDuration = 500

        # Whether pupil updates are currently enabled.
        self.checkingStatus = 0

        # Trial-level state.
        self.startTime = 0
        self.lastUpdateTime = 0
        self.updatePupil = 0
        self.trialNum = 0
        self.pupilSize = 0

    def getCheckingStatus(self):
        """Return whether pupil updates are currently enabled."""
        return self.checkingStatus

    def setCheckingStatus(self, status):
        """Enable or disable pupil updates."""
        self.checkingStatus = status

    def resetTrial(self, trialNum):
        """
        Reset trial-level timing and state before a new trial begins.
        """
        self.startTime = 0
        self.lastUpdateTime = 0
        self.updatePupil = 0
        self.checkingStatus = 0
        self.trialNum = trialNum

    def sendPupilTohost(self):
        """
        Poll the newest EyeLink sample and send the current pupil size to the
        Host PC at the configured update interval.
        """
        if self.checkingStatus != 1:
            return

        currentTime = sreb.time.getCurrentTime()

        if self.startTime == 0:
            self.startTime = currentTime
            self.lastUpdateTime = currentTime
            self.updatePupil = 1
        elif currentTime - self.lastUpdateTime >= self.updateDuration:
            self.lastUpdateTime = currentTime
            self.updatePupil = 1

        if self.updatePupil != 1:
            return

        sample = pylink.getEYELINK().getNewestSample()
        if not sample:
            return

        eyeData = sample.getRightEye()
        if eyeData is None:
            eyeData = sample.getLeftEye()

        if eyeData is None:
            return

        self.pupilSize = int(eyeData.getPupilSize())

        pylink.getEYELINK().sendCommand(
            "record_status_message 'Trial = {0}   Pupil Size = {1}'".format(
                self.trialNum, self.pupilSize
            )
        )

        self.updatePupil = 0


# Backward-compatible alias in case the Experiment Builder project still
# references the original template class name.
CustomClassTemplate = PupilToHost
