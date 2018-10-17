#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.2),
    on Wed Sep 19 12:11:12 2018
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division

import psychopy
psychopy.useVersion('1.85.2')

from psychopy import locale_setup, sound, gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'Inhibition_Task'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'/Users/benjaminseitz/Desktop/Inhibition_Task/inhibition_task_new.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1440, 900), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='cm')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "Start_Experiment"
Start_ExperimentClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text=u'Press the Space Bar to Begin the Experiment ',
    font=u'Arial',
    pos=(0, 0.25), height=1.3, wrapWidth=None, ori=0, 
    color=u'White', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Trialstart"
TrialstartClock = core.Clock()

mouseA = event.Mouse(win=win)
x, y = [None, None]
startingkey1on = visual.ShapeStim(
    win=win, name='startingkey1on',
    vertices=[[-(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [+(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [0,(2, 2)[1]/2.0]],
    ori=0, pos=(0, -3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
startingkey1off = visual.ShapeStim(
    win=win, name='startingkey1off',
    vertices=[[-(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [+(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [0,(2, 2)[1]/2.0]],
    ori=0, pos=(0, -3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=-3.0, interpolate=True)
startingkey2on = visual.ShapeStim(
    win=win, name='startingkey2on',
    vertices=[[-(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [+(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [0,(2, 2)[1]/2.0]],
    ori=0, pos=(0, -3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
startingkey2off = visual.ShapeStim(
    win=win, name='startingkey2off',
    vertices=[[-(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [+(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [0,(2, 2)[1]/2.0]],
    ori=0, pos=(0, -3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=-5.0, interpolate=True)
startingkey3on = visual.ShapeStim(
    win=win, name='startingkey3on',
    vertices=[[-(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [+(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [0,(2, 2)[1]/2.0]],
    ori=0, pos=(0, -3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
startingkey3off = visual.ShapeStim(
    win=win, name='startingkey3off',
    vertices=[[-(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [+(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [0,(2, 2)[1]/2.0]],
    ori=0, pos=(0, -3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=-7.0, interpolate=True)
startingkey4on = visual.ShapeStim(
    win=win, name='startingkey4on',
    vertices=[[-(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [+(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [0,(2, 2)[1]/2.0]],
    ori=0, pos=(0, -3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-8.0, interpolate=True)
startingkey4off = visual.ShapeStim(
    win=win, name='startingkey4off',
    vertices=[[-(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [+(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [0,(2, 2)[1]/2.0]],
    ori=0, pos=(0, -3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=-9.0, interpolate=True)
startingkey5on = visual.ShapeStim(
    win=win, name='startingkey5on',
    vertices=[[-(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [+(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [0,(2, 2)[1]/2.0]],
    ori=0, pos=(0, -3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-10.0, interpolate=True)
startingkey5off = visual.ShapeStim(
    win=win, name='startingkey5off',
    vertices=[[-(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [+(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [0,(2, 2)[1]/2.0]],
    ori=0, pos=(0, -3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=-11.0, interpolate=True)
startingkey6on = visual.ShapeStim(
    win=win, name='startingkey6on',
    vertices=[[-(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [+(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [0,(2, 2)[1]/2.0]],
    ori=0, pos=(0, -3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-12.0, interpolate=True)
startingkey6off = visual.ShapeStim(
    win=win, name='startingkey6off',
    vertices=[[-(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [+(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [0,(2, 2)[1]/2.0]],
    ori=0, pos=(0, -3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=-13.0, interpolate=True)
startingkey7on = visual.ShapeStim(
    win=win, name='startingkey7on',
    vertices=[[-(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [+(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [0,(2, 2)[1]/2.0]],
    ori=0, pos=(0, -3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-14.0, interpolate=True)
startingkey7off = visual.ShapeStim(
    win=win, name='startingkey7off',
    vertices=[[-(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [+(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [0,(2, 2)[1]/2.0]],
    ori=0, pos=(0, -3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=-15.0, interpolate=True)
startingkey8on = visual.ShapeStim(
    win=win, name='startingkey8on',
    vertices=[[-(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [+(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [0,(2, 2)[1]/2.0]],
    ori=0, pos=(0, -3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-16.0, interpolate=True)
startingkey8off = visual.ShapeStim(
    win=win, name='startingkey8off',
    vertices=[[-(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [+(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [0,(2, 2)[1]/2.0]],
    ori=0, pos=(0, -3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=-17.0, interpolate=True)
startingkey9on = visual.ShapeStim(
    win=win, name='startingkey9on',
    vertices=[[-(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [+(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [0,(2, 2)[1]/2.0]],
    ori=0, pos=(0, -3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-18.0, interpolate=True)
startingkey9off = visual.ShapeStim(
    win=win, name='startingkey9off',
    vertices=[[-(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [+(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [0,(2, 2)[1]/2.0]],
    ori=0, pos=(0, -3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=-19.0, interpolate=True)
startingkey10on = visual.ShapeStim(
    win=win, name='startingkey10on',
    vertices=[[-(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [+(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [0,(2, 2)[1]/2.0]],
    ori=0, pos=(0, -3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-20.0, interpolate=True)
startingkey10off = visual.ShapeStim(
    win=win, name='startingkey10off',
    vertices=[[-(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [+(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [0,(2, 2)[1]/2.0]],
    ori=0, pos=(0, -3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=-21.0, interpolate=True)
startingkey11on = visual.ShapeStim(
    win=win, name='startingkey11on',
    vertices=[[-(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [+(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [0,(2, 2)[1]/2.0]],
    ori=0, pos=(0, -3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-22.0, interpolate=True)
startingkey11off = visual.ShapeStim(
    win=win, name='startingkey11off',
    vertices=[[-(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [+(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [0,(2, 2)[1]/2.0]],
    ori=0, pos=(0, -3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=-23.0, interpolate=True)
startingkey12on = visual.ShapeStim(
    win=win, name='startingkey12on',
    vertices=[[-(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [+(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [0,(2, 2)[1]/2.0]],
    ori=0, pos=(0, -3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-24.0, interpolate=True)
startingkey12off = visual.ShapeStim(
    win=win, name='startingkey12off',
    vertices=[[-(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [+(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [0,(2, 2)[1]/2.0]],
    ori=0, pos=(0, -3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=-25.0, interpolate=True)
startingkey13on = visual.ShapeStim(
    win=win, name='startingkey13on',
    vertices=[[-(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [+(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [0,(2, 2)[1]/2.0]],
    ori=0, pos=(0, -3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-26.0, interpolate=True)
startingkey13off = visual.ShapeStim(
    win=win, name='startingkey13off',
    vertices=[[-(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [+(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [0,(2, 2)[1]/2.0]],
    ori=0, pos=(0, -3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=-27.0, interpolate=True)
startingkey14on = visual.ShapeStim(
    win=win, name='startingkey14on',
    vertices=[[-(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [+(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [0,(2, 2)[1]/2.0]],
    ori=0, pos=(0, -3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-28.0, interpolate=True)
startingkey14off = visual.ShapeStim(
    win=win, name='startingkey14off',
    vertices=[[-(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [+(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [0,(2, 2)[1]/2.0]],
    ori=0, pos=(0, -3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=-29.0, interpolate=True)
startingkey15on = visual.ShapeStim(
    win=win, name='startingkey15on',
    vertices=[[-(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [+(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [0,(2, 2)[1]/2.0]],
    ori=0, pos=(0, -3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-30.0, interpolate=True)
startingkey15off = visual.ShapeStim(
    win=win, name='startingkey15off',
    vertices=[[-(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [+(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [0,(2, 2)[1]/2.0]],
    ori=0, pos=(0, -3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=-31.0, interpolate=True)
startingkey16on = visual.ShapeStim(
    win=win, name='startingkey16on',
    vertices=[[-(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [+(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [0,(2, 2)[1]/2.0]],
    ori=0, pos=(0, -3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-32.0, interpolate=True)
startingkey16off = visual.ShapeStim(
    win=win, name='startingkey16off',
    vertices=[[-(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [+(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [0,(2, 2)[1]/2.0]],
    ori=0, pos=(0, -3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=-33.0, interpolate=True)
startingkey17on = visual.ShapeStim(
    win=win, name='startingkey17on',
    vertices=[[-(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [+(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [0,(2, 2)[1]/2.0]],
    ori=0, pos=(0, -3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-34.0, interpolate=True)
startingkey17off = visual.ShapeStim(
    win=win, name='startingkey17off',
    vertices=[[-(0.25, 0.25)[0]/2.0,-(0.25, 0.25)[1]/2.0], [+(0.25, 0.25)[0]/2.0,-(0.25, 0.25)[1]/2.0], [0,(0.25, 0.25)[1]/2.0]],
    ori=0, pos=(0, -3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=-35.0, interpolate=True)
startingkey18on = visual.ShapeStim(
    win=win, name='startingkey18on',
    vertices=[[-(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [+(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [0,(2, 2)[1]/2.0]],
    ori=0, pos=(0, -3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-36.0, interpolate=True)
startingkey18off = visual.ShapeStim(
    win=win, name='startingkey18off',
    vertices=[[-(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [+(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [0,(2, 2)[1]/2.0]],
    ori=0, pos=(0, -3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=-37.0, interpolate=True)
startingkey19on = visual.ShapeStim(
    win=win, name='startingkey19on',
    vertices=[[-(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [+(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [0,(2, 2)[1]/2.0]],
    ori=0, pos=(0, -3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-38.0, interpolate=True)
startingkey19off = visual.ShapeStim(
    win=win, name='startingkey19off',
    vertices=[[-(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [+(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [0,(2, 2)[1]/2.0]],
    ori=0, pos=(0, -3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=-39.0, interpolate=True)
startingkey20on = visual.ShapeStim(
    win=win, name='startingkey20on',
    vertices=[[-(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [+(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [0,(2, 2)[1]/2.0]],
    ori=0, pos=(0, -3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-40.0, interpolate=True)
startingkey20off = visual.ShapeStim(
    win=win, name='startingkey20off',
    vertices=[[-(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [+(2, 2)[0]/2.0,-(2, 2)[1]/2.0], [0,(2, 2)[1]/2.0]],
    ori=0, pos=(0, -3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=-41.0, interpolate=True)

# Initialize components for Routine "Nopeckblankscreen"
NopeckblankscreenClock = core.Clock()

blankscreen = visual.Rect(
    win=win, name='blankscreen',
    width=(50, 50)[0], height=(50, 50)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=-1.0, interpolate=True)

# Initialize components for Routine "Buffer"
BufferClock = core.Clock()
buffer = visual.Rect(
    win=win, name='buffer',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=0.0, interpolate=True)

# Initialize components for Routine "Go_No_Go"
Go_No_GoClock = core.Clock()


mouse2 = event.Mouse(win=win)
x, y = [None, None]
FoodKey_Area = visual.Rect(
    win=win, name='FoodKey_Area',
    width=(5.5, 5.5)[0], height=(5.5, 5.5)[1],
    ori=0, pos=(0, -9),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='red', fillColorSpace='rgb',
    opacity=0, depth=-3.0, interpolate=True)
FoodKey = visual.Rect(
    win=win, name='FoodKey',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0, pos=(0, -9),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
background = visual.Rect(
    win=win, name='background',
    width=(50, 50)[0], height=(50, 50)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=-5.0, interpolate=True)
ColorStimulus = visual.Polygon(
    win=win, name='ColorStimulus',
    edges=100, size=(5, 5),
    ori=0, pos=(0, .25),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)

# Initialize components for Routine "FoodReward"
FoodRewardClock = core.Clock()


FeederOpening = visual.TextStim(win=win, name='FeederOpening',
    text='Feeder Opening',
    font='Arial',
    pos=(0, 0), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
FeederClosing = visual.TextStim(win=win, name='FeederClosing',
    text='Feeder Closing\n',
    font='Arial',
    pos=(0, -3), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);

# Initialize components for Routine "AversiveMovie"
AversiveMovieClock = core.Clock()
import psychopy.visual
import moviepy


movie = visual.MovieStim3(
    win=win, name='movie',
    noAudio = False,
    filename='TV Static effect.mp4',
    ori=0, pos=(0, 0), opacity=1,
    size=(1400,1400),
    depth=-1.0,
    )

# Initialize components for Routine "ITI"
ITIClock = core.Clock()
iti = visual.Rect(
    win=win, name='iti',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=0.0, interpolate=True)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Start_Experiment"-------
t = 0
Start_ExperimentClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()
# keep track of which components have finished
Start_ExperimentComponents = [text_4, key_resp_2]
for thisComponent in Start_ExperimentComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Start_Experiment"-------
while continueRoutine:
    # get current time
    t = Start_ExperimentClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_4* updates
    if t >= 0.0 and text_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_4.tStart = t
        text_4.frameNStart = frameN  # exact frame index
        text_4.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Start_ExperimentComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Start_Experiment"-------
for thisComponent in Start_ExperimentComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Start_Experiment" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=5, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Workbook9.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    # set up handler to look after randomisation of conditions etc
    trials_2 = data.TrialHandler(nReps=100, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials_2')
    thisExp.addLoop(trials_2)  # add the loop to the experiment
    thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2.keys():
            exec(paramName + '= thisTrial_2.' + paramName)
    
    for thisTrial_2 in trials_2:
        currentLoop = trials_2
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if thisTrial_2 != None:
            for paramName in thisTrial_2.keys():
                exec(paramName + '= thisTrial_2.' + paramName)
        
        # ------Prepare to start Routine "Trialstart"-------
        t = 0
        TrialstartClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(20.000000)
        # update component parameters for each repeat
        skipblankscreen = False
        # setup some python lists for storing info about the mouseA
        mouseA.x = []
        mouseA.y = []
        mouseA.leftButton = []
        mouseA.midButton = []
        mouseA.rightButton = []
        mouseA.time = []
        # keep track of which components have finished
        TrialstartComponents = [mouseA, startingkey1on, startingkey1off, startingkey2on, startingkey2off, startingkey3on, startingkey3off, startingkey4on, startingkey4off, startingkey5on, startingkey5off, startingkey6on, startingkey6off, startingkey7on, startingkey7off, startingkey8on, startingkey8off, startingkey9on, startingkey9off, startingkey10on, startingkey10off, startingkey11on, startingkey11off, startingkey12on, startingkey12off, startingkey13on, startingkey13off, startingkey14on, startingkey14off, startingkey15on, startingkey15off, startingkey16on, startingkey16off, startingkey17on, startingkey17off, startingkey18on, startingkey18off, startingkey19on, startingkey19off, startingkey20on, startingkey20off]
        for thisComponent in TrialstartComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "Trialstart"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = TrialstartClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            if startingkey20off.status == STARTED and t >= frameRemains:
                continueRoutine = False
            
            if mouseA.isPressedIn(startingkey1on):
                skipblankscreen = True
                continueRoutine = False
            if mouseA.isPressedIn(startingkey1off):
                skipblankscreen = True
                continueRoutine = False
            if mouseA.isPressedIn(startingkey2on):
                skipblankscreen = True
                continueRoutine = False
            if mouseA.isPressedIn(startingkey2off):
                skipblankscreen = True
                continueRoutine = False
            if mouseA.isPressedIn(startingkey3on):
                skipblankscreen = True
                continueRoutine = False
            if mouseA.isPressedIn(startingkey3off):
                skipblankscreen = True
                continueRoutine = False
            if mouseA.isPressedIn(startingkey4on):
                skipblankscreen = True
                continueRoutine = False
            if mouseA.isPressedIn(startingkey4off):
                skipblankscreen = True
                continueRoutine = False
            if mouseA.isPressedIn(startingkey5on):
                skipblankscreen = True
                continueRoutine = False
            if mouseA.isPressedIn(startingkey5off):
                skipblankscreen = True
                continueRoutine = False
            if mouseA.isPressedIn(startingkey6on):
                skipblankscreen = True
                continueRoutine = False
            if mouseA.isPressedIn(startingkey6off):
                skipblankscreen = True
                continueRoutine = False
            if mouseA.isPressedIn(startingkey7on):
                skipblankscreen = True
                continueRoutine = False
            if mouseA.isPressedIn(startingkey7off):
                skipblankscreen = True
                continueRoutine = False
            if mouseA.isPressedIn(startingkey8on):
                skipblankscreen = True
                continueRoutine = False
            if mouseA.isPressedIn(startingkey8off):
                skipblankscreen = True
                continueRoutine = False
            if mouseA.isPressedIn(startingkey9on):
                skipblankscreen = True
                continueRoutine = False
            if mouseA.isPressedIn(startingkey9off):
                skipblankscreen = True
                continueRoutine = False
            if mouseA.isPressedIn(startingkey10on):
                skipblankscreen = True
                continueRoutine = False
            if mouseA.isPressedIn(startingkey10off):
                skipblankscreen = True
                continueRoutine = False
            if mouseA.isPressedIn(startingkey11on):
                skipblankscreen = True
                continueRoutine = False
            if mouseA.isPressedIn(startingkey11off):
                skipblankscreen = True
                continueRoutine = False
            if mouseA.isPressedIn(startingkey12on):
                skipblankscreen = True
                continueRoutine = False
            if mouseA.isPressedIn(startingkey12off):
                skipblankscreen = True
                continueRoutine = False
            if mouseA.isPressedIn(startingkey13on):
                skipblankscreen = True
                continueRoutine = False
            if mouseA.isPressedIn(startingkey13off):
                skipblankscreen = True
                continueRoutine = False
            if mouseA.isPressedIn(startingkey14on):
                skipblankscreen = True
                continueRoutine = False
            if mouseA.isPressedIn(startingkey14off):
                skipblankscreen = True
                continueRoutine = False
            if mouseA.isPressedIn(startingkey15on):
                skipblankscreen = True
                continueRoutine = False
            if mouseA.isPressedIn(startingkey15off):
                skipblankscreen = True
                continueRoutine = False
            if mouseA.isPressedIn(startingkey16on):
                skipblankscreen = True
                continueRoutine = False
            if mouseA.isPressedIn(startingkey16off):
                skipblankscreen = True
                continueRoutine = False
            if mouseA.isPressedIn(startingkey17on):
                skipblankscreen = True
                continueRoutine = False
            if mouseA.isPressedIn(startingkey17off):
                skipblankscreen = True
                continueRoutine = False
            if mouseA.isPressedIn(startingkey18on):
                skipblankscreen = True
                continueRoutine = False
            if mouseA.isPressedIn(startingkey18off):
                skipblankscreen = True
                continueRoutine = False
            if mouseA.isPressedIn(startingkey19on):
                skipblankscreen = True
                continueRoutine = False
            if mouseA.isPressedIn(startingkey19off):
                skipblankscreen = True
                continueRoutine = False
            if mouseA.isPressedIn(startingkey20on):
                skipblankscreen = True
                continueRoutine = False
            if mouseA.isPressedIn(startingkey20off):
                skipblankscreen = True
                continueRoutine = False
            # *mouseA* updates
            if t >= 0.0 and mouseA.status == NOT_STARTED:
                # keep track of start time/frame for later
                mouseA.tStart = t
                mouseA.frameNStart = frameN  # exact frame index
                mouseA.status = STARTED
                event.mouseButtons = [0, 0, 0]  # reset mouse buttons to be 'up'
            frameRemains = 0.0 + 20- win.monitorFramePeriod * 0.75  # most of one frame period left
            if mouseA.status == STARTED and t >= frameRemains:
                mouseA.status = STOPPED
            if mouseA.status == STARTED:  # only update if started and not stopped!
                buttons = mouseA.getPressed()
                if sum(buttons) > 0:  # ie if any button is pressed
                    x, y = mouseA.getPos()
                    mouseA.x.append(x)
                    mouseA.y.append(y)
                    mouseA.leftButton.append(buttons[0])
                    mouseA.midButton.append(buttons[1])
                    mouseA.rightButton.append(buttons[2])
                    mouseA.time.append(TrialstartClock.getTime())
            
            # *startingkey1on* updates
            if t >= 0.0 and startingkey1on.status == NOT_STARTED:
                # keep track of start time/frame for later
                startingkey1on.tStart = t
                startingkey1on.frameNStart = frameN  # exact frame index
                startingkey1on.setAutoDraw(True)
            frameRemains = 0.7 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if startingkey1on.status == STARTED and t >= frameRemains:
                startingkey1on.setAutoDraw(False)
            
            # *startingkey1off* updates
            if t >= 0.7 and startingkey1off.status == NOT_STARTED:
                # keep track of start time/frame for later
                startingkey1off.tStart = t
                startingkey1off.frameNStart = frameN  # exact frame index
                startingkey1off.setAutoDraw(True)
            frameRemains = 1.0 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if startingkey1off.status == STARTED and t >= frameRemains:
                startingkey1off.setAutoDraw(False)
            
            # *startingkey2on* updates
            if t >= 1.0 and startingkey2on.status == NOT_STARTED:
                # keep track of start time/frame for later
                startingkey2on.tStart = t
                startingkey2on.frameNStart = frameN  # exact frame index
                startingkey2on.setAutoDraw(True)
            frameRemains = 1.7 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if startingkey2on.status == STARTED and t >= frameRemains:
                startingkey2on.setAutoDraw(False)
            
            # *startingkey2off* updates
            if t >= 1.7 and startingkey2off.status == NOT_STARTED:
                # keep track of start time/frame for later
                startingkey2off.tStart = t
                startingkey2off.frameNStart = frameN  # exact frame index
                startingkey2off.setAutoDraw(True)
            frameRemains = 2.0 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if startingkey2off.status == STARTED and t >= frameRemains:
                startingkey2off.setAutoDraw(False)
            
            # *startingkey3on* updates
            if t >= 2 and startingkey3on.status == NOT_STARTED:
                # keep track of start time/frame for later
                startingkey3on.tStart = t
                startingkey3on.frameNStart = frameN  # exact frame index
                startingkey3on.setAutoDraw(True)
            frameRemains = 2.7 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if startingkey3on.status == STARTED and t >= frameRemains:
                startingkey3on.setAutoDraw(False)
            
            # *startingkey3off* updates
            if t >= 2.7 and startingkey3off.status == NOT_STARTED:
                # keep track of start time/frame for later
                startingkey3off.tStart = t
                startingkey3off.frameNStart = frameN  # exact frame index
                startingkey3off.setAutoDraw(True)
            frameRemains = 3 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if startingkey3off.status == STARTED and t >= frameRemains:
                startingkey3off.setAutoDraw(False)
            
            # *startingkey4on* updates
            if t >= 3.0 and startingkey4on.status == NOT_STARTED:
                # keep track of start time/frame for later
                startingkey4on.tStart = t
                startingkey4on.frameNStart = frameN  # exact frame index
                startingkey4on.setAutoDraw(True)
            frameRemains = 3.7 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if startingkey4on.status == STARTED and t >= frameRemains:
                startingkey4on.setAutoDraw(False)
            
            # *startingkey4off* updates
            if t >= 3.7 and startingkey4off.status == NOT_STARTED:
                # keep track of start time/frame for later
                startingkey4off.tStart = t
                startingkey4off.frameNStart = frameN  # exact frame index
                startingkey4off.setAutoDraw(True)
            frameRemains = 4.0 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if startingkey4off.status == STARTED and t >= frameRemains:
                startingkey4off.setAutoDraw(False)
            
            # *startingkey5on* updates
            if t >= 4.0 and startingkey5on.status == NOT_STARTED:
                # keep track of start time/frame for later
                startingkey5on.tStart = t
                startingkey5on.frameNStart = frameN  # exact frame index
                startingkey5on.setAutoDraw(True)
            frameRemains = 4.7 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if startingkey5on.status == STARTED and t >= frameRemains:
                startingkey5on.setAutoDraw(False)
            
            # *startingkey5off* updates
            if t >= 4.7 and startingkey5off.status == NOT_STARTED:
                # keep track of start time/frame for later
                startingkey5off.tStart = t
                startingkey5off.frameNStart = frameN  # exact frame index
                startingkey5off.setAutoDraw(True)
            frameRemains = 5.0 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if startingkey5off.status == STARTED and t >= frameRemains:
                startingkey5off.setAutoDraw(False)
            
            # *startingkey6on* updates
            if t >= 5 and startingkey6on.status == NOT_STARTED:
                # keep track of start time/frame for later
                startingkey6on.tStart = t
                startingkey6on.frameNStart = frameN  # exact frame index
                startingkey6on.setAutoDraw(True)
            frameRemains = 5 + .7- win.monitorFramePeriod * 0.75  # most of one frame period left
            if startingkey6on.status == STARTED and t >= frameRemains:
                startingkey6on.setAutoDraw(False)
            
            # *startingkey6off* updates
            if t >= 5.7 and startingkey6off.status == NOT_STARTED:
                # keep track of start time/frame for later
                startingkey6off.tStart = t
                startingkey6off.frameNStart = frameN  # exact frame index
                startingkey6off.setAutoDraw(True)
            frameRemains = 6 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if startingkey6off.status == STARTED and t >= frameRemains:
                startingkey6off.setAutoDraw(False)
            
            # *startingkey7on* updates
            if t >= 6 and startingkey7on.status == NOT_STARTED:
                # keep track of start time/frame for later
                startingkey7on.tStart = t
                startingkey7on.frameNStart = frameN  # exact frame index
                startingkey7on.setAutoDraw(True)
            frameRemains = 6 + .7- win.monitorFramePeriod * 0.75  # most of one frame period left
            if startingkey7on.status == STARTED and t >= frameRemains:
                startingkey7on.setAutoDraw(False)
            
            # *startingkey7off* updates
            if t >= 6.7 and startingkey7off.status == NOT_STARTED:
                # keep track of start time/frame for later
                startingkey7off.tStart = t
                startingkey7off.frameNStart = frameN  # exact frame index
                startingkey7off.setAutoDraw(True)
            frameRemains = 7 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if startingkey7off.status == STARTED and t >= frameRemains:
                startingkey7off.setAutoDraw(False)
            
            # *startingkey8on* updates
            if t >= 7 and startingkey8on.status == NOT_STARTED:
                # keep track of start time/frame for later
                startingkey8on.tStart = t
                startingkey8on.frameNStart = frameN  # exact frame index
                startingkey8on.setAutoDraw(True)
            frameRemains = 7 + .7- win.monitorFramePeriod * 0.75  # most of one frame period left
            if startingkey8on.status == STARTED and t >= frameRemains:
                startingkey8on.setAutoDraw(False)
            
            # *startingkey8off* updates
            if t >= 7.7 and startingkey8off.status == NOT_STARTED:
                # keep track of start time/frame for later
                startingkey8off.tStart = t
                startingkey8off.frameNStart = frameN  # exact frame index
                startingkey8off.setAutoDraw(True)
            frameRemains = 8 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if startingkey8off.status == STARTED and t >= frameRemains:
                startingkey8off.setAutoDraw(False)
            
            # *startingkey9on* updates
            if t >= 8 and startingkey9on.status == NOT_STARTED:
                # keep track of start time/frame for later
                startingkey9on.tStart = t
                startingkey9on.frameNStart = frameN  # exact frame index
                startingkey9on.setAutoDraw(True)
            frameRemains = 8 + .7- win.monitorFramePeriod * 0.75  # most of one frame period left
            if startingkey9on.status == STARTED and t >= frameRemains:
                startingkey9on.setAutoDraw(False)
            
            # *startingkey9off* updates
            if t >= 8.7 and startingkey9off.status == NOT_STARTED:
                # keep track of start time/frame for later
                startingkey9off.tStart = t
                startingkey9off.frameNStart = frameN  # exact frame index
                startingkey9off.setAutoDraw(True)
            frameRemains = 9 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if startingkey9off.status == STARTED and t >= frameRemains:
                startingkey9off.setAutoDraw(False)
            
            # *startingkey10on* updates
            if t >= 9 and startingkey10on.status == NOT_STARTED:
                # keep track of start time/frame for later
                startingkey10on.tStart = t
                startingkey10on.frameNStart = frameN  # exact frame index
                startingkey10on.setAutoDraw(True)
            frameRemains = 9 + .7- win.monitorFramePeriod * 0.75  # most of one frame period left
            if startingkey10on.status == STARTED and t >= frameRemains:
                startingkey10on.setAutoDraw(False)
            
            # *startingkey10off* updates
            if t >= 9.7 and startingkey10off.status == NOT_STARTED:
                # keep track of start time/frame for later
                startingkey10off.tStart = t
                startingkey10off.frameNStart = frameN  # exact frame index
                startingkey10off.setAutoDraw(True)
            frameRemains = 10 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if startingkey10off.status == STARTED and t >= frameRemains:
                startingkey10off.setAutoDraw(False)
            
            # *startingkey11on* updates
            if t >= 10 and startingkey11on.status == NOT_STARTED:
                # keep track of start time/frame for later
                startingkey11on.tStart = t
                startingkey11on.frameNStart = frameN  # exact frame index
                startingkey11on.setAutoDraw(True)
            frameRemains = 10 + .7- win.monitorFramePeriod * 0.75  # most of one frame period left
            if startingkey11on.status == STARTED and t >= frameRemains:
                startingkey11on.setAutoDraw(False)
            
            # *startingkey11off* updates
            if t >= 10.7 and startingkey11off.status == NOT_STARTED:
                # keep track of start time/frame for later
                startingkey11off.tStart = t
                startingkey11off.frameNStart = frameN  # exact frame index
                startingkey11off.setAutoDraw(True)
            frameRemains = 11 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if startingkey11off.status == STARTED and t >= frameRemains:
                startingkey11off.setAutoDraw(False)
            
            # *startingkey12on* updates
            if t >= 11 and startingkey12on.status == NOT_STARTED:
                # keep track of start time/frame for later
                startingkey12on.tStart = t
                startingkey12on.frameNStart = frameN  # exact frame index
                startingkey12on.setAutoDraw(True)
            frameRemains = 11 + .7- win.monitorFramePeriod * 0.75  # most of one frame period left
            if startingkey12on.status == STARTED and t >= frameRemains:
                startingkey12on.setAutoDraw(False)
            
            # *startingkey12off* updates
            if t >= 11.7 and startingkey12off.status == NOT_STARTED:
                # keep track of start time/frame for later
                startingkey12off.tStart = t
                startingkey12off.frameNStart = frameN  # exact frame index
                startingkey12off.setAutoDraw(True)
            frameRemains = 12 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if startingkey12off.status == STARTED and t >= frameRemains:
                startingkey12off.setAutoDraw(False)
            
            # *startingkey13on* updates
            if t >= 12 and startingkey13on.status == NOT_STARTED:
                # keep track of start time/frame for later
                startingkey13on.tStart = t
                startingkey13on.frameNStart = frameN  # exact frame index
                startingkey13on.setAutoDraw(True)
            frameRemains = 12 + .7- win.monitorFramePeriod * 0.75  # most of one frame period left
            if startingkey13on.status == STARTED and t >= frameRemains:
                startingkey13on.setAutoDraw(False)
            
            # *startingkey13off* updates
            if t >= 12.7 and startingkey13off.status == NOT_STARTED:
                # keep track of start time/frame for later
                startingkey13off.tStart = t
                startingkey13off.frameNStart = frameN  # exact frame index
                startingkey13off.setAutoDraw(True)
            frameRemains = 13.0 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if startingkey13off.status == STARTED and t >= frameRemains:
                startingkey13off.setAutoDraw(False)
            
            # *startingkey14on* updates
            if t >= 13 and startingkey14on.status == NOT_STARTED:
                # keep track of start time/frame for later
                startingkey14on.tStart = t
                startingkey14on.frameNStart = frameN  # exact frame index
                startingkey14on.setAutoDraw(True)
            frameRemains = 13 + .7- win.monitorFramePeriod * 0.75  # most of one frame period left
            if startingkey14on.status == STARTED and t >= frameRemains:
                startingkey14on.setAutoDraw(False)
            
            # *startingkey14off* updates
            if t >= 13.7 and startingkey14off.status == NOT_STARTED:
                # keep track of start time/frame for later
                startingkey14off.tStart = t
                startingkey14off.frameNStart = frameN  # exact frame index
                startingkey14off.setAutoDraw(True)
            frameRemains = 14 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if startingkey14off.status == STARTED and t >= frameRemains:
                startingkey14off.setAutoDraw(False)
            
            # *startingkey15on* updates
            if t >= 14 and startingkey15on.status == NOT_STARTED:
                # keep track of start time/frame for later
                startingkey15on.tStart = t
                startingkey15on.frameNStart = frameN  # exact frame index
                startingkey15on.setAutoDraw(True)
            frameRemains = 14 + .7- win.monitorFramePeriod * 0.75  # most of one frame period left
            if startingkey15on.status == STARTED and t >= frameRemains:
                startingkey15on.setAutoDraw(False)
            
            # *startingkey15off* updates
            if t >= 14.7 and startingkey15off.status == NOT_STARTED:
                # keep track of start time/frame for later
                startingkey15off.tStart = t
                startingkey15off.frameNStart = frameN  # exact frame index
                startingkey15off.setAutoDraw(True)
            frameRemains = 15.0 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if startingkey15off.status == STARTED and t >= frameRemains:
                startingkey15off.setAutoDraw(False)
            
            # *startingkey16on* updates
            if t >= 15 and startingkey16on.status == NOT_STARTED:
                # keep track of start time/frame for later
                startingkey16on.tStart = t
                startingkey16on.frameNStart = frameN  # exact frame index
                startingkey16on.setAutoDraw(True)
            frameRemains = 15 + .7- win.monitorFramePeriod * 0.75  # most of one frame period left
            if startingkey16on.status == STARTED and t >= frameRemains:
                startingkey16on.setAutoDraw(False)
            
            # *startingkey16off* updates
            if t >= 15.7 and startingkey16off.status == NOT_STARTED:
                # keep track of start time/frame for later
                startingkey16off.tStart = t
                startingkey16off.frameNStart = frameN  # exact frame index
                startingkey16off.setAutoDraw(True)
            frameRemains = 16.0 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if startingkey16off.status == STARTED and t >= frameRemains:
                startingkey16off.setAutoDraw(False)
            
            # *startingkey17on* updates
            if t >= 16 and startingkey17on.status == NOT_STARTED:
                # keep track of start time/frame for later
                startingkey17on.tStart = t
                startingkey17on.frameNStart = frameN  # exact frame index
                startingkey17on.setAutoDraw(True)
            frameRemains = 16 + .7- win.monitorFramePeriod * 0.75  # most of one frame period left
            if startingkey17on.status == STARTED and t >= frameRemains:
                startingkey17on.setAutoDraw(False)
            
            # *startingkey17off* updates
            if t >= 16.7 and startingkey17off.status == NOT_STARTED:
                # keep track of start time/frame for later
                startingkey17off.tStart = t
                startingkey17off.frameNStart = frameN  # exact frame index
                startingkey17off.setAutoDraw(True)
            frameRemains = 17.0 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if startingkey17off.status == STARTED and t >= frameRemains:
                startingkey17off.setAutoDraw(False)
            
            # *startingkey18on* updates
            if t >= 17 and startingkey18on.status == NOT_STARTED:
                # keep track of start time/frame for later
                startingkey18on.tStart = t
                startingkey18on.frameNStart = frameN  # exact frame index
                startingkey18on.setAutoDraw(True)
            frameRemains = 17 + .7- win.monitorFramePeriod * 0.75  # most of one frame period left
            if startingkey18on.status == STARTED and t >= frameRemains:
                startingkey18on.setAutoDraw(False)
            
            # *startingkey18off* updates
            if t >= 17.7 and startingkey18off.status == NOT_STARTED:
                # keep track of start time/frame for later
                startingkey18off.tStart = t
                startingkey18off.frameNStart = frameN  # exact frame index
                startingkey18off.setAutoDraw(True)
            frameRemains = 18 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if startingkey18off.status == STARTED and t >= frameRemains:
                startingkey18off.setAutoDraw(False)
            
            # *startingkey19on* updates
            if t >= 18 and startingkey19on.status == NOT_STARTED:
                # keep track of start time/frame for later
                startingkey19on.tStart = t
                startingkey19on.frameNStart = frameN  # exact frame index
                startingkey19on.setAutoDraw(True)
            frameRemains = 18 + .7- win.monitorFramePeriod * 0.75  # most of one frame period left
            if startingkey19on.status == STARTED and t >= frameRemains:
                startingkey19on.setAutoDraw(False)
            
            # *startingkey19off* updates
            if t >= 18.7 and startingkey19off.status == NOT_STARTED:
                # keep track of start time/frame for later
                startingkey19off.tStart = t
                startingkey19off.frameNStart = frameN  # exact frame index
                startingkey19off.setAutoDraw(True)
            frameRemains = 19 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if startingkey19off.status == STARTED and t >= frameRemains:
                startingkey19off.setAutoDraw(False)
            
            # *startingkey20on* updates
            if t >= 19 and startingkey20on.status == NOT_STARTED:
                # keep track of start time/frame for later
                startingkey20on.tStart = t
                startingkey20on.frameNStart = frameN  # exact frame index
                startingkey20on.setAutoDraw(True)
            frameRemains = 19 + .7- win.monitorFramePeriod * 0.75  # most of one frame period left
            if startingkey20on.status == STARTED and t >= frameRemains:
                startingkey20on.setAutoDraw(False)
            
            # *startingkey20off* updates
            if t >= 19.7 and startingkey20off.status == NOT_STARTED:
                # keep track of start time/frame for later
                startingkey20off.tStart = t
                startingkey20off.frameNStart = frameN  # exact frame index
                startingkey20off.setAutoDraw(True)
            frameRemains = 20 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if startingkey20off.status == STARTED and t >= frameRemains:
                startingkey20off.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in TrialstartComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Trialstart"-------
        for thisComponent in TrialstartComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # store data for trials_2 (TrialHandler)
        trials_2.addData('mouseA.x', mouseA.x)
        trials_2.addData('mouseA.y', mouseA.y)
        trials_2.addData('mouseA.leftButton', mouseA.leftButton)
        trials_2.addData('mouseA.midButton', mouseA.midButton)
        trials_2.addData('mouseA.rightButton', mouseA.rightButton)
        trials_2.addData('mouseA.time', mouseA.time)
        
        # ------Prepare to start Routine "Nopeckblankscreen"-------
        t = 0
        NopeckblankscreenClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(9.000000)
        # update component parameters for each repeat
        
        # keep track of which components have finished
        NopeckblankscreenComponents = [blankscreen]
        for thisComponent in NopeckblankscreenComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "Nopeckblankscreen"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = NopeckblankscreenClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            if skipblankscreen:
                trials_2.finished=True
                continueRoutine = False
            
            # *blankscreen* updates
            if t >= 0.0 and blankscreen.status == NOT_STARTED:
                # keep track of start time/frame for later
                blankscreen.tStart = t
                blankscreen.frameNStart = frameN  # exact frame index
                blankscreen.setAutoDraw(True)
            frameRemains = 0.0 + 9- win.monitorFramePeriod * 0.75  # most of one frame period left
            if blankscreen.status == STARTED and t >= frameRemains:
                blankscreen.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in NopeckblankscreenComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Nopeckblankscreen"-------
        for thisComponent in NopeckblankscreenComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        thisExp.nextEntry()
        
    # completed 100 repeats of 'trials_2'
    
    
    # ------Prepare to start Routine "Buffer"-------
    t = 0
    BufferClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.200000)
    # update component parameters for each repeat
    # keep track of which components have finished
    BufferComponents = [buffer]
    for thisComponent in BufferComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Buffer"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = BufferClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *buffer* updates
        if t >= 0.0 and buffer.status == NOT_STARTED:
            # keep track of start time/frame for later
            buffer.tStart = t
            buffer.frameNStart = frameN  # exact frame index
            buffer.setAutoDraw(True)
        frameRemains = 0.0 + .2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if buffer.status == STARTED and t >= frameRemains:
            buffer.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BufferComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Buffer"-------
    for thisComponent in BufferComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "Go_No_Go"-------
    t = 0
    Go_No_GoClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(10.000000)
    # update component parameters for each repeat
    skipaversivemovie = False
    skipfoodreward = False
    
    if rewarded == 'yes':
        rewardedtrial_nopeckmade = True
    if rewarded == 'no':
        nonrewarded_nopeckmade = True
    
    # setup some python lists for storing info about the mouse2
    FoodKey.setFillColor('white')
    ColorStimulus.setFillColor(color)
    # keep track of which components have finished
    Go_No_GoComponents = [mouse2, FoodKey_Area, FoodKey, background, ColorStimulus]
    for thisComponent in Go_No_GoComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Go_No_Go"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Go_No_GoClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if ColorStimulus.status == STARTED and t >= frameRemains:
            continueRoutine = False
        
        if rewarded == 'yes':
            if mouse2.isPressedIn(FoodKey_Area):
                rewardedtrial_nopeckmade = False
                skipaversivemovie = True
                skipfoodreward = False
                continueRoutine = False
        if rewarded == 'no':
            if mouse2.isPressedIn(FoodKey_Area):
                nonrewarded_nopeckmade = False
                skipaversivemovie = False
                skipfoodreward = True
                continueRoutine = False
            if mouse2.isPressedIn(background) and not mouse2.isPressedIn(FoodKey_Area):
                nonrewarded_nopeckmade = True
                skipaversivemovie = False
                skipfoodreward = True
        if mouse2.isPressedIn(background) and not (mouse2.isPressedIn(FoodKey_Area)):
            thisExp.addData('mouse2Time',t)
            thisExp.addData('mouse2position', mouse2.getPos())
            thisExp.addData('Location', "outside all stimuli")
            thisExp.nextEntry()
            while mouse2.isPressedIn(background) and not (mouse2.isPressedIn(FoodKey_Area)):
                continue
        
        elif (mouse2.isPressedIn(FoodKey_Area)):
            thisExp.addData('mouse2Time', t)
            thisExp.addData('mouse2position', mouse2.getPos())
            thisExp.addData('Location', "in food key")
            thisExp.nextEntry()
            while (mouse2.isPressedIn(FoodKey_Area)):
                continue
        
        if (mouse2.isPressedIn(ColorStimulus)):
            thisExp.addData('mouse2Time', t)
            thisExp.addData('mouse2position', mouse2.getPos())
            thisExp.addData('Location', "in color stimulus")
            thisExp.nextEntry()
            while (mouse2.isPressedIn(ColorStimulus)):
                continue
        
        # *FoodKey_Area* updates
        if t >= 0.0 and FoodKey_Area.status == NOT_STARTED:
            # keep track of start time/frame for later
            FoodKey_Area.tStart = t
            FoodKey_Area.frameNStart = frameN  # exact frame index
            FoodKey_Area.setAutoDraw(True)
        frameRemains = 0.0 + 10- win.monitorFramePeriod * 0.75  # most of one frame period left
        if FoodKey_Area.status == STARTED and t >= frameRemains:
            FoodKey_Area.setAutoDraw(False)
        
        # *FoodKey* updates
        if t >= 0 and FoodKey.status == NOT_STARTED:
            # keep track of start time/frame for later
            FoodKey.tStart = t
            FoodKey.frameNStart = frameN  # exact frame index
            FoodKey.setAutoDraw(True)
        frameRemains = 10 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if FoodKey.status == STARTED and t >= frameRemains:
            FoodKey.setAutoDraw(False)
        
        # *background* updates
        if t >= 0.0 and background.status == NOT_STARTED:
            # keep track of start time/frame for later
            background.tStart = t
            background.frameNStart = frameN  # exact frame index
            background.setAutoDraw(True)
        frameRemains = 0.0 + 10- win.monitorFramePeriod * 0.75  # most of one frame period left
        if background.status == STARTED and t >= frameRemains:
            background.setAutoDraw(False)
        
        # *ColorStimulus* updates
        if t >= 0 and ColorStimulus.status == NOT_STARTED:
            # keep track of start time/frame for later
            ColorStimulus.tStart = t
            ColorStimulus.frameNStart = frameN  # exact frame index
            ColorStimulus.setAutoDraw(True)
        frameRemains = 10 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if ColorStimulus.status == STARTED and t >= frameRemains:
            ColorStimulus.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Go_No_GoComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Go_No_Go"-------
    for thisComponent in Go_No_GoComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    
    # store data for trials (TrialHandler)
    
    # ------Prepare to start Routine "FoodReward"-------
    t = 0
    FoodRewardClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(3.100000)
    # update component parameters for each repeat
    
    feeder_open = False
    # keep track of which components have finished
    FoodRewardComponents = [FeederOpening, FeederClosing]
    for thisComponent in FoodRewardComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "FoodReward"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = FoodRewardClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if skipfoodreward:
            continueRoutine = False
        
        if rewarded == 'yes':
            if rewardedtrial_nopeckmade:
                continueRoutine = False
        
        if rewarded == 'no':
            if nonrewarded_nopeckmade:
                continueRoutine = False
        #if FeederOpening.status == STARTED:
            #if not feeder_open:
                #feeder_open = True
                #feeder_start = t # current time
                #servo.setAccel(0,-2)      #set servo 0 acceleration to -2
                #servo.setTarget(0,4500)  #move servo to feed 
                #servo.setAccel(10,-2)      #turn light on
                #servo.setTarget(10,6000) #turn light on 
        #servo settings are touchy, these will probably need altering to your specifics 
        
        #if FeederClosing.status == STARTED:
            #servo.setAccel(0,-2)      #set servo 0 acceleration to -2
            #servo.setTarget(0,6000)  #move servo to resting position
            #servo.setAccel(10,-2)      #turn light off
            #servo.setTarget(10,4500) #turn light off
            #servo.close 
            #feeder_open = False
        
        # *FeederOpening* updates
        if t >= 0.0 and FeederOpening.status == NOT_STARTED:
            # keep track of start time/frame for later
            FeederOpening.tStart = t
            FeederOpening.frameNStart = frameN  # exact frame index
            FeederOpening.setAutoDraw(True)
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if FeederOpening.status == STARTED and t >= frameRemains:
            FeederOpening.setAutoDraw(False)
        
        # *FeederClosing* updates
        if t >= 3 and FeederClosing.status == NOT_STARTED:
            # keep track of start time/frame for later
            FeederClosing.tStart = t
            FeederClosing.frameNStart = frameN  # exact frame index
            FeederClosing.setAutoDraw(True)
        frameRemains = 3 + .1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if FeederClosing.status == STARTED and t >= frameRemains:
            FeederClosing.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FoodRewardComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "FoodReward"-------
    for thisComponent in FoodRewardComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    punishmenttrial_nopeckmade = True
    
    
    # ------Prepare to start Routine "AversiveMovie"-------
    t = 0
    AversiveMovieClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    if skipaversivemovie:
        continueRoutine = False
    
    if rewarded == 'yes':
        if rewardedtrial_nopeckmade:
            continueRoutine = False
    
    if rewarded == 'no':
        if nonrewarded_nopeckmade:
            continueRoutine = False
    # keep track of which components have finished
    AversiveMovieComponents = [movie]
    for thisComponent in AversiveMovieComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "AversiveMovie"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = AversiveMovieClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *movie* updates
        if t >= 0.0 and movie.status == NOT_STARTED:
            # keep track of start time/frame for later
            movie.tStart = t
            movie.frameNStart = frameN  # exact frame index
            movie.setAutoDraw(True)
        frameRemains = 5 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if movie.status == STARTED and t >= frameRemains:
            movie.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AversiveMovieComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "AversiveMovie"-------
    for thisComponent in AversiveMovieComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    
    # ------Prepare to start Routine "ITI"-------
    t = 0
    ITIClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    ITIComponents = [iti]
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "ITI"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ITIClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *iti* updates
        if t >= 0.0 and iti.status == NOT_STARTED:
            # keep track of start time/frame for later
            iti.tStart = t
            iti.frameNStart = frameN  # exact frame index
            iti.setAutoDraw(True)
        frameRemains = 0.0 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if iti.status == STARTED and t >= frameRemains:
            iti.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ITI"-------
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 5 repeats of 'trials'








# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
