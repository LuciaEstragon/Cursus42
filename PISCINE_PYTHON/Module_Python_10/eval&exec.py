"""
El contexto real donde eval() y exec() son útiles

1. Configuración dinámica desde archivos externos
Imagina que tienes un archivo de configuración con expresiones matemáticas:

Útil cuando: Los usuarios no-programadores necesitan definir fórmulas sin modificar el código.
"""

# config.txt
"ancho * alto / 2"

# En tu programa
with open("config.txt", "r") as f:
    formula = f.read()

ancho = 10
alto = 5
resultado = eval(formula)  # 10*5/2 = 25
print(resultado)  # 25

"""
2. Calculadoras o intérpretes embebidos

Útil cuando: Necesitas un entorno interactivo como el propio REPL de Python.
"""
def calculadora():
    while True:
        expr = input(">>> ")
        if expr == "salir":
            break
        try:
            print(eval(expr))
        except:
            print("Error")

# Uso:
# >>> 3 + 4 * 2  → 11
# >>> [x*2 for x in range(5)] → [0, 2, 4, 6, 8]

"""
3. Plantillas y generación de código

Útil cuando: Necesitas generar código repetitivo automáticamente.
"""
# Generar funciones dinámicamente
operaciones = {
    "suma": "a + b",
    "resta": "a - b",
    "multiplicacion": "a * b",
    "division": "a / b if b != 0 else 'Error'"
}

def crear_funcion(operacion, formula):
    codigo = f"""
def {operacion}(a, b):
    return {formula}
"""
    exec(codigo)
    return locals()[operacion]  # Recuperar la función creada

# Crear funciones en tiempo de ejecución
suma = crear_funcion("suma", "a + b")
print(suma(5, 3))  # 8

# ¡Incluso podrías crear 100 funciones con un patrón!

"""
4. Deserialización de estructuras de datos complejas

Nota: Para esto es mejor usar json o pickle, pero eval() puede ser útil en casos simples.
"""
# Guardar estructuras en formato texto
datos_guardados = "{'nombre': 'Ana', 'edades': [20, 25, 30]}"

# Recuperarlos
datos = eval(datos_guardados)
print(datos['nombre'])  # Ana
print(datos['edades'][1])  # 25

"""
5. Plugins y código cargado desde archivos externos

Útil cuando: Quieres permitir extensiones sin reiniciar la aplicación.
"""
# archivo_plugin.py
def procesar(dato):
    return dato * 2

# Programa principal
with open("archivo_plugin.py", "r") as f:
    codigo_plugin = f.read()

exec(codigo_plugin)  # Carga las funciones del plugin
print(procesar(10))  # 20 (la función ahora existe)


