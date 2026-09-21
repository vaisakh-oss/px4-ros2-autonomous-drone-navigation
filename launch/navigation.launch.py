# =================================================================
# ROS 2 DEPLOYMENT LAUNCH FRAMEWORK
# Programmed by: Vaisakh TV (USN: ENG24RA1004)
# Target: Automating drone node instantiation & parameter tracking
# =================================================================

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # Fetch parameters file mapping path
    pkg_share = get_package_share_directory('px4_ros2_drone_nav')
    params_file = os.path.join(pkg_share, 'params.yaml')

    return LaunchDescription([
        # Initialize the core drone navigation execution node
        Node(
            package='px4_ros2_drone_nav',
            executable='drone_nav_node',
            name='drone_nav_node',
            parameters=[params_file],
            output='screen',
            emulate_tty=True
        )
    ])
