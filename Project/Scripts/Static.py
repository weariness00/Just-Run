import numpy
import time
windowSize = None
GameRunning = None
Start_Time = None

def SetRunning(value):
    global GameRunning
    GameRunning = value
    pass

def SetWindowSize(value):
    global windowSize
    windowSize = numpy.array(value)
    pass

def Distance(myDot, otherDot):
    return (
        ((myDot[0] - otherDot[0]) ** 2) +
        ((myDot[1] - otherDot[1]) ** 2)
    ) ** 0.5  # fast sqrt

def SetStartTime():
    global Start_Time
    Start_Time = time.time()
    pass

def GetStartTime():
    global Start_Time
    return Start_Time

def FrameTime():
    frameTime = time.time() - GetStartTime()
    return float(frameTime)

def SetPngName(default, name):
    png = default + name + ".png"
    return png
    pass

def Init():
    global windowSize, GameRunning
    windowSize = numpy.array([1600, 900])
    GameRunning = True
    pass