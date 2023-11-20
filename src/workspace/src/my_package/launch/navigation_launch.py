# navigation_launch.py

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Launch Gazebo with TurtleBot3 world
        Node(
            package='turtlebot3_gazebo',
            executable='turtlebot3_world.launch.py',
        ),
        # Launch Navigation2 with the saved map
        Node(
            package='turtlebot3_navigation2',
            executable='navigation2.launch.py',
            parameters=[{'use_sim_time': True}],
            arguments=['map:=~/Documents/Maps/my-map.yaml'],
        ),
    ])
