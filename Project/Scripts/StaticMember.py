import numpy
import Static_Funtion
windowSize = None
GameRunning = None

def SetRunning(value):
    global GameRunning
    GameRunning = value
    pass

def SetWindowSize(value):
    global windowSize
    windowSize = numpy.array(value)
    pass

def Init():
    global windowSize, GameRunning
    windowSize = numpy.array([1600, 900])
    GameRunning = True
    pass