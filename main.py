#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# The scanable colors
POSSIBLE_COLORS = (Color.RED, Color.GREEN, Color.BLUE, Color.YELLOW)

# Init
brick.display.clear()
brick.sound.beep()

brick.display.text("Hallo Mape")

# sensors
touchSensor = TouchSensor(Port.S1)
colorSensor = ColorSensor(Port.S3)

#motors
testMotor1 = Motor(Port.A, Direction.CLOCKWISE)
testMotor1.reset_angle(0)

# until you stop the program.
while True:
    if touchSensor.pressed():
        color = colorSensor.color()
        brick.display.text(color)

        if color in POSSIBLE_COLORS:
            
            brick.sound.file(SoundFile.READY)

            if color == Color.BLUE:
                brick.sound.file(SoundFile.BLUE)
                testMotor1.run_target(500, 10)
            elif color == Color.GREEN:
                brick.sound.file(SoundFile.GREEN)
                testMotor1.run_target(500, 132)
            elif color == Color.YELLOW:
                brick.sound.file(SoundFile.YELLOW)
                testMotor1.run_target(500, 360)
            elif color == Color.RED:
                brick.sound.file(SoundFile.RED)
                testMotor1.run_target(500, 530)

        else:
            brick.sound.file(SoundFile.ERROR)