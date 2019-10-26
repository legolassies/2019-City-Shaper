#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

left_motor = Motor(Port.B) 
right_motor = Motor(Port.C)

def move(Steering, Power, Inches, Brake):
    angle = 36*Inches 
    left_motor.run_target(Power, angle, Brake, False)    
    right_motor.run_target(Power, angle, Brake, True)    

def stop(Brake):
    left_motor.stop (Brake)    
    right_motor.stop (Brake)    

def move_forever(Power):
    left_motor.run(Power)    
    right_motor.run(Power)   

def move_to_black(Power, Port, Brake):
    move_forever(Power)
    color_sensor=ColorSensor(Port)
    print(color_sensor.reflection())

    while color_sensor.reflection()>15:
        print(color_sensor.reflection())
        wait(0.1)
    stop(Brake)
    brick.sound.beep()

def move_to_black_for_square(Power, Port1, Port2, Brake):
    move_forever(Power)
    light_sensor1=ColorSensor(Port1)
    light_sensor2=ColorSensor(Port2)
    print(str(light_sensor1.reflection())+ " " + str(light_sensor2.reflection()))

    while light_sensor1.reflection()>15 and light_sensor2.reflection()>15:
        print(str(light_sensor1.reflection())+ " " + str(light_sensor2.reflection()))
        wait(0.1)

    print(str(light_sensor1.reflection())+ " " + str(light_sensor2.reflection()))
    
    stop(Brake)
    brick.sound.beep()

   

def move_to_white(Power, Port, Brake):
    move_forever(Power)
    color_sensor=ColorSensor(Port)
    print(color_sensor.reflection())

    while color_sensor.reflection()<90:
        print(color_sensor.reflection())
        wait(0.1)
    stop(Brake)
    brick.sound.beep()

def square():
    left_sensor=ColorSensor(Port.S1) 
    right_sensor=ColorSensor(Port.S4) 
    move_to_black_for_square(50,Port.S1,Port.S4,Stop.BRAKE)

def follow_line(Power, Port, Brake):
    #move, then check the color underneath the sensor.
    #If the color underneath the sensor is black, move forwards.
    #If the color is not black, turn right and check the color again.
    #Do the same for the left side of the robot.
    #If there is no black on either sides of the robot, then beep and stop.

    #Move, then check the color underneath the sensor.
    move_forever(Power)
    while color_reflection <15:

        #If the color underneath the sensor is black, move forwards.
        move_forever(Power)
        #print color_reflection

    #If the color is not black, turn right and check the color again.
    pivotright (Power, Degrees, Brake)
    while color_reflection <15:
        move_forever(Power)
        #print color_reflection
    
    #Do the same for the left side of the robot.
    pivotleft (Power, Degrees, Brake)
    while color_reflection <15:
        move_forever(Power)
        #print color_reflection

    #If there is no black on either sides of the robot, then beep and stop.
    brick.sound.beep()
    stop(Brake) 