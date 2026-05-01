# Baymax Architecture

## Overview

Baymax is a ROS 2 Jazzy robot with four main subsystems communicating over topics and services.

## Subsystems

| Package | Role |
|---|---|
| `arm` | Controls the robot arm joints and end-effector |
| `navigation` | Handles autonomous movement and path planning |
| `vision` | Processes camera feeds for perception |
| `pill_dispenser` | Manages medication dispensing hardware |
| `baymax_interfaces` | Shared message/service definitions (the inter-team contract) |

## Interface Contract

All cross-team communication goes through `baymax_interfaces`. Teams must not
depend directly on another team's package — only on `baymax_interfaces`.

## Building

```bash
cd ~/baymax
source /opt/ros/jazzy/setup.bash
colcon build
source install/setup.bash
```

## Running

```bash
ros2 launch launch/baymax.launch.py
```
