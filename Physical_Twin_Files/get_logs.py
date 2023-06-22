from niryo_robot_python_ros_wrapper.ros_wrapper import *
import sys
import rospy
import time
from datetime import datetime

rospy.init_node('niryo_blockly_interpreted_code2')
n = NiryoRosWrapper()
rospy.timer.Rate(30)

prev_pos_list = n.get_joints()
tolerance = 0.01  # Adjust this value as needed
t1 = datetime.now()

def is_moved(current, previous, tolerance):
    return any(abs(c - p) > tolerance for c, p in zip(current, previous))

log_file = 'scenario_4_run_2.txt'  # name of the log file

try:
    while not rospy.is_shutdown():
        while True:
            rospy.sleep(0.06)
            current_pos_list = [round(num, 4) for num in n.get_joints()]
            if is_moved(current_pos_list, prev_pos_list, tolerance):  # Checking if position has changed
                t2 = datetime.now()
                log_line = str(current_pos_list) + ', ' + str((t2 - t1).microseconds/1000) + '\n'  # prepare line to be logged
                t1 = t2
                with open(log_file, 'a') as file:  # Change 'w' to 'a' for append mode
                    file.write(log_line)  # write the log line to file
                print(log_line)
                prev_pos_list = current_pos_list  # Updating the previous position

        print('Logs written to ' + log_file)

except KeyboardInterrupt:
    print('Keyboard interrupt detected, exiting...')
    print(rospy.is_shutdown())
    sys.exit()
