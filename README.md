# DigitalTwin_for_Cyber_Physical_Systems_with_Niryo
This repository is to compare the data logs from digital twin platform to real robo

# Physical Twin
- Niryo Ned robot
- ROS Melodic
- Scripts under `Physical_Twin_File/` folder

# Digital Twin
- Webots 2023a https://github.com/cyberbotics/webots/releases/tag/R2023a
- URDF model of Niryo Ned robot
- urdf and .py under `Digital_Twin_File/` folder

# Target Position

There are 4 Scenario for with seperate individual target position

Eg: Scenario 1
```
# Scenario 1
[
[0, 0, 0, 0, 0, 0],
[0.096, -0.592, 0.673, -1.738, -1.499, 0.003],
[-1.253, -0.592, -0.079, -0.054, -0.750, 0.003],
[2.495, 0.610, 0.074, 1.770, -1.441, 0.003],
[0.000, 0.500, -1.250, 0.000, -0.003, 0.003],
[0, 0, 0, 0, 0, 0]
],
```

# Log Files
Theses has logs of each scenarios for 5 iterations

eg:
'''[-0.0, -0.0, 0.0, 0.0, -0.0, 0.0] 56.456'''
explains
position of motor m1, m2, m3, m4, m5, m6 and at end 56.45 represents the 'Time difference' between previous logging line
