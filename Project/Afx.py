import math
import numpy
from pico2d import *
from enum import Enum, auto
# from Transform import *
# from Collide import *
# from Object import *
# from Tile import *
# from EndlessTile import *
# from Player import *
# from Camera import *
# from Renderer import *

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
