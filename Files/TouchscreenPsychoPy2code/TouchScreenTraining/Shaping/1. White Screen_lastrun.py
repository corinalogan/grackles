#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.2),
    on Thu Jan 25 11:29:30 2018
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
    originPath=u'/Users/grackle2/Desktop/1. White Screen.psyexp',
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

# Initialize components for Routine "AllWhite"
AllWhiteClock = core.Clock()
from psychopy import core, event

mouse = event.Mouse(win=win)
x, y = [None, None]
whitescreen = visual.Rect(
    win=win, name='whitescreen',
    width=(3, 3)[0], height=(3, 3)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)

# Initialize components for Routine "FoodReward"
FoodRewardClock = core.Clock()


FeederOpening = visual.TextStim(win=win, name='FeederOpening',
    text='Feeder Opening',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
FeederClosing = visual.TextStim(win=win, name='FeederClosing',
    text='Feeder Closing\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
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
    
    # ------Prepare to start Routine "AllWhite"-------
    t = 0
    AllWhiteClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    skipfoodreward = False
    timer = core.Clock()
    #event.Mouse(visible = False)
    
    
    # setup some python lists for storing info about the mouseA
    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
    
    # setup some python lists for storing info about the mouse
    # keep track of which components have finished
    AllWhiteComponents = [mouse, whitescreen]
    for thisComponent in AllWhiteComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "AllWhite"-------
    while continueRoutine:
        # get current time
        t = AllWhiteClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if mouse.isPressedIn(whitescreen):
            skipfoodreward = False
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
        # Record mouse position if a key is pressed
            if any(mouse.getPressed()):
                x, y = mouse.getPos()
                mouse.x.append(x)
                mouse.y.append(y)
                mouse.leftButton.append(buttons[0])
                mouse.midButton.append(buttons[1])
                mouse.rightButton.append(buttons[2])
                mouse.time.append(AllWhiteClock.getTime())
        
                # Wait until all buttons are released
            while any(mouse.getPressed()):
                pass
        
        # *whitescreen* updates
        if t >= 0.0 and whitescreen.status == NOT_STARTED:
            # keep track of start time/frame for later
            whitescreen.tStart = t
            whitescreen.frameNStart = frameN  # exact frame index
            whitescreen.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AllWhiteComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "AllWhite"-------
    for thisComponent in AllWhiteComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials (TrialHandler)
    trials.addData('TrialTime', timer.getTime())
    #trials_1.addData('mouse.x', mouse.x)
    #trials_1.addData('mouse.y', mouse.y)
    #trials_1.addData('NumPecks', mouse.leftButton)
    #trials_1.addData('PeckTimes', mouse.time)
    timer.reset()
    # store data for trials (TrialHandler)
    # the Routine "AllWhite" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
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
            #if not feeder_open:
                #feeder_open = True
                #feeder_start = t # current time
                #servo.setAccel(0,-2)      #set servo 0 acceleration to -2
                #servo.setTarget(0,4600)  #move servo to feed 
                #servo.setAccel(10,-2)  #code for light
                #servo.setTarget(10,6000) #turn light on
        
        #servo settings are touchy, these will probably need altering to your specifics 
        
        #if FeederClosing.status == STARTED:
            #servo.setAccel(0,-2)      #set servo 0 acceleration to -2
            #servo.setTarget(0,6000)  #move servo to resting position
            #servo.setAccel(10,-2) #code for light
            #servo.setTarget(10,4500) #turns light off
            #servo.close 
            #feeder_open = False
        
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
