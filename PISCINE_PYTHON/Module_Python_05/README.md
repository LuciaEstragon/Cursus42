python3 -m flake8 . --exclude=ex2/my_data_processor.py


# Si creamos una instancia
proc = NumericProcessor()
# Esto extrae el nombre
name = proc.__class__.__name__

print(name)  # El resultado en consola será exactamente: "NumericProcessor"



# -> Resumen con analogía final
Pipeline = cadena de montaje de datos.
Procesadores = trabajadores en cada estación (heredan de DataProcessor).
Plugin = adaptador de salida (formato CSV, JSON...). No necesitan heredar, solo tener process_output.
Protocol = "contrato" que dice qué método debe tener un plugin.
Duck typing = "si tiene process_output, sirve como plugin".



### ¿Qué es un plugin? (ejemplo muy simple)
Un plugin es como un adaptador de enchufe. Si viajas a otro país, necesitas un adaptador para que tu móvil se conecte a la pared. 
Da igual la marca del adaptador; lo que importa es que tenga la forma correcta (clavija) y funcione.

En programación, un plugin es un componente que se puede conectar al sistema principal sin modificar el sistema. 
Solo tiene que cumplir con un contrato (una interfaz). Si cumple, el sistema lo acepta.

Ejemplo de plugin simple:
Imagina un programa que quiere saludar de diferentes maneras. Puedes tener plugins de saludo:

python
# El sistema principal espera que el plugin tenga un método 'saludar'
class Sistema:
    def usar_plugin(self, plugin):
        plugin.saludar()

# Plugin en español
class SaludoEspanol:
    def saludar(self):
        print("¡Hola!")

# Plugin en inglés
class SaludoIngles:
    def saludar(self):
        print("Hello!")


En el ejercicio, los plugins de exportación (CSVExportPlugin, JSONExportPlugin) deben tener el método process_output. Da igual su tipo; DataStream solo pide que tengan ese método.

### ¿Qué es un Protocol en Python?
Un Protocol es una forma de documentar qué métodos debe tener un plugin, pero no obliga a heredar. 
Es como un "contrato escrito" que dice: "para ser plugin de exportación, debes tener un método process_output que reciba una lista de tuplas y no devuelva nada".
 Cualquier clase que cumpla eso es válida.

Ejemplo simple de Protocol:

python
from typing import Protocol

class Saludador(Protocol):
    def saludar(self) -> None:   # El protocolo exige un método saludar
        pass

# No hereda de Saludador, pero cumple el protocolo porque tiene 'saludar'
class Perro:
    def saludar(self):
        print("Guau")

def funcion_que_usa_plugin(plugin: Saludador):
    plugin.saludar()

funcion_que_usa_plugin(Perro())  # Funciona, imprime "Guau"




Readme - Lucia


