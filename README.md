# RobotAutonomoUNLP
Initial project of an autonomous robot led by a group of students from the Real-Time Systems course at UNLP (National University of La Plata).

## Overview
This project consists of a tri-wheeled robot that uses de ROS framwork to process scripts and move making geometric figures with its path, also implementing a control system so the movement is smooth and syncronized.

## Table of Contents

- [Getting Started](#getting-started)


## Getting Started

- [Connection Instructions](#connection-instructions)
- [Remote Access](#remote-access)
- [Robot Initialization](#robot-initialization)
- [Workspace](#workspace)

### Connection Instructions

For the first iteration of the project, the robot needs to be connected to two 220V power outlets, one using the power jack that is installed on a step down transformer, the second outlet is for the Raspberry Pi 4 that uses an USB C connector.

### Remote Access

Once all powered up, the robot will automatically connect to the univerity's wireless local area network.
To access it the user must be connected to the same Wi-Fi network.
<pre>
  SSID: alumnosInfo
  Password: Informatica2019
</pre>

You can now connect to the robot via ssh, for that you will need the robot ip address.
We used the 3rd party mobile app "Fing" to recognise the "Raspberry Pi" device and figure out the ip address.

With both previous steps done (Connect to UNLP Informatica Wi-Fi, and knowing device ip address), you can now access remotely via ssh.
On your pcs vsCode, you can use the "Connect to Host" feature. Or you can do this on your pcs terminal.
In either case, we recommend open 3 terminals and connect to the robot. If using vsCode, you can connect once and then instance more terminals from within.
This is for an easier robot initialization after the connection.

enter the following command:

```
$ ssh robotAutonomoUNLP@[IP ADDRESS]
```

After that you will be asked for a password, enter:
<pre>
  undertaker
</pre>

If its the first time you connect via ssh to the device, it will ask to trust it, please entre yes.

### Robot Initialization

Once inside the robot, you will be able to see the Linux terminal.
The 3 terminals previously asked for are one for the actual initialization (ROS Launch), one for running the robot (ROS Run), and one for an emergency stop (Emergency) in case its needed.

#### ROS Launch

To start the robot please run the command

```
  $ roslaunch locomotion_robot_pkg start.launch
```

### ROS Run

```
 rosrun locomotion_robot_pkg locomotion_receptor.py {movement: args} 
```

| Parameter                     | Description                                               |
|-------------------------------|-----------------------------------------------------------|
| `test`                        | Moves forward, then backwards, then turns left, then right|
| `line {length in cm}`         | Moves forward the ammount of cm specifie                  |
| `square {side lenght in cm}`  | Makes a square of side specified in cm as parameter       |


## Workspace

To start making your own code routines, the workspace is located in
<pre>
  ~/robotAutonomoUNLP/locomotion_ws/src/locomotion_robot_pkg/src/
</pre>

