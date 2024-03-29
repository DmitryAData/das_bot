# Необходимые для работы библиотеки
import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
import xacro

# Функция генерирующая описание запуска
def generate_launch_description():

    # Переменная для хранения запроса на хранение синхронизации по времени
    use_sim_time = LaunchConfiguration('use_sim_time')

    # Получаем описание робота
    pkg_path = os.path.join(get_package_share_directory('das_bot')) # Ищем пакет
    xacro_file = os.path.join(pkg_path,'description','robot.urdf.xacro') # Указывваем на URDF файл в пакете 
    robot_description_config = xacro.process_file(xacro_file).toxml() # Помещаем обработанное с помощью xacro описание робота в файл

    # Создаем ноду для joint_state_publisher
    params = {'robot_description': robot_description_config, 'use_sim_time': use_sim_time} # Берем параметры из переменных
    node_robot_state_publisher = Node(package='robot_state_publisher', executable='robot_state_publisher', output='screen', parameters=[params]) # Создаем ноду

    # Запускаем
    return LaunchDescription([DeclareLaunchArgument('use_sim_time', default_value='false', description='Use sim time if true'), node_robot_state_publisher])