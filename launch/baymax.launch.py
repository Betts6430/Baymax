from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        # Add nodes here as they are implemented, e.g.:
        # Node(
        #     package='arm',
        #     executable='arm_node',
        #     name='arm',
        # ),
        # Node(
        #     package='navigation',
        #     executable='nav_node',
        #     name='navigation',
        # ),
        # Node(
        #     package='vision',
        #     executable='vision_node',
        #     name='vision',
        # ),
        # Node(
        #     package='pill_dispenser',
        #     executable='dispenser_node',
        #     name='pill_dispenser',
        # ),
    ])
