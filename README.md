# ponderadas-m8

## Ponderada 1 - Implementação de SLAM

Pré-requisitos - ROS2

Para iniciar a rotina de mapeamento

```bash

ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py

ros2 run turtlebot3_teleop teleop_keyboard

ros2 launch turtlebot3_cartographer cartographer.launch.py use_sim_time:=True 

```

Para salvar o mapa

```bash
ros2 run nav2_map_saver map_saver_cli -f /home/hallzero/mapa
```

```bash

ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py

ros2 launch turtlebot3_navigation2 navigation2.launch.py use_sim_time:=True map:=/home/hallzero/mapa.yaml

```

## Launchfiles
As lauchfiles lançam os nós necessários para fazer o mapeamento e navegação

[Vídeo da mapeamento](https://youtu.be/WHxhn_I36Fk)

[Vídeo da navegação](https://youtu.be/2Frr23Gh8b8)



