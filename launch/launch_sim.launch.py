# Необходимые для работы библиотеки
import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

# Функция генерирующая описание запуска
def generate_launch_description():

    # Сохраняем имя пакета
    package_name='das_bot'

    # Поолучаем описание робота из лаунч файла
    rsp = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory(package_name),'launch','rsp.launch.py'
            )]), launch_arguments={'use_sim_time': 'true'}.items())

    # Получаем файлы запуска Gazebo
    gazebo = IncludeLaunchDescription(PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')]))
    
    # Создаем робота в симуляции
    spawn_entity = Node(package='gazebo_ros', executable='spawn_entity.py',
                        arguments=['-topic', 'robot_description',
                                   '-entity', 'das_bot'],
                        output='screen')

    # Запускаем
    return LaunchDescription([
        rsp,
        gazebo,
        spawn_entity
    ])