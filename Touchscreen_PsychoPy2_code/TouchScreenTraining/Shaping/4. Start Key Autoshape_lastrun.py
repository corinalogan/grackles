#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.2),
    on Fri Jan 26 11:34:12 2018
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
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
expName = 'GrackleFlex'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s_%s' % (expInfo['participant'], expInfo['session'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'/Users/grackle2/Desktop/4. Start Key Autoshape.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DATA)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1680, 1050), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "Trialstart"
TrialstartClock = core.Clock()
from psychopy import core, event

mouseA = event.Mouse(win=win)
x, y = [None, None]
startingkey1on = visual.ShapeStim(
    win=win, name='startingkey1on',
    vertices=[[-(0.35, 0.35)[0]/2.0,-(0.35, 0.35)[1]/2.0], [+(0.35, 0.35)[0]/2.0,-(0.35, 0.35)[1]/2.0], [0,(0.35, 0.35)[1]/2.0]],
    ori=0, pos=(0, -.65),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
startingkey1off = visual.ShapeStim(
    win=win, name='startingkey1off',
    vertices=[[-(0.35, 0.35)[0]/2.0,-(0.35, 0.35)[1]/2.0], [+(0.35, 0.35)[0]/2.0,-(0.35, 0.35)[1]/2.0], [0,(0.35, 0.35)[1]/2.0]],
    ori=0, pos=(0, -.65),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=-3.0, interpolate=True)
startingkey2on = visual.ShapeStim(
    win=win, name='startingkey2on',
    vertices=[[-(0.35, 0.35)[0]/2.0,-(0.35, 0.35)[1]/2.0], [+(0.35, 0.35)[0]/2.0,-(0.35, 0.35)[1]/2.0], [0,(0.35, 0.35)[1]/2.0]],
    ori=0, pos=(0, -.65),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
startingkey2off = visual.ShapeStim(
    win=win, name='startingkey2off',
    vertices=[[-(0.35, 0.35)[0]/2.0,-(0.35, 0.35)[1]/2.0], [+(0.35, 0.35)[0]/2.0,-(0.35, 0.35)[1]/2.0], [0,(0.35, 0.35)[1]/2.0]],
    ori=0, pos=(0, -.65),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=-5.0, interpolate=True)
startingkey3on = visual.ShapeStim(
    win=win, name='startingkey3on',
    vertices=[[-(0.35, 0.35)[0]/2.0,-(0.35, 0.35)[1]/2.0], [+(0.35, 0.35)[0]/2.0,-(0.35, 0.35)[1]/2.0], [0,(0.35, 0.35)[1]/2.0]],
    ori=0, pos=(0, -.65),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
startingkey3off = visual.ShapeStim(
    win=win, name='startingkey3off',
    vertices=[[-(0.35, 0.35)[0]/2.0,-(0.35, 0.35)[1]/2.0], [+(0.35, 0.35)[0]/2.0,-(0.35, 0.35)[1]/2.0], [0,(0.35, 0.35)[1]/2.0]],
    ori=0, pos=(0, -.65),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=-7.0, interpolate=True)
startingkey4on = visual.ShapeStim(
    win=win, name='startingkey4on',
    vertices=[[-(0.35, 0.35)[0]/2.0,-(0.35, 0.35)[1]/2.0], [+(0.35, 0.35)[0]/2.0,-(0.35, 0.35)[1]/2.0], [0,(0.35, 0.35)[1]/2.0]],
    ori=0, pos=(0, -.65),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-8.0, interpolate=True)
startingkey4off = visual.ShapeStim(
    win=win, name='startingkey4off',
    vertices=[[-(0.35, 0.35)[0]/2.0,-(0.35, 0.35)[1]/2.0], [+(0.35, 0.35)[0]/2.0,-(0.35, 0.35)[1]/2.0], [0,(0.35, 0.35)[1]/2.0]],
    ori=0, pos=(0, -.65),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=-9.0, interpolate=True)
startingkey5on = visual.ShapeStim(
    win=win, name='startingkey5on',
    vertices=[[-(0.35, 0.35)[0]/2.0,-(0.35, 0.35)[1]/2.0], [+(0.35, 0.35)[0]/2.0,-(0.35, 0.35)[1]/2.0], [0,(0.35, 0.35)[1]/2.0]],
    ori=0, pos=(0, -.65),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-10.0, interpolate=True)
startingkey5off = visual.ShapeStim(
    win=win, name='startingkey5off',
    vertices=[[-(0.35, 0.35)[0]/2.0,-(0.35, 0.35)[1]/2.0], [+(0.35, 0.35)[0]/2.0,-(0.35, 0.35)[1]/2.0], [0,(0.35, 0.35)[1]/2.0]],
    ori=0, pos=(0, -.65),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=-11.0, interpolate=True)

# Initialize components for Routine "stimuli"
stimuliClock = core.Clock()
from psychopy import core, event

mouse = event.Mouse(win=win)
x, y = [None, None]
background = visual.Rect(
    win=win, name='background',
    width=(3, 3)[0], height=(3, 3)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=-2.0, interpolate=True)
White_2 = visual.Rect(
    win=win, name='White_2',
    width=(0.33,0.33)[0], height=(0.33,0.33)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)

# Initialize components for Routine "Nopeckblankscreen"
NopeckblankscreenClock = core.Clock()

blankscreen = visual.Rect(
    win=win, name='blankscreen',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=-1.0, interpolate=True)

# Initialize components for Routine "FoodReward"
FoodRewardClock = core.Clock()


FeederOpening = visual.TextStim(win=win, name='FeederOpening',
    text=u'Feeder Opening',
    font=u'Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-2.0);
FeederClosing = visual.TextStim(win=win, name='FeederClosing',
    text=u'Feeder Closing\n',
    font=u'Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-3.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=10, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
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
    trials_2 = data.TrialHandler(nReps=5, method='random', 
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
        routineTimer.add(5.000000)
        # update component parameters for each repeat
        skipblankscreen = False
        timer = core.Clock()
        #event.Mouse(visible = False)
        
        
        # setup some python lists for storing info about the mouseA
        mouseA.x = []
        mouseA.y = []
        mouseA.leftButton = []
        mouseA.midButton = []
        mouseA.rightButton = []
        mouseA.time = []
        
        # setup some python lists for storing info about the mouseA
        # keep track of which components have finished
        TrialstartComponents = [mouseA, startingkey1on, startingkey1off, startingkey2on, startingkey2off, startingkey3on, startingkey3off, startingkey4on, startingkey4off, startingkey5on, startingkey5off]
        for thisComponent in TrialstartComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "Trialstart"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = TrialstartClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            if mouseA.isPressedIn(startingkey1on):
                trials_2.finished=True
                continueRoutine = False
            if mouseA.isPressedIn(startingkey1off):
                trials_2.finished=True
                continueRoutine = False
            if mouseA.isPressedIn(startingkey2on):
                trials_2.finished=True
                continueRoutine = False
            if mouseA.isPressedIn(startingkey2off):
                trials_2.finished=True
                continueRoutine = False
            if mouseA.isPressedIn(startingkey3on):
                trials_2.finished=True
                continueRoutine = False
            if mouseA.isPressedIn(startingkey3off):
                trials_2.finished=True
                continueRoutine = False
            if mouseA.isPressedIn(startingkey4on):
                trials_2.finished=True
                continueRoutine = False
            if mouseA.isPressedIn(startingkey4off):
                trials_2.finished=True
                continueRoutine = False
            if mouseA.isPressedIn(startingkey5on):
                trials_2.finished=True
                continueRoutine = False
            if mouseA.isPressedIn(startingkey5off):
                trials_2.finished=True
                continueRoutine = False
            
            # *mouseA* updates
            if t >= 0.0 and mouseA.status == NOT_STARTED:
                # keep track of start time/frame for later
                mouseA.tStart = t
                mouseA.frameNStart = frameN  # exact frame index
                mouseA.status = STARTED
                event.mouseButtons = [0, 0, 0]  # reset mouse buttons to be 'up'
            frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if mouseA.status == STARTED and t >= frameRemains:
                mouseA.status = STOPPED
            if mouseA.status == STARTED:  # only update if started and not stopped!
                buttons = mouseA.getPressed()
                #if sum(buttons) > 0:  # ie if any button is pressed
                # Record mouse position if a key is pressed
                if any(mouseA.getPressed()):
                    x, y = mouseA.getPos()
                    mouseA.x.append(x)
                    mouseA.y.append(y)
                    mouseA.leftButton.append(buttons[0])
                    mouseA.midButton.append(buttons[1])
                    mouseA.rightButton.append(buttons[2])
                    mouseA.time.append(TrialstartClock.getTime())
            
                    # Wait until all buttons are released
                while any(mouseA.getPressed()):
                    pass
            
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
        trials_2.addData('StartKeyTime', timer.getTime())
        # store data for trials_2 (TrialHandler)
        #trials_2.addData('mouseA.x', mouseA.x)
        #trials_2.addData('mouseA.y', mouseA.y)
        trials_2.addData('StartKeyNumPecks', mouseA.leftButton)
        #trials_2.addData('mouseA.midButton', mouseA.midButton)
        #trials_2.addData('mouseA.rightButton', mouseA.rightButton)
        trials_2.addData('StartKeyPeckTimes', mouseA.time)
        timer.reset()
        # store data for trials_2 (TrialHandler)
        thisExp.nextEntry()
        
    # completed 5 repeats of 'trials_2'
    
    
    # ------Prepare to start Routine "stimuli"-------
    t = 0
    stimuliClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    skipblankscreen = False
    skipfoodreward = True
    timer = core.Clock()
    
    #make the mouse invisible
    #event.Mouse(visible = False)
    
    # setup some python lists for storing info about the mouse
    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
    
    # setup some python lists for storing info about the mouse
    White_2.setPos((0,-.65))
    # keep track of which components have finished
    stimuliComponents = [mouse, background, White_2]
    for thisComponent in stimuliComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "stimuli"-------
    while continueRoutine:
        # get current time
        t = stimuliClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if mouse.isPressedIn(White_2):
            skipblankscreen = True
            skipfoodreward= False
            continueRoutine = False
        if mouse.isPressedIn(background):
            continueRoutine = False
        
        # *mouse* updates
        if t >= 0.0 and mouse.status == NOT_STARTED:
            # keep track of start time/frame for later
            mouse.tStart = t
            mouse.frameNStart = frameN  # exact frame index
            mouse.status = STARTED
            event.mouseButtons = [0, 0, 0]  # reset mouse buttons to be 'up'
        frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if mouse.status == STARTED and t >= frameRemains:
            mouse.status = STOPPED
        if mouse.status == STARTED:  # only update if started and not stopped!
            buttons = mouse.getPressed()
        #Record mouse position if a key is pressed
            if any(mouse.getPressed()):
                x, y = mouse.getPos()
                mouse.x.append(x)
                mouse.y.append(y)
                mouse.leftButton.append(buttons[0])
                mouse.midButton.append(buttons[1])
                mouse.rightButton.append(buttons[2])
                mouse.time.append(stimuliClock.getTime())
        
        #Wait until all buttons are released
            while any(mouse.getPressed()):
                pass
        
        # *background* updates
        if t >= 0.0 and background.status == NOT_STARTED:
            # keep track of start time/frame for later
            background.tStart = t
            background.frameNStart = frameN  # exact frame index
            background.setAutoDraw(True)
        
        # *White_2* updates
        if t >= 0.0 and White_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            White_2.tStart = t
            White_2.frameNStart = frameN  # exact frame index
            White_2.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stimuliComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stimuli"-------
    for thisComponent in stimuliComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials (TrialHandler)
    trials.addData('TrialTime', timer.getTime()) #stores how long the trial was in seconds
    trials.addData('SkipFoodReward', skipfoodreward) #stores whether the response was incorrect or not
    #trials.addData('mouse.x', mouse.x)   #stores x position of mouse
    #trials.addData('mouse.y', mouse.y)     #stores y position of mouse
    #trials.addData('NumPecks', mouse.leftButton)   #stores number of pecks, in this scenario it can only be 1
    #trials.addData('PeckTimes', mouseB.time)   #stores time of pecks
    timer.reset()
    # store data for trials (TrialHandler)
    # the Routine "stimuli" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Nopeckblankscreen"-------
    t = 0
    NopeckblankscreenClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(10.000000)
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
            continueRoutine = False
        
        # *blankscreen* updates
        if t >= 0.0 and blankscreen.status == NOT_STARTED:
            # keep track of start time/frame for later
            blankscreen.tStart = t
            blankscreen.frameNStart = frameN  # exact frame index
            blankscreen.setAutoDraw(True)
        frameRemains = 0.0 + 10- win.monitorFramePeriod * 0.75  # most of one frame period left
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
    
    
    # ------Prepare to start Routine "FoodReward"-------
    t = 0
    FoodRewardClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    
    #feeder_open = False
    
    
    
    
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
        #if FeederOpening.status == STARTED:
        #    if not feeder_open:
        #        feeder_open = True
        #        feeder_start = t # current time
        #        servo.setAccel(0,-2)      #set servo 0 acceleration to -2
        #        servo.setTarget(0,4600)  #move servo to feed 
        #servo settings are touchy, these will probably need altering to your specifics 
        
        #if FeederClosing.status == STARTED:
        #    servo.setAccel(0,-2)      #set servo 0 acceleration to -2
        #    servo.setTarget(0,6000)  #move servo to resting position
        #    servo.close 
        #    feeder_open = False
        
        # *FeederOpening* updates
        if t >= 0.0 and FeederOpening.status == NOT_STARTED:
            # keep track of start time/frame for later
            FeederOpening.tStart = t
            FeederOpening.frameNStart = frameN  # exact frame index
            FeederOpening.setAutoDraw(True)
        frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if FeederOpening.status == STARTED and t >= frameRemains:
            FeederOpening.setAutoDraw(False)
        
        # *FeederClosing* updates
        if t >= 1.5 and FeederClosing.status == NOT_STARTED:
            # keep track of start time/frame for later
            FeederClosing.tStart = t
            FeederClosing.frameNStart = frameN  # exact frame index
            FeederClosing.setAutoDraw(True)
        frameRemains = 1.5 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
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
    
    
    thisExp.nextEntry()
    
# completed 10 repeats of 'trials'






# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
