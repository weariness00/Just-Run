import os
os.chdir("D:/GItData/Just Run/Project")

import math
import numpy
from pico2d import *
from enum import Enum, auto

windowSize = numpy.array([1600, 900])
GameRunning = True

def SetRunning(value):
    global GameRunning
    GameRunning = value
    pass

def SetWindowSize(value):
    global windowSize
    windowSize = numpy.array(value)
    pass
