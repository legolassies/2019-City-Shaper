#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

left_motor = Motor( Port.B ) 
right_motor = Motor( Port.C )

def move( steering, power, inches, brake ):
    angle = 36*Inches 
    left_motor.run_target( power, angle, brake, False)    
    right_motor.run_target( power, angle, brake, True)    

def stop( brake ):
    left_motor.stop( brake )    
    right_motor.stop( brake )    

def move_forever( power ):
    left_motor.run( power )    
    right_motor.run( power )   

def move_to_black( power, port, brake ):
    move_forever( power )
    color_sensor=ColorSensor( port )
    print( color_sensor.reflection() )

    while color_sensor.reflection()>15:
        print(color_sensor.reflection())
        wait(0.1)
    stop(brake)
    brick.sound.beep()

def move_to_black_for_square( power, port1, port2, brake ):
    move_forever( power )
    light_sensor1=ColorSensor( port1 )
    light_sensor2=ColorSensor( port2 )
    print(str(light_sensor1.reflection())+ " " + str(light_sensor2.reflection()))

    while light_sensor1.reflection() > 15 and light_sensor2.reflection() > 15:
        print(str(light_sensor1.reflection())+ " " + str(light_sensor2.reflection()))
        wait(0.1)

    print(str(light_sensor1.reflection())+ " " + str(light_sensor2.reflection()))
    
    stop( brake )
    brick.sound.beep()

def move_to_white( power, port, brake ):
    move_forever( power )
    color_sensor=ColorSensor( port )
    print(color_sensor.reflection())

    while color_sensor.reflection()<90:
        print(color_sensor.reflection())
        wait(0.1)
    stop( brake )
    brick.sound.beep()

def square():
    left_sensor=ColorSensor( Port.S1 ) 
    right_sensor=ColorSensor( Port.S4 ) 
    move_to_black_for_square( 50, Port.S1, Port.S4, Stop.BRAKE )

def follow_line( power, port, brake ):
    #move, then check the color underneath the sensor.
    #If the color underneath the sensor is black, move forwards.
    #If the color is not black, turn right and check the color again.
    #Do the same for the left side of the robot.
    #If there is no black on either sides of the robot, then beep and stop.

    #Move, then check the color underneath the sensor.
    move_forever( power )
    while color_reflection <15:

        #If the color underneath the sensor is black, move forwards.
        move_forever( power )
        #print color_reflection

    #If the color is not black, turn right and check the color again.
    pivotright( power, degrees, brake )
    while color_reflection < 15:
        move_forever( power)
        #print color_reflection
    
    #Do the same for the left side of the robot.
    pivotleft( power, degrees, brake )
    while color_reflection < 15:
        move_forever( power )
        #print color_reflection

    #If there is no black on either sides of the robot, then beep and stop.
    brick.sound.beep()
    stop( brake ) 