#Trabalho Matemática Discreta - Grafos 

Brincando com a biblioteca Python NetworkX
https://networkx.github.io

##GPS com Grafos

###Objetivo:
Ler o mapa no formato GML, oferecer as cidades disponíveis num menu onde o usuário seleciona a origem e o destino. O sistema processa e mostra as rotas possíveis entre as cidades.


###Instalar/Rodar:

***Pré-requisito:** Ter o GIT instalado na máquina.*
***Obs.:** Comandos do virtualenv compativeis com Linux/MAC se usar Windows dê uma pesquisada...*

Clonar o projeto git:
```shell
git clone git@bitbucket.org:robertsonweb/gps-grafos-python.git
```

Acessar o diretório:
```shell
cd gps-grafos-python
```

Criar a virtualenv:
```shell
virtualenv venv
```

Ativar a virtualenv:
```shell
source venv/bin/activate
```

Instalar as dependências da virtualenv:
```shell
pip install -r requirements.txt
```

Rodar o programa:
```shell
python main.py
```