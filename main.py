#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

import Move
import Pivot

# Write your program here
brick.sound.beep()
#Move.move(0, 80, 12, Stop.BRAKE)
#Pivot.pivotright(100, 90, Stop.BRAKE)
#Move.move_to_white (80, Port.S1, Stop.BRAKE)
#Move.move_to_black( 80, Port.S1, Stop.BRAKE) 
#Pivot.pivotleft (80, 135, Stop.BRAKE)
#Move.move_to_black (90, Port.S1, Stop.BRAKE)
Move.square()
#Move.follow_line(80, Port.S1, Stop.BRAKE)