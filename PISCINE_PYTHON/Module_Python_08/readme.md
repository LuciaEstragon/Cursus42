__ se permiten errores de flake8 y mypy __

## EX1

1) Comprobar si estoy en entorno virtual
>./construct.py

Mi programa devuelve esta ruta:
/usr/bin/python3
que es la misma que si pregunto:
which python3

Nota 1:
#!/usr/bin/python3ma y #!/usr/bin/env python3
#!/usr/bin/env python3  --> esto busca primero en env si no lo encuentra o no lo conoce, va a buscar fuera.

>man env
>env
 -- el PATH de env buscara el ejecutable python
 PATH=/home/lestrada/bin:/home/lestrada/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/lestrada/.vscode/extensions/ms-python.debugpy-2026.6.0-linux-x64/bundled/scripts/noConfigScripts

Puedo usar python desde la consola metiendome a la ruta que me mando mi programa:
>/usr/bin/python3
o metiendome directamente por el comando env y completando la ruta a python3.
>env python3
Python 3.10.12 (main, Mar  3 2026, 11:56:32) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
Ctrl click to launch VS Code Native REPL


2) Crear entorno virtual y comprobar si estoy dentro
> sudo apt install python3-venv     # 1. herramienta para crear los env en python
> python3 -m venv my_name_env       # 2. implementar/crear/poner en marcha el env 
NOTA: > ls # se ha creado una carpeta con todo lo necesario ara en env python
> source my_name_env/bin/activate   # 3. activar env para qu cojas de aqui las dependencias
> deactivate

antes de desactivar lo pruebo
>./construct.py

Nota 2:
pip3 vs venv
pip3 es un administrador de paquetes que se utiliza para instalar y administrar Python bibliotecas, mientras que venv crea entornos aislados donde se almacenan estas bibliotecas

Nota 3:
sys : modulo o herramienta del sistema para comunicarte con el interprete (con la comutadora)
sys lee los PATH o Rutas


## EX2
> ./loading.py  
 me responde que no tengo pandas y no se que instalados

1. instalar las dependencias con pip
 creo un entorno virtual e instalo esas dependencias con requirements.txt
> python3 -m venv my_env
> python3 -m venv my_env
> pip install -r requirements.txt
> ./loading.py   # ahora si esta todo instalad y sale el matrix_analisis.png
Nota: > pip uninstall paquete

2. instalar las dependencias con poetry
> curl -sSL https://install.python-poetry.org | python3 -
> poetry --version   # me aseguro de que esta instalado
> export PATH="$HOME/.local/bin:$PATH"  # para incluir el poetry en el PATH de la ruta de python
> source ~/.zshrc

ya esta todo listo
> poetry install  # esto implementa el entorno virtual (env)
Para ejecutar comandos dentro el entorno virtual tendremos que añadir el prefijo de "poetry run" a todo lo que ejecutemos:
> poetry run python3 loading.py

Poetry es un gestor de dependencias, y pip un instalador de paquetes
Poetry crea una estructura con env y pip no, lo tienes que crear tu
mi-proyecto
├── .venv/
├── poetry.lock
├── poetry.toml
└── pyproject.toml


## EX3
Cargar variables de entorno desde `python-dotenv`.
> pip3 install python-dotenv   # para instalarlo en el ordenador
> ./oracle.py
> cp .env.example .env  # creo un entorno virtual que tenga lo que necesito


**Sobrescritura con variables de entorno:**
> MATRIX_MODE=production API_KEY=secret123 python3 oracle.py
Debería usar las variables de entorno en lugar del archivo .env


Teoria:
Las *variables de entorno* son pares de clave-valor que se configuran en el entorno del sistema operativo en el que se está ejecutando un programa. Estas variables proporcionan una manera de configurar el comportamiento de las aplicaciones sin necesidad de modificar el código fuente.
Las variables de entorno se utilizan comúnmente en aplicaciones para las siguientes casuísticas comunes:
    - Configurar conexiones a bases de datos.
    - Definir claves y secretos de API.
    - Configurar parámetros específicos del entorno (p.ej., modo de depuración).
    - Definir rutas y directorios importantes.


*python-dotenv* es una biblioteca para Python que te permite cargar variables de entorno desde un archivo .env a tu entorno de ejecución. Esto es útil para mantener tus configuraciones y credenciales fuera del código fuente.
