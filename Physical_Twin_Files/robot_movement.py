#!/usr/bin/env python

from niryo_robot_python_ros_wrapper import *
import rospy
import argparse

# Parsing command line argument for scenario
parser = argparse.ArgumentParser(description='Choose a scenario for the robot movement.')
parser.add_argument('scenario', type=int, choices=range(1, 6),
                    help='an integer for the scenario (1-5)')
args = parser.parse_args()
scenario = args.scenario

# Initializing ROS node
rospy.init_node('niryo_ned_example_python_ros_wrapper')

n = NiryoRosWrapper()
n.calibrate_auto()
n.set_arm_max_velocity(50)

def move_to_position(scenario_list):
    for position in scenario_list:
        m1, m2, m3, m4, m5, m6 = position
        n.move_joints(m1,m2,m3,m4,m5,m6)

# Scenarios are lists of lists
scenarios = [
    # Scenario 1
    [
        [0, 0, 0, 0, 0, 0],
        [0.096, -0.592, 0.673, -1.738, -1.499, 0.003],
        [-1.253, -0.592, -0.079, -0.054, -0.750, 0.003],
        [2.495, 0.610, 0.074, 1.770, -1.441, 0.003],
        [0.000, 0.500, -1.250, 0.000, -0.003, 0.003],
        [0, 0, 0, 0, 0, 0]
    ],

    # Scenario 2
    [
        [0, 0, 0, 0, 0, 0],
        [0.00, 0.50, -1.25, 0.00, 0.00, 0.00],
        [0.995, -0.244, 1.0, 0.000, 0.000, -0.007],
        [0.096, -0.592, 0.673, -1.738, -1.499, 0.003],
        [0.000, 0.500, -1.250, 0.000, -0.003, 0.003],
        [0, 0, 0, 0, 0, 0]
    ],

    # Scenario 3
    [
        [0.00, 0.50, -1.25, 0.00, 0.00, 0.00],
        [0, 0, 0, 0, 0, 0],
        [1.253, 0.592, -0.079, -0.054, -0.750, 0.003],
        [0.096, -0.592, 0.673, -1.4, -1.499, 0.003],
        [0.90, 0.5, 0.5, -1.56, 0.0, 0.0],
        [0.000, 0.500, -1.250, 0.000, -0.003, 0.003],
        [0.00, 0.50, -1.25, 0.00, 0.00, 0.00]
    ],

    # Scenario 4
    [
        [0.995, -0.244, 1.0, 0.000, 0.000, -0.007],
        [2.495, 0.610, 0.074, 1.770, -1.441, 0.003],
        [0.000, 0.500, -1.250, 0.000, -0.003, 0.003],
        [-1.253,-0.5,-0.079,-0.054,-0.750,0.003],
        [0.00, 0.20, 0.00, -0.02, -1.4, -0.01],
        [0.096,-0.3,0.673, -1.738, -1.3, 0.003]

    ]
]

try:
    # Select the chosen scenario from the list and execute it
    move_to_position(scenarios[scenario-1])

finally:
    # After performing all movements, disable learning mode
    n.set_learning_mode(False)
    print("Learning mode disabled, exiting script.")
