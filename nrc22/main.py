#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import os, sys

# This program requires LEGO EV3 MicxroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
MotorA = Motor(Port.A)
MotorB = Motor(Port.B)
MotorC= Motor(Port.C)
MotorD = Motor(Port.D)
left_color = ColorSensor()
right_color = ColorSensor()
bottom_color = ColorSensor()
gyro_sensor = GyroSensor()


# Write your program here.

# PID General Controller

def PID(target, actual, kp, ki, kd):
    integral = 0
    error = target - actual
    previous = error
    derivative = 0
    result = 0
    while error != 0:
        error = target - actual
        integral += error
        derivative = error - previous
        result = (kp * error) + (ki * integral) + (kd * derivative)
        MotorA.run(result)
        MotorB.run(result)
        previous = error
        print(f"error is now {error}, changing speed to: {result}")
    print("error is now 0")
    
# starting algorithm


# the picking stuff up FUNCTION


# the savepeopleandpickstuffup algorithm

