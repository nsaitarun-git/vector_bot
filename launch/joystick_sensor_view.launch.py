import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription,TimerAction
import time
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import ExecuteProcess



def generate_launch_description():


    # Include the robot_state_publisher launch file, provided by our own package. Force sim time to be enabled
    # !!! MAKE SURE YOU SET THE PACKAGE NAME CORRECTLY !!!

    package_name='vector_bot' #<--- CHANGE ME

    joystick = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory(package_name),'launch','joystick.launch.py'
                )]), launch_arguments={'use_sim_time': 'false'}.items()
    )

    rviz = ExecuteProcess(
            cmd=['rviz2'],
            output = "screen",
        )

    rqt_image_view = ExecuteProcess(
            cmd=['rqt'],
            output = "screen", 
        )

    

    # Launch them all!
    return LaunchDescription([
        joystick,
        rqt_image_view,
        rviz,
    ])
