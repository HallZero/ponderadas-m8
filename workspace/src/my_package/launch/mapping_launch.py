# mapping_launch.py

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Launch Gazebo with TurtleBot3 world
        Node(
            package='turtlebot3_gazebo',
            executable='turtlebot3_world.launch.py',
        ),
        # Run teleop for manual control
        Node(
            package='turtlebot3_teleop',
            executable='teleop_keyboard',
        ),
        # Launch Cartographer for mapping
        Node(
            package='turtlebot3_cartographer',
            executable='cartographer.launch.py',
            parameters=[{'use_sim_time': True}],
        ),
        # Save the map
        Node(
            package='nav2_map_saver',
            executable='map_saver_cli',
            arguments=['-f', '~/Documents/Maps/my-map'],
        ),
    ])
