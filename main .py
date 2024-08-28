#!/usr/bin/env pybricks-micropython

import random
from pybricks.ev3devices import ColorSensor, InfraredSensor, Motor
from pybricks.hubs import EV3Brick
from pybricks.parameters import Button, Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait
from pybricks.parameters import Stop
import pickle

# Constants
WHITE = 25
BLACK = 8
TURN_ANGLE = 2
DRIVE_SPEED = 20
ALPHA = 0.1  # Learning rate
EPSILON = 1  # Exploration rate
GAMMA = 0.9  # Discount factor
E=2.7321
TEMP=1000

# Initialize hardware components
ev3 = EV3Brick()
left_motor = Motor(Port.C)
right_motor = Motor(Port.B)
light_sensor = ColorSensor(Port.S1)
ir_sensor = InfraredSensor(Port.S4)
robot = DriveBase(left_motor, right_motor, wheel_diameter=40, axle_track=50)
direction = 'Forward'

