import os
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription, SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node



def generate_launch_description():

    # Directories
    pkg_ros_example = get_package_share_directory("isaac_ros_examples")
    # Paths
    pkg_ros_example_launch = PathJoinSubstitution([pkg_ros_example, "launch", "isaac_ros_examples.launch.py"])
    # Gazebo
    vslam = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([pkg_ros_example_launch]),
        launch_arguments=[
            ("launch_fragments", "visual_slam"),
            ("pub_frame_rate", "30.0"),
            ("base_frame", "zed2_camera_center"),
            ("camera_optical_frames", "['zed2_left_camera_optical_frame', 'zed2_right_camera_optical_frame']"),
            ("interface_specs_file", "/workspaces/isaac_ros-dev/isaac_ros_assets/isaac_ros_visual_slam/zed2_quickstart_interface_specs.json"),
        ]
    )

    # Create launch description and add actions
    ld = LaunchDescription()
    ld.add_action(vslam)
    return ld