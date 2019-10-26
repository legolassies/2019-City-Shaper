from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import Move 
left_motor = Motor(Port.C) 
right_motor = Motor(Port.B)

def pivotright (Power, Degrees, Brake):
    angle = Degrees * 2.8
    #right_motor.run_target(1, 0, Stop.BRAKE, False)
    left_motor.run_target(Power, angle, Brake, True)

def pivotleft (Power, Degrees, Brake):
    angle = Degrees * 2.8
    #left_motor.run_target(1, 0, Stop.BRAKE, False)
    right_motor.run_target(Power, angle, Brake, True)


