# Baymax

A ROS 2 Jazzy robot with autonomous navigation, computer vision, arm control, and medication dispensing.

## Subsystems

| Package | Description |
|---|---|
| `arm` | Robot arm joint control and end-effector |
| `navigation` | Autonomous movement and path planning |
| `vision` | Camera-based perception |
| `pill_dispenser` | Medication dispensing hardware |
| `baymax_interfaces` | Shared message and service definitions |

## Prerequisites

- ROS 2 Jazzy — [install guide](https://docs.ros.org/en/jazzy/Installation.html)
- colcon: `sudo apt install python3-colcon-common-extensions`

## Setup

```bash
git clone git@github.com:Betts6430/Baymax.git ~/baymax
cd ~/baymax
source /opt/ros/jazzy/setup.bash
colcon build --symlink-install
source install/setup.bash
```

Add these two `source` lines to your `~/.bashrc` so you don't need to run them every session.

## Running

```bash
# Launch all subsystems
ros2 launch launch/baymax.launch.py

# Run a single node (e.g. for testing)
ros2 run arm arm_node
```

## Useful Commands

```bash
ros2 node list          # see all running nodes
ros2 topic list         # see all active topics
ros2 topic echo /topic  # watch messages on a topic
rqt_graph               # visualise the node graph
```

## Repository Structure

```
baymax/
├── src/
│   ├── arm/                  # arm package
│   ├── navigation/           # navigation package
│   ├── vision/               # vision package
│   ├── pill_dispenser/       # pill dispenser package
│   └── interfaces/           # shared msgs and srvs (baymax_interfaces)
├── launch/                   # launch files
└── docs/                     # architecture docs and guides
```

Cross-team communication must go through `baymax_interfaces` — teams should not depend directly on each other's packages.
