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

### Launchfiles

Para criar as launchfiles, execute os comandos:

```bash

mkdir launch

```

Em setup.py:

```bash

import os
from glob import glob
from setuptools import setup

package_name = 'my_package'

setup(
    # Other parameters ...
    data_files=[
        # ... Other data files
        # Include all launch files.
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*')))
    ]
)

```

```bash

colcon build

# Dependendo do que você quiser lançar:
# Lançador de mapeamento:
ros2 launch py_launch_example mapping_launch.py

# Lançador de navegação:
ros2 launch py_launch_example navigation_launch.py

```

As lauchfiles lançam os nós necessários para fazer o mapeamento e navegação, entretanto, quando tento rodá-lo, o seguinte erro aparece:

```bash
[ERROR] [launch]: Caught exception in launch (see debug for traceback): executable 'turtlebot3_world.launch.py' not found on the libexec directory '/home/hallzero/turtlebot3_ws/install/turtlebot3_gazebo/lib/turtlebot3_gazebo' 
```

### Vídeos

[Vídeo da mapeamento](https://youtu.be/WHxhn_I36Fk)

[Vídeo da navegação](https://youtu.be/2Frr23Gh8b8)

## Ponderada 2 - Criando um Chatbot simples




## Ponderada 3 - Chatbot com LLM: parte 1

Para baixar as bibliotecas necessárias, utilizaremos o comando abaixo na pasta root do projeto:

```bash
pip install -r requirements.txt
```

Navegue até a pasta llm:

```bash
cd ./src/llm
```

Utilizaremos o ollama para construção do modelo, utilizando o modelo dolphin2.2-mistral

Para criar o modelo, usamos o seguinte comando

```bash
ollama create security -f Modelfile
```

Para lançar a interface que conversa com o modelo, utilizamos:

```bash
gradio llm_interface.py
```

### Vídeos
🚧 WIP 🚧
