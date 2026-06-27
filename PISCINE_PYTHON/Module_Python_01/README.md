README PYTHON

Comprobaciones: 
python3 -m mypy . 
python3 -m flake8 .
python3 -m mypy --strict .

Modo de ejecutar:
1. normal
python3 ft_garden_intro.py
2. con shebang y permisos de ejecucion (#!/usr/bin/env python3)
chmod +x ft_garden_intro.py 
./ft_garden_intro.py 


Python 00
ex00 - ex05 -> solo son para manejar print e input
ex06 -> recursividad e iteratividad
ex07 -> aprender a utilizar hints : mypy

Python 01
ex00 -> aprender a hacer un main en python
	USO DE: #!/usr/bin/env python3 		--> pasa de ser un fichero a un ejecutable
		if __name__ == "__main__":	--> main de pruebas, SOLO PARA MI
			Si usas el script, Python le asigna al nombre del archivo una variable especial 
			llamada __name__ con el valor "__main__". Si otro programador intenta importar 
			tu archivo (import ft_garden_intro) para usar una función tuya, Python no 
			ejecutará lo que esté dentro de ese if.
			
ex01 -> primera clase: 3 atributos, un metodo, un main

ex02 -> herencias - crear un for que vaya incrementando un metodo heredado

ex03 -> herencias usando el constructor para inicializar al padre con super()
	diferencias con el ejercicio anterior

ex04 -> settes y gettes

ex05 -> encapsulamiento y polimorfismo
	1- El encapsulamiento es el mecanismo que oculta los detalles internos de una clase y protege los
	   datos para que no sean modificados directamente desde fuera. Solo se accede a ellos a través de 
	   métodos controlados. (getes y setes)
				Nivel				Sintaxis	Acceso
				Público				self.name	Accesible desde cualquier lado
				Protegido (convención)		self._name	"No toques esto" - pero se puede
				Privado	(name mangling)		self.__name	Python oculta el nombre (no es 100% privado)
	2- El polimorfismo (del griego: "muchas formas") permite que objetos de diferentes clases respondan 
	   al mismo mensaje (método) de forma distinta.
		Ejemplo: el método hacer_sonido():
			Un Perro → "Guau"
			Un Gato → "Miau"
			Una Vaca → "Muu"

		# ✅ Misma llamada, resultados diferentes (polimorfismo)
		print(plant.show())  
		# Generic: 10.0cm, 5 days old

		print(flower.show())
		# Rose: 15.0cm, 10 days old
		# Color: red

		print(tree.show())
		# Oak: 200.0cm, 365 days old
		# Trunk diameter: 5.0cm

		print(seed.show())
		# Sunflower: 80.0cm, 45 days old
		# Color: yellow
		# Seeds: 0

ex06 -> métodos estáticos, métodos de clase, clases anidadas
		@staticmethod: Es una función que vive dentro de la clase pero no necesita acceder 
		a self (la instancia). Es como una herramienta de utilidad.

		@classmethod: Recibe la clase (cls) en lugar de la instancia (self). Es ideal para 
		crear "fábricas" de objetos (como la planta anónima).

		Clase Anidada: Es una clase definida dentro de otra. Se usa aquí para agrupar los 
		contadores de estadísticas de forma organizada



DIFERENCIA DE CONCEPTOS APRENDIDOS . EJERCICIO 2, 3 y 5
Tabla comparativa: Ejercicios A, B y C
Concepto				Ejercicio 3			Ejercicio 5					Ejercicio 2
Herencia				✓				✓						✓
super().__init__()			✓				✓						✗ (no usa explícitamente por herencia directa sin atributos nuevos)
Sobrescritura de métodos		✓ (grow)			✓ (show)					✓ (grow)
Extensión de métodos			✗				✓ (con super().show())				✗
Atributos protegidos			✗				✓ (_height, _age)				✗
Atributos privados			✗				✗						✗
Atributos específicos de subclase	✗				✓ (color, trunk_diameter, harvest_season)	✗
Métodos exclusivos de subclase		✗				✓ (bloom(), produce_shade(), grow_and_age())	✗
Polimorfismo				✓ (básico: diferentes tasas)	✓ (avanzado: comportamiento + atributos)	✓ (básico)
Método mágico __str__			✗				✗						✓
Uso de print(objeto)			✗				✗						✓
Simulación temporal			✗ (solo instanciación)		✗ (excepto grow_and_age)			✓ (bucle de 7 días)
Estado interno cambiante		✗				✓ (is_blooming, nutritional_value)		✗
Seguimiento del crecimiento		✗				✗						✓ (initial_height comparada con final)
Formato de altura decimal		Sin formato fijo		:.1f						:.1f (en __str__)
Colección de plantas			✓ (list[Plant])			✗ (instancias sueltas)				✗ (una sola planta)
Fábrica de plantas			✓ (plant_factory)		✗						✗
Simulación día a día			✗	✗	✓ (muestra cada día)
Nombre pasado por parámetro		✗ (hardcodeado en cada clase)	✓						✓
Cantidad de subclases			5 (Rose,Oak,Cactus,flower,Fern)	3 (Flower, Tree, Vegetable)			3 (Rose, Bamboo, Cactus)




'''
ejercicio 0
Crea un programa que se ejecute cuando se ejecute directamente usando python3 ft_garden_intro.py.
Utiliza el patrón especial if __name__ == "__main__":.
Guarda la siguiente información de la planta en variables simples: nombre, altura y edad.
Muestra la información de la planta usando print().
Imita el ejemplo de salida que se muestra abajo; no habrá una comprobación estricta de la salida durante la evaluación.
'''
explicar que es el shebang #! --> si le doy permisos de ejecucion pasamos de porder ejecutar asi python3 a asi ./
if __name__ == "__main__":   --> solo se ejecuta si corro este archivo. (./this.py) si importase a otro lado esto no se ejecuta. Sirve para hacer mains de prueba



'''
ejercicio 1
Debes crear una clase Planta que sirva como modelo para cualquier planta, en lugar de manejar cada una individualmente. Todas las plantas serán descritas usando los mismos atributos, o características, enumerados anteriormente: nombre, altura y edad. Para cada planta, se instanciará la clase, luego los atributos se establecerán con sus valores específicos.
'''
explicar concepto de clase - poo 



'''
ejercicio 2
Reutiliza la clase Planta del Ejercicio 1.
• Las plantas deben poder crecer() y envejecer() por sí solas (es decir, estos serán métodos
de la clase).
• Simula una semana de crecimiento para una planta y luego accede a los datos de la clase para obtener la
altura final y mostrar el aumento total semanal.
• Considera cómo debería cambiar la planta con el tiempo al usar los métodos crecer() y envejecer().
Las diferentes plantas pueden evolucionar de manera diferente.
'''
conceto de herencia - poo - defino la funcion grow solo en sus hijos (pass)
aqui explicar mi error: __init__ y __str__ : metodos dunder o metodo magico : son llamados automaticamente para ayudar a que tu objeto haga cosas 
(init es el constructor; el str cobierte el objeto a un string - definido por ti-)
def __str__(self):
  return ---string---
print(my_plant)




'''
ejercicio 3
• Las plantas deben crearse directamente con su información inicial (nombre, altura inicial, edad inicial).
• Cada planta debe estar lista para usarse inmediatamente después de su creación (por ejemplo, si se desea hacerla crecer).
• Crea al menos 5 plantas diferentes con características variadas.
• Muestra todas las plantas creadas de forma organizada.
'''
herencias, polimorfismo.. cada hija es independiente
# creo una lista con todos mis objetos para luego con un for recorrer la lista



'''
ejercicio 4
Mejora tu clase Planta para proteger sus datos de la corrupción.
• Proporciona métodos controlados para modificar los datos de la planta: `set_height()`, `set_age()`.
• Proporciona métodos seguros para acceder a los datos de la planta: `get_height()`, `get_age()`.
• Asegúrate de que la altura de la planta no pueda ser negativa mediante validación.
• Asegúrate de que la edad de la planta no pueda ser negativa mediante validación.
• Imprime mensajes de error de la clase cuando se proporcionen valores no válidos, dejando los datos sin modificar o creando la planta con valores predeterminados.
• Usa encapsulación: evita que los atributos de tu clase se utilicen directamente mediante la convención `protected` (no la descomposición).
'''

Niveles de acceso en Python (por convención)
Convención	Significado	Acceso desde fuera
self.name	Público	✅ Se puede leer y modificar
self._name	Protegido	⚠️ Se PUEDE pero NO DEBE (es convención)
self.__name	Privado	❌ Name mangling (difícil acceder)


# Crear una planta
mi_rosa = Rose(25.0, 30)

# ==========================================
# ACCESO PÚBLICO (original - SÍ funciona)
# ==========================================
print(mi_rosa.name)      # ✅ Funciona (pero es mala práctica)
mi_rosa.height = 100     # ✅ Funciona (pero sin validación)
mi_rosa.age_days = -5    # ✅ Funciona (edad negativa válida - PROBLEMA)

# ==========================================
# ACCESO PROTEGIDO (con _ - SÍ funciona, pero es mala práctica)
# ==========================================
# Python NO impide el acceso, solo es una convención
print(mi_rosa._name)      # ⚠️ FUNCIONA (pero no deberías)
mi_rosa._height = -999    # ⚠️ FUNCIONA (rompe validación)

# ==========================================
# ACCESO PRIVADO (con __ - NO funciona fácilmente)
# ==========================================
# Si usaras self.__name:
print(mi_rosa.__name)     # ❌ AttributeError: 'Rose' object has no attribute '__name'
mi_rosa.__height = 50     # ❌ No modifica el atributo real (crea uno nuevo)

# Para acceder a privados (name mangling - NO recomendado):
print(mi_rosa._Plant__name)  # ⚠️ Funciona pero es horrible

# ==========================================
# USANDO GETTERS (funciona bien - RECOMENDADO)
# ==========================================
print(mi_rosa.get_name())     # ✅ Funciona
print(mi_rosa.get_height())   # ✅ Funciona

# ==========================================
# USANDO SETTERS (funciona con validación - RECOMENDADO)
# ==========================================
mi_rosa.set_height(30)        # ✅ Funciona y valida
mi_rosa.set_height(-10)       # ✅ No cambia, muestra error
mi_rosa.set_age(-5)           # ✅ No cambia, muestra error


'''
ejercicio 5
• Comience con la clase Planta del ejercicio anterior, que contiene las características comunes (nombre, altura y edad).
• Cree tipos especializados: Flor, Árbol y Vegetal.
• Cada tipo especializado debe heredar las características básicas de la planta.
• La Flor necesita: un atributo de color y la capacidad de florecer.
• El Árbol necesita: un atributo de diámetro del tronco y la capacidad de producir sombra.
• El Vegetal necesita: un atributo de temporada de cosecha y un atributo de valor nutricional.
• Al crear plantas especializadas, llame a los métodos de la clase padre desde dentro de su nueva clase usando `super()`. Se puede aplicar a cualquier método, incluido `__init__()`.
• Una llamada a `show()` en una clase especializada debe imprimir la salida estándar de la Planta y las características adicionales de su planta especializada. Su método puede reutilizar el código existente en la clase padre.

• Cree al menos una instancia de cada tipo de planta; haga que la flor florezca; haga que el valor nutricional comience en 0 y aumente cuando se llamen los métodos `age()` y `grow()` del Vegetal. 17
Cultivo de código en sistemas de jardinería orientados a objetos
• Evitar duplicar el código común de las plantas en diferentes tipos especializados.

• No es necesario validar los nuevos atributos en las tres nuevas clases.
'''




		
'''
EJERCICIO 6
Crear un método estático en Plant que compruebe si una edad es mayor de un año
Crear un método de clase en Plant que cree una planta "anónima"
Crear clase Seed que hereda de Flower, con contador de semillas
Cada planta tiene un sistema interno (clase anidada) para estadísticas
Trees necesitan estadística extra (llamadas a produce_shade)
Función independiente que muestre estadísticas de cualquier planta
'''
