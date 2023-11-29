# ponderadas-m8

## Ponderada 2 - Implementação de SLAM

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

## Ponderada 3 - Criando um Chatbot simples

Para rodar o chatbot, clone o repositório do projeto e navegue até a pasta chatbot e rode o programa:

```bash

git clone https://github.com/HallZero/ponderadas-m8.git

cd src/chatbot/chatbot

python chatbot.py
```
O chatbot funciona com um regex simples, que pega palavras chaves

### Vídeos
[Vídeo da implementação do chatbot com regex](https://youtu.be/LfekA_juCEo)


## Ponderada 4 - Chatbot com LLM: parte 1

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
ollama create security -f modelfile
```

Para lançar a interface que conversa com o modelo, utilizamos:

```bash
gradio llm_interface.py
```

### Vídeos
Original -> (Ollama e gradio (10+min without response))[https://youtu.be/yFhn2YFJ3rE]
Alternativa (Mesmo com o streaming, a reposta era lenta) -> (Ollama e gradio com streaming)[https://youtu.be/WGrk6reJUK0]

## Ponderada 5 - Construção de um chatbot com LLM e RAG
Para a utilização do modelo juntamente com o RAG, foi criado um arquivo .txt a partir do site da [Deakin university](https://www.deakin.edu.au/students/study-support/faculties/sebe/abe/workshop/rules-safety).

Vá até a pasta llm e rode o arquivo:

```bash
python rag.py
```

Entendendo o arquivo:

1. Primeiro, lemos o documento através do TextLoader
2. Em seguida, separamos o documento em chunks através do CharacterTextSplitter, que divide chunks de até 100 caracteres.
3. Embeddings são geradas para cada chunk do documento utilizando o modelo all-MiniLM-L6-v2, que depois são armazenados no Chroma
4. Criamos então um template de prompt
5. Carregamos o Ollama com o modelo e criamos um chain processing

### Vídeos


## Ponderada 6 - Perceptron e portas lógicas

### Implementação do Perceptron e Portas Lógicas

O código para a implementação do Perceptron e portas lógicas está presente nos arquivos `perceptron.py` e `logic_ports.py`. Siga as instruções abaixo para executar o sistema.

#### Passos para Executar o Perceptron e Portas Lógicas

1. Clone este repositório:

   ```bash
   git clone https://github.com/seu-usuario/ponderadas-m8.git
   cd ponderadas-m8

2. Certifique-se de ter Python instalado. Se não, baixe e instale o Python.
3. Instale as dependências:
```bash
pip install numpy
```
3. Execute o código normalmente:
```bash
python perceptron.py
```

O script demonstra o treinamento do perceptron para reproduzir o comportamento das portas lógicas AND, OR e XOR.

Observação: O perceptron é um modelo simples de rede neural que é eficaz para resolver problemas linearmente separáveis. Ele opera realizando uma combinação linear das entradas ponderadas pelos pesos e, em seguida, aplicando uma função de ativação para produzir a saída. No entanto, o perceptron tem limitações quando se trata de resolver problemas não lineares, como o caso da porta lógica XOR. Ao tentar treinar um perceptron para a porta XOR, o algoritmo de treinamento não consegue encontrar um conjunto de pesos e bias que produza a saída correta para todas as entradas. Isso ocorre porque a função de ativação do perceptron é uma função degrau, que é linear, e, portanto, não é adequada para resolver problemas não lineares.

### Vídeos
[Vídeo da implementação do perceptron com portas lógicas](https://youtu.be/NNUY2_luYzU)