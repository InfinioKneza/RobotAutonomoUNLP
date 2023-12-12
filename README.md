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
- [Taking the Robot Home](#taking-home)

### Connection Instructions
<a name="connection-instructions"></a>

For the first iteration of the project, the robot needs to be connected to two 220V power outlets, one using the power jack that is installed on a step down transformer, the second outlet is for the Raspberry Pi 4 that uses an USB C connector.

### Remote Access
<a name="remote-access"></a>

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
<a name="robot-initialization"></a>

Once inside the robot, to start making your own code routines or sending commands you must change directory to project workspace located at:

<pre>
  ~/robotAutonomoUNLP/locomotion_ws/src/locomotion_robot_pkg/src/
</pre>

The 3 terminals previously asked for are one for the actual initialization ([ROS Launch](#ros-launch)), one for running the robot ([ROS Run](#ros-run)), and one for an emergency stop ([Emergency](#ros-emergency)) in case its needed.
The 3 should all be on the project's workspace

#### ROS Launch
<a name="ros-launch"></a>

To start the robot please run the command. To reduce conflicts we recommend to wait at least 15 seconds before start running the robot (ROS Run) 

```
  $ roslaunch locomotion_robot_pkg start.launch
```

### ROS Run
<a name="ros-run"></a>

```
 $ rosrun locomotion_robot_pkg locomotion_receptor.py {movement: args} 
```

| Parameter                     | Description                                               |
|-------------------------------|-----------------------------------------------------------|
| `test`                        | Moves forward, then backwards, then turns left, then right|
| `line {length in cm}`         | Moves forward the ammount of cm specifie                  |
| `square {side lenght in cm}`  | Makes a square of side specified in cm as parameter       |

### Emergency
<a name="ros-emergency"></a>

```
 $ python3 emergency_stop.py 
```

## Taking the Robot Home
<a name="taking-home"></a>

In case any of the project participants need to take the robot home, and use it in their own Wi-Fi, the netplan configuration should be changed. Please read how to change this file and how YAML files should be written on.
