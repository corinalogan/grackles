#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.2),
    on Mon Jun 18 12:59:32 2018
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
expName = 'newnewnew'  # from the Builder filename that created this script
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
    originPath=u'/Users/grackle2/Documents/Touchscreen/MovingTargetTraining/moving_stim.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1680, 1050), fullscr=True, screen=0,
    allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='cm')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "Moving_Stim"
Moving_StimClock = core.Clock()
background = visual.Rect(
    win=win, name='background',units='cm', 
    width=(50, 40)[0], height=(50, 40)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
out_circle = visual.Polygon(
    win=win, name='out_circle',
    edges=99, size=(2, 2),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='red', fillColorSpace='rgb',
    opacity=0, depth=-1.0, interpolate=True)
target = visual.Polygon(
    win=win, name='target',units='cm', 
    edges=99, size=(0.5, 0.5),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='White', fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
mouse = event.Mouse(win=win)
x, y = [None, None]

audio_FB = sound.Sound('1300', secs=-1)
audio_FB.setVolume(1)

# Initialize components for Routine "Reward"
RewardClock = core.Clock()
background_4 = visual.Rect(
    win=win, name='background_4',
    width=(50, 40)[0], height=(50, 40)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
FeederOpen = visual.TextStim(win=win, name='FeederOpen',
    text='Feeder Is Open',
    font='Arial',
    pos=(0, 0), height=2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
FeederClosed = visual.TextStim(win=win, name='FeederClosed',
    text='Feeder is Closing',
    font='Arial',
    pos=(0, 0), height=2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);


# Initialize components for Routine "ITI"
ITIClock = core.Clock()
invisible = visual.Rect(
    win=win, name='invisible',
    width=(50, 50)[0], height=(50, 50)[1],
    ori=0, pos=(0, -.75),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1.0, depth=0.0, interpolate=True)

# Initialize components for Routine "Moving_Stim_2"
Moving_Stim_2Clock = core.Clock()
background_2 = visual.Rect(
    win=win, name='background_2',units='cm', 
    width=(50, 40)[0], height=(50, 40)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
out_circle_2 = visual.Polygon(
    win=win, name='out_circle_2',
    edges=99, size=(2, 2),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='red', fillColorSpace='rgb',
    opacity=0, depth=-1.0, interpolate=True)
target_2 = visual.Polygon(
    win=win, name='target_2',units='cm', 
    edges=99, size=(0.5, 0.5),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='White', fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
mouse_2 = event.Mouse(win=win)
x, y = [None, None]

audio_FB2 = sound.Sound('1300', secs=-1)
audio_FB2.setVolume(1)

# Initialize components for Routine "Reward"
RewardClock = core.Clock()
background_4 = visual.Rect(
    win=win, name='background_4',
    width=(50, 40)[0], height=(50, 40)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
FeederOpen = visual.TextStim(win=win, name='FeederOpen',
    text='Feeder Is Open',
    font='Arial',
    pos=(0, 0), height=2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
FeederClosed = visual.TextStim(win=win, name='FeederClosed',
    text='Feeder is Closing',
    font='Arial',
    pos=(0, 0), height=2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);


# Initialize components for Routine "ITI"
ITIClock = core.Clock()
invisible = visual.Rect(
    win=win, name='invisible',
    width=(50, 50)[0], height=(50, 50)[1],
    ori=0, pos=(0, -.75),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1.0, depth=0.0, interpolate=True)

# Initialize components for Routine "Moving_Stim_3"
Moving_Stim_3Clock = core.Clock()
background_3 = visual.Rect(
    win=win, name='background_3',units='cm', 
    width=(50, 40)[0], height=(50, 40)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
out_circle_3 = visual.Polygon(
    win=win, name='out_circle_3',
    edges=99, size=(2, 2),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='red', fillColorSpace='rgb',
    opacity=0, depth=-1.0, interpolate=True)
target_3 = visual.Polygon(
    win=win, name='target_3',units='cm', 
    edges=99, size=(0.5, 0.5),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='White', fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
mouse_3 = event.Mouse(win=win)
x, y = [None, None]

audio_FB3 = sound.Sound('1300', secs=-1)
audio_FB3.setVolume(1)

# Initialize components for Routine "Reward"
RewardClock = core.Clock()
background_4 = visual.Rect(
    win=win, name='background_4',
    width=(50, 40)[0], height=(50, 40)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
FeederOpen = visual.TextStim(win=win, name='FeederOpen',
    text='Feeder Is Open',
    font='Arial',
    pos=(0, 0), height=2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
FeederClosed = visual.TextStim(win=win, name='FeederClosed',
    text='Feeder is Closing',
    font='Arial',
    pos=(0, 0), height=2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);


# Initialize components for Routine "ITI"
ITIClock = core.Clock()
invisible = visual.Rect(
    win=win, name='invisible',
    width=(50, 50)[0], height=(50, 50)[1],
    ori=0, pos=(0, -.75),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1.0, depth=0.0, interpolate=True)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
Main_Loop = data.TrialHandler(nReps=2, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='Main_Loop')
thisExp.addLoop(Main_Loop)  # add the loop to the experiment
thisMain_Loop = Main_Loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisMain_Loop.rgb)
if thisMain_Loop != None:
    for paramName in thisMain_Loop.keys():
        exec(paramName + '= thisMain_Loop.' + paramName)

for thisMain_Loop in Main_Loop:
    currentLoop = Main_Loop
    # abbreviate parameter names if possible (e.g. rgb = thisMain_Loop.rgb)
    if thisMain_Loop != None:
        for paramName in thisMain_Loop.keys():
            exec(paramName + '= thisMain_Loop.' + paramName)
    
    # set up handler to look after randomisation of conditions etc
    Path_A = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(u'ITI_time.xlsx'),
        seed=None, name='Path_A')
    thisExp.addLoop(Path_A)  # add the loop to the experiment
    thisPath_A = Path_A.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPath_A.rgb)
    if thisPath_A != None:
        for paramName in thisPath_A.keys():
            exec(paramName + '= thisPath_A.' + paramName)
    
    for thisPath_A in Path_A:
        currentLoop = Path_A
        # abbreviate parameter names if possible (e.g. rgb = thisPath_A.rgb)
        if thisPath_A != None:
            for paramName in thisPath_A.keys():
                exec(paramName + '= thisPath_A.' + paramName)
        
        # set up handler to look after randomisation of conditions etc
        Trial_A = data.TrialHandler(nReps=2, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(u'Path_1.xlsx'),
            seed=None, name='Trial_A')
        thisExp.addLoop(Trial_A)  # add the loop to the experiment
        thisTrial_A = Trial_A.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_A.rgb)
        if thisTrial_A != None:
            for paramName in thisTrial_A.keys():
                exec(paramName + '= thisTrial_A.' + paramName)
        
        for thisTrial_A in Trial_A:
            currentLoop = Trial_A
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_A.rgb)
            if thisTrial_A != None:
                for paramName in thisTrial_A.keys():
                    exec(paramName + '= thisTrial_A.' + paramName)
            
            # ------Prepare to start Routine "Moving_Stim"-------
            t = 0
            Moving_StimClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(0.100000)
            # update component parameters for each repeat
            out_circle.setPos(pos)
            target.setPos(pos)
            # setup some python lists for storing info about the mouse
            
            # keep track of which components have finished
            Moving_StimComponents = [background, out_circle, target, mouse, audio_FB]
            for thisComponent in Moving_StimComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "Moving_Stim"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = Moving_StimClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *background* updates
                if t >= 0.0 and background.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    background.tStart = t
                    background.frameNStart = frameN  # exact frame index
                    background.setAutoDraw(True)
                frameRemains = 0.0 + .1- win.monitorFramePeriod * 0.75  # most of one frame period left
                if background.status == STARTED and t >= frameRemains:
                    background.setAutoDraw(False)
                
                # *out_circle* updates
                if t >= 0.0 and out_circle.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    out_circle.tStart = t
                    out_circle.frameNStart = frameN  # exact frame index
                    out_circle.setAutoDraw(True)
                frameRemains = 0.0 + .1- win.monitorFramePeriod * 0.75  # most of one frame period left
                if out_circle.status == STARTED and t >= frameRemains:
                    out_circle.setAutoDraw(False)
                
                # *target* updates
                if t >= 0.0 and target.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    target.tStart = t
                    target.frameNStart = frameN  # exact frame index
                    target.setAutoDraw(True)
                frameRemains = 0.0 + .1- win.monitorFramePeriod * 0.75  # most of one frame period left
                if target.status == STARTED and t >= frameRemains:
                    target.setAutoDraw(False)
                # *mouse* updates
                if t >= 0.0 and mouse.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    mouse.tStart = t
                    mouse.frameNStart = frameN  # exact frame index
                    mouse.status = STARTED
                    event.mouseButtons = [0, 0, 0]  # reset mouse buttons to be 'up'
                frameRemains = 0.0 + .1- win.monitorFramePeriod * 0.75  # most of one frame period left
                if mouse.status == STARTED and t >= frameRemains:
                    mouse.status = STOPPED
                if mouse.status == STARTED:  # only update if started and not stopped!
                    buttons = mouse.getPressed()
                    if sum(buttons) > 0:  # ie if any button is pressed
                        # abort routine on response
                        continueRoutine = False
                if mouse.isPressedIn(out_circle):
                    audio_FB.tStart = t
                    audio_FB.frameNStart = frameN  # exact frame index
                    audio_FB.play()  # start the sound (it finishes automatically)
                    thisExp.addData('Time',t)
                    thisExp.addData('Pos', mouse.getPos())
                    thisExp.addData('In_Stim', 1)
                    thisExp.nextEntry()
                    continueRoutine = False
                    Trial_A.finished=True
                while mouse.isPressedIn(out_circle):
                        continue
                if mouse.isPressedIn(background) and not (mouse.isPressedIn(out_circle)):
                    audio_FB.tStart = t
                    audio_FB.frameNStart = frameN  # exact frame index
                    audio_FB.play()  # start the sound (it finishes automatically)
                    thisExp.addData('Time',t)
                    thisExp.addData('Pos', mouse.getPos())
                    thisExp.addData('In_Stim', 0)
                    thisExp.nextEntry()
                while mouse.isPressedIn(background) and not (mouse.isPressedIn(out_circle)):
                            continue
                # start/stop audio_FB
                if (0.0) and audio_FB.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    audio_FB.tStart = t
                    audio_FB.frameNStart = frameN  # exact frame index
                    audio_FB.play()  # start the sound (it finishes automatically)
                if audio_FB.status == STARTED and t >= (audio_FB.tStart + .1):
                    audio_FB.stop()  # stop the sound (if longer than duration)
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Moving_StimComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "Moving_Stim"-------
            for thisComponent in Moving_StimComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store data for Trial_A (TrialHandler)
            x, y = mouse.getPos()
            buttons = mouse.getPressed()
            Trial_A.addData('mouse.x', x)
            Trial_A.addData('mouse.y', y)
            Trial_A.addData('mouse.leftButton', buttons[0])
            Trial_A.addData('mouse.midButton', buttons[1])
            Trial_A.addData('mouse.rightButton', buttons[2])
            
            audio_FB.stop()  # ensure sound has stopped at end of routine
            thisExp.nextEntry()
            
        # completed 2 repeats of 'Trial_A'
        
        
        # ------Prepare to start Routine "Reward"-------
        t = 0
        RewardClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        feeder_open = False
        # keep track of which components have finished
        RewardComponents = [background_4, FeederOpen, FeederClosed]
        for thisComponent in RewardComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "Reward"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = RewardClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *background_4* updates
            if t >= 0.0 and background_4.status == NOT_STARTED:
                # keep track of start time/frame for later
                background_4.tStart = t
                background_4.frameNStart = frameN  # exact frame index
                background_4.setAutoDraw(True)
            frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
            if background_4.status == STARTED and t >= frameRemains:
                background_4.setAutoDraw(False)
            
            # *FeederOpen* updates
            if t >= 0.0 and FeederOpen.status == NOT_STARTED:
                # keep track of start time/frame for later
                FeederOpen.tStart = t
                FeederOpen.frameNStart = frameN  # exact frame index
                FeederOpen.setAutoDraw(True)
            frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if FeederOpen.status == STARTED and t >= frameRemains:
                FeederOpen.setAutoDraw(False)
            
            # *FeederClosed* updates
            if t >= 1.5 and FeederClosed.status == NOT_STARTED:
                # keep track of start time/frame for later
                FeederClosed.tStart = t
                FeederClosed.frameNStart = frameN  # exact frame index
                FeederClosed.setAutoDraw(True)
            frameRemains = 1.5 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if FeederClosed.status == STARTED and t >= frameRemains:
                FeederClosed.setAutoDraw(False)
            #if FeederOpen.status == STARTED:
                #if not feeder_open:
                    #feeder_open = True
                    #feeder_start = t # current time
                    #servo.setAccel(0,-2)      #set servo 0 acceleration to -2
                    #servo.setTarget(0,4500)  #move servo to feed 
            #servo settings are touchy, these will probably need altering to your specifics 
            
            #if FeederClosed.status == STARTED:
                #servo.setAccel(0,-2)      #set servo 0 acceleration to -2
                #servo.setTarget(0,6000)  #move servo to resting position
                #servo.close 
                #feeder_open = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in RewardComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Reward"-------
        for thisComponent in RewardComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        
        # ------Prepare to start Routine "ITI"-------
        t = 0
        ITIClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        invisible.setOpacity(1)
        # keep track of which components have finished
        ITIComponents = [invisible]
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "ITI"-------
        while continueRoutine:
            # get current time
            t = ITIClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *invisible* updates
            if t >= 0.0 and invisible.status == NOT_STARTED:
                # keep track of start time/frame for later
                invisible.tStart = t
                invisible.frameNStart = frameN  # exact frame index
                invisible.setAutoDraw(True)
            frameRemains = 0.0 + ITI_time- win.monitorFramePeriod * 0.75  # most of one frame period left
            if invisible.status == STARTED and t >= frameRemains:
                invisible.setAutoDraw(False)
            
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
        # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'Path_A'
    
    
    # set up handler to look after randomisation of conditions etc
    Path_B = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(u'ITI_time.xlsx'),
        seed=None, name='Path_B')
    thisExp.addLoop(Path_B)  # add the loop to the experiment
    thisPath_B = Path_B.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPath_B.rgb)
    if thisPath_B != None:
        for paramName in thisPath_B.keys():
            exec(paramName + '= thisPath_B.' + paramName)
    
    for thisPath_B in Path_B:
        currentLoop = Path_B
        # abbreviate parameter names if possible (e.g. rgb = thisPath_B.rgb)
        if thisPath_B != None:
            for paramName in thisPath_B.keys():
                exec(paramName + '= thisPath_B.' + paramName)
        
        # set up handler to look after randomisation of conditions etc
        Trial_B = data.TrialHandler(nReps=2, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(u'Path_2.xlsx'),
            seed=None, name='Trial_B')
        thisExp.addLoop(Trial_B)  # add the loop to the experiment
        thisTrial_B = Trial_B.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_B.rgb)
        if thisTrial_B != None:
            for paramName in thisTrial_B.keys():
                exec(paramName + '= thisTrial_B.' + paramName)
        
        for thisTrial_B in Trial_B:
            currentLoop = Trial_B
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_B.rgb)
            if thisTrial_B != None:
                for paramName in thisTrial_B.keys():
                    exec(paramName + '= thisTrial_B.' + paramName)
            
            # ------Prepare to start Routine "Moving_Stim_2"-------
            t = 0
            Moving_Stim_2Clock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(0.100000)
            # update component parameters for each repeat
            out_circle_2.setPos(pos)
            target_2.setPos(pos)
            # setup some python lists for storing info about the mouse_2
            
            # keep track of which components have finished
            Moving_Stim_2Components = [background_2, out_circle_2, target_2, mouse_2, audio_FB2]
            for thisComponent in Moving_Stim_2Components:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "Moving_Stim_2"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = Moving_Stim_2Clock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *background_2* updates
                if t >= 0.0 and background_2.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    background_2.tStart = t
                    background_2.frameNStart = frameN  # exact frame index
                    background_2.setAutoDraw(True)
                frameRemains = 0.0 + .1- win.monitorFramePeriod * 0.75  # most of one frame period left
                if background_2.status == STARTED and t >= frameRemains:
                    background_2.setAutoDraw(False)
                
                # *out_circle_2* updates
                if t >= 0.0 and out_circle_2.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    out_circle_2.tStart = t
                    out_circle_2.frameNStart = frameN  # exact frame index
                    out_circle_2.setAutoDraw(True)
                frameRemains = 0.0 + .1- win.monitorFramePeriod * 0.75  # most of one frame period left
                if out_circle_2.status == STARTED and t >= frameRemains:
                    out_circle_2.setAutoDraw(False)
                
                # *target_2* updates
                if t >= 0.0 and target_2.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    target_2.tStart = t
                    target_2.frameNStart = frameN  # exact frame index
                    target_2.setAutoDraw(True)
                frameRemains = 0.0 + .1- win.monitorFramePeriod * 0.75  # most of one frame period left
                if target_2.status == STARTED and t >= frameRemains:
                    target_2.setAutoDraw(False)
                # *mouse_2* updates
                if t >= 0.0 and mouse_2.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    mouse_2.tStart = t
                    mouse_2.frameNStart = frameN  # exact frame index
                    mouse_2.status = STARTED
                    event.mouseButtons = [0, 0, 0]  # reset mouse buttons to be 'up'
                frameRemains = 0.0 + .1- win.monitorFramePeriod * 0.75  # most of one frame period left
                if mouse_2.status == STARTED and t >= frameRemains:
                    mouse_2.status = STOPPED
                if mouse_2.status == STARTED:  # only update if started and not stopped!
                    buttons = mouse_2.getPressed()
                    if sum(buttons) > 0:  # ie if any button is pressed
                        # abort routine on response
                        continueRoutine = False
                if mouse_2.isPressedIn(out_circle_2):
                    audio_FB2.tStart = t
                    audio_FB2.frameNStart = frameN  # exact frame index
                    audio_FB2.play()  # start the sound (it finishes automatically)
                    thisExp.addData('Time',t)
                    thisExp.addData('Pos', mouse_2.getPos())
                    thisExp.addData('In_Stim', 1)
                    thisExp.nextEntry()
                    continueRoutine = False
                    Trial_B.finished=True
                while mouse_2.isPressedIn(out_circle_2):
                    continue
                if mouse_2.isPressedIn(background_2) and not (mouse_2.isPressedIn(out_circle_2)):
                    audio_FB2.tStart = t
                    audio_FB2.frameNStart = frameN  # exact frame index
                    audio_FB2.play()  # start the sound (it finishes automatically)
                    thisExp.addData('Time',t)
                    thisExp.addData('Pos', mouse_2.getPos())
                    thisExp.addData('In_Stim', 0)
                    thisExp.nextEntry()
                while mouse_2.isPressedIn(background_2) and not (mouse_2.isPressedIn(out_circle_2)):
                    continue
                # start/stop audio_FB2
                if (0.0) and audio_FB2.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    audio_FB2.tStart = t
                    audio_FB2.frameNStart = frameN  # exact frame index
                    audio_FB2.play()  # start the sound (it finishes automatically)
                if audio_FB2.status == STARTED and t >= (audio_FB2.tStart + .1):
                    audio_FB2.stop()  # stop the sound (if longer than duration)
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Moving_Stim_2Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "Moving_Stim_2"-------
            for thisComponent in Moving_Stim_2Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store data for Trial_B (TrialHandler)
            x, y = mouse_2.getPos()
            buttons = mouse_2.getPressed()
            Trial_B.addData('mouse_2.x', x)
            Trial_B.addData('mouse_2.y', y)
            Trial_B.addData('mouse_2.leftButton', buttons[0])
            Trial_B.addData('mouse_2.midButton', buttons[1])
            Trial_B.addData('mouse_2.rightButton', buttons[2])
            
            audio_FB2.stop()  # ensure sound has stopped at end of routine
            thisExp.nextEntry()
            
        # completed 2 repeats of 'Trial_B'
        
        
        # ------Prepare to start Routine "Reward"-------
        t = 0
        RewardClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        feeder_open = False
        # keep track of which components have finished
        RewardComponents = [background_4, FeederOpen, FeederClosed]
        for thisComponent in RewardComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "Reward"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = RewardClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *background_4* updates
            if t >= 0.0 and background_4.status == NOT_STARTED:
                # keep track of start time/frame for later
                background_4.tStart = t
                background_4.frameNStart = frameN  # exact frame index
                background_4.setAutoDraw(True)
            frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
            if background_4.status == STARTED and t >= frameRemains:
                background_4.setAutoDraw(False)
            
            # *FeederOpen* updates
            if t >= 0.0 and FeederOpen.status == NOT_STARTED:
                # keep track of start time/frame for later
                FeederOpen.tStart = t
                FeederOpen.frameNStart = frameN  # exact frame index
                FeederOpen.setAutoDraw(True)
            frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if FeederOpen.status == STARTED and t >= frameRemains:
                FeederOpen.setAutoDraw(False)
            
            # *FeederClosed* updates
            if t >= 1.5 and FeederClosed.status == NOT_STARTED:
                # keep track of start time/frame for later
                FeederClosed.tStart = t
                FeederClosed.frameNStart = frameN  # exact frame index
                FeederClosed.setAutoDraw(True)
            frameRemains = 1.5 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if FeederClosed.status == STARTED and t >= frameRemains:
                FeederClosed.setAutoDraw(False)
            #if FeederOpen.status == STARTED:
                #if not feeder_open:
                    #feeder_open = True
                    #feeder_start = t # current time
                    #servo.setAccel(0,-2)      #set servo 0 acceleration to -2
                    #servo.setTarget(0,4500)  #move servo to feed 
            #servo settings are touchy, these will probably need altering to your specifics 
            
            #if FeederClosed.status == STARTED:
                #servo.setAccel(0,-2)      #set servo 0 acceleration to -2
                #servo.setTarget(0,6000)  #move servo to resting position
                #servo.close 
                #feeder_open = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in RewardComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Reward"-------
        for thisComponent in RewardComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        
        # ------Prepare to start Routine "ITI"-------
        t = 0
        ITIClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        invisible.setOpacity(1)
        # keep track of which components have finished
        ITIComponents = [invisible]
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "ITI"-------
        while continueRoutine:
            # get current time
            t = ITIClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *invisible* updates
            if t >= 0.0 and invisible.status == NOT_STARTED:
                # keep track of start time/frame for later
                invisible.tStart = t
                invisible.frameNStart = frameN  # exact frame index
                invisible.setAutoDraw(True)
            frameRemains = 0.0 + ITI_time- win.monitorFramePeriod * 0.75  # most of one frame period left
            if invisible.status == STARTED and t >= frameRemains:
                invisible.setAutoDraw(False)
            
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
        # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'Path_B'
    
    
    # set up handler to look after randomisation of conditions etc
    Path_C = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(u'ITI_time.xlsx'),
        seed=None, name='Path_C')
    thisExp.addLoop(Path_C)  # add the loop to the experiment
    thisPath_C = Path_C.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPath_C.rgb)
    if thisPath_C != None:
        for paramName in thisPath_C.keys():
            exec(paramName + '= thisPath_C.' + paramName)
    
    for thisPath_C in Path_C:
        currentLoop = Path_C
        # abbreviate parameter names if possible (e.g. rgb = thisPath_C.rgb)
        if thisPath_C != None:
            for paramName in thisPath_C.keys():
                exec(paramName + '= thisPath_C.' + paramName)
        
        # set up handler to look after randomisation of conditions etc
        Trial_C = data.TrialHandler(nReps=2, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(u'Path_3.xlsx'),
            seed=None, name='Trial_C')
        thisExp.addLoop(Trial_C)  # add the loop to the experiment
        thisTrial_C = Trial_C.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_C.rgb)
        if thisTrial_C != None:
            for paramName in thisTrial_C.keys():
                exec(paramName + '= thisTrial_C.' + paramName)
        
        for thisTrial_C in Trial_C:
            currentLoop = Trial_C
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_C.rgb)
            if thisTrial_C != None:
                for paramName in thisTrial_C.keys():
                    exec(paramName + '= thisTrial_C.' + paramName)
            
            # ------Prepare to start Routine "Moving_Stim_3"-------
            t = 0
            Moving_Stim_3Clock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(0.100000)
            # update component parameters for each repeat
            out_circle_3.setPos(pos)
            target_3.setPos(pos)
            # setup some python lists for storing info about the mouse_3
            
            # keep track of which components have finished
            Moving_Stim_3Components = [background_3, out_circle_3, target_3, mouse_3, audio_FB3]
            for thisComponent in Moving_Stim_3Components:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "Moving_Stim_3"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = Moving_Stim_3Clock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *background_3* updates
                if t >= 0.0 and background_3.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    background_3.tStart = t
                    background_3.frameNStart = frameN  # exact frame index
                    background_3.setAutoDraw(True)
                frameRemains = 0.0 + .1- win.monitorFramePeriod * 0.75  # most of one frame period left
                if background_3.status == STARTED and t >= frameRemains:
                    background_3.setAutoDraw(False)
                
                # *out_circle_3* updates
                if t >= 0.0 and out_circle_3.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    out_circle_3.tStart = t
                    out_circle_3.frameNStart = frameN  # exact frame index
                    out_circle_3.setAutoDraw(True)
                frameRemains = 0.0 + .1- win.monitorFramePeriod * 0.75  # most of one frame period left
                if out_circle_3.status == STARTED and t >= frameRemains:
                    out_circle_3.setAutoDraw(False)
                
                # *target_3* updates
                if t >= 0.0 and target_3.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    target_3.tStart = t
                    target_3.frameNStart = frameN  # exact frame index
                    target_3.setAutoDraw(True)
                frameRemains = 0.0 + .1- win.monitorFramePeriod * 0.75  # most of one frame period left
                if target_3.status == STARTED and t >= frameRemains:
                    target_3.setAutoDraw(False)
                # *mouse_3* updates
                if t >= 0.0 and mouse_3.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    mouse_3.tStart = t
                    mouse_3.frameNStart = frameN  # exact frame index
                    mouse_3.status = STARTED
                    event.mouseButtons = [0, 0, 0]  # reset mouse buttons to be 'up'
                frameRemains = 0.0 + .1- win.monitorFramePeriod * 0.75  # most of one frame period left
                if mouse_3.status == STARTED and t >= frameRemains:
                    mouse_3.status = STOPPED
                if mouse_3.status == STARTED:  # only update if started and not stopped!
                    buttons = mouse_3.getPressed()
                    if sum(buttons) > 0:  # ie if any button is pressed
                        # abort routine on response
                        continueRoutine = False
                if mouse_3.isPressedIn(out_circle_3):
                    audio_FB3.tStart = t
                    audio_FB3.frameNStart = frameN  # exact frame index
                    audio_FB3.play()  # start the sound (it finishes automatically)
                    thisExp.addData('Time',t)
                    thisExp.addData('Pos', mouse_3.getPos())
                    thisExp.addData('In_Stim', 1)
                    thisExp.nextEntry()
                    continueRoutine = False
                    Trial_C.finished=True
                while mouse_3.isPressedIn(out_circle_3):
                        continue
                if mouse.isPressedIn(background_3) and not (mouse_3.isPressedIn(out_circle_3)):
                    audio_FB3.tStart = t
                    audio_FB3.frameNStart = frameN  # exact frame index
                    audio_FB3.play()  # start the sound (it finishes automatically)
                    thisExp.addData('Time',t)
                    thisExp.addData('Pos', mouse_3.getPos())
                    thisExp.addData('In_Stim', 0)
                    thisExp.nextEntry()
                while mouse_3.isPressedIn(background_3) and not (mouse_3.isPressedIn(out_circle_3)):
                            continue
                # start/stop audio_FB3
                if (0.0) and audio_FB3.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    audio_FB3.tStart = t
                    audio_FB3.frameNStart = frameN  # exact frame index
                    audio_FB3.play()  # start the sound (it finishes automatically)
                if audio_FB3.status == STARTED and t >= (audio_FB3.tStart + .1):
                    audio_FB3.stop()  # stop the sound (if longer than duration)
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Moving_Stim_3Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "Moving_Stim_3"-------
            for thisComponent in Moving_Stim_3Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store data for Trial_C (TrialHandler)
            x, y = mouse_3.getPos()
            buttons = mouse_3.getPressed()
            Trial_C.addData('mouse_3.x', x)
            Trial_C.addData('mouse_3.y', y)
            Trial_C.addData('mouse_3.leftButton', buttons[0])
            Trial_C.addData('mouse_3.midButton', buttons[1])
            Trial_C.addData('mouse_3.rightButton', buttons[2])
            
            audio_FB3.stop()  # ensure sound has stopped at end of routine
            thisExp.nextEntry()
            
        # completed 2 repeats of 'Trial_C'
        
        
        # ------Prepare to start Routine "Reward"-------
        t = 0
        RewardClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        feeder_open = False
        # keep track of which components have finished
        RewardComponents = [background_4, FeederOpen, FeederClosed]
        for thisComponent in RewardComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "Reward"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = RewardClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *background_4* updates
            if t >= 0.0 and background_4.status == NOT_STARTED:
                # keep track of start time/frame for later
                background_4.tStart = t
                background_4.frameNStart = frameN  # exact frame index
                background_4.setAutoDraw(True)
            frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
            if background_4.status == STARTED and t >= frameRemains:
                background_4.setAutoDraw(False)
            
            # *FeederOpen* updates
            if t >= 0.0 and FeederOpen.status == NOT_STARTED:
                # keep track of start time/frame for later
                FeederOpen.tStart = t
                FeederOpen.frameNStart = frameN  # exact frame index
                FeederOpen.setAutoDraw(True)
            frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if FeederOpen.status == STARTED and t >= frameRemains:
                FeederOpen.setAutoDraw(False)
            
            # *FeederClosed* updates
            if t >= 1.5 and FeederClosed.status == NOT_STARTED:
                # keep track of start time/frame for later
                FeederClosed.tStart = t
                FeederClosed.frameNStart = frameN  # exact frame index
                FeederClosed.setAutoDraw(True)
            frameRemains = 1.5 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if FeederClosed.status == STARTED and t >= frameRemains:
                FeederClosed.setAutoDraw(False)
            #if FeederOpen.status == STARTED:
                #if not feeder_open:
                    #feeder_open = True
                    #feeder_start = t # current time
                    #servo.setAccel(0,-2)      #set servo 0 acceleration to -2
                    #servo.setTarget(0,4500)  #move servo to feed 
            #servo settings are touchy, these will probably need altering to your specifics 
            
            #if FeederClosed.status == STARTED:
                #servo.setAccel(0,-2)      #set servo 0 acceleration to -2
                #servo.setTarget(0,6000)  #move servo to resting position
                #servo.close 
                #feeder_open = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in RewardComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Reward"-------
        for thisComponent in RewardComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        
        # ------Prepare to start Routine "ITI"-------
        t = 0
        ITIClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        invisible.setOpacity(1)
        # keep track of which components have finished
        ITIComponents = [invisible]
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "ITI"-------
        while continueRoutine:
            # get current time
            t = ITIClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *invisible* updates
            if t >= 0.0 and invisible.status == NOT_STARTED:
                # keep track of start time/frame for later
                invisible.tStart = t
                invisible.frameNStart = frameN  # exact frame index
                invisible.setAutoDraw(True)
            frameRemains = 0.0 + ITI_time- win.monitorFramePeriod * 0.75  # most of one frame period left
            if invisible.status == STARTED and t >= frameRemains:
                invisible.setAutoDraw(False)
            
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
        # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'Path_C'
    
    thisExp.nextEntry()
    
# completed 2 repeats of 'Main_Loop'







# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
