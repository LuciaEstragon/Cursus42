## Programacion funcional - funciones de orden superior (o funciones de primera clase)

Lambda, Decoradores, Guardián del Alcance,

Las funciones en python pueden ser pasadas, almacenadas en variables y transformadas como cualquier otro dato. Patrones de programación funcional.

Resumen:
- **Ejercicio 0: Sanctum Lambda**
  - Domina las funciones anónimas y las expresiones lambda.
- **Ejercicio 1: Reino Superior**
  - Descubre el poder de las funciones de orden superior.
- **Ejercicio 2: Profundidades de la Memoria**
  - Comprende el alcance léxico y los closures.
- **Ejercicio 3: Biblioteca Ancestral**
  - Explora los tesoros del módulo functools.
- **Ejercicio 4: Torre del Maestro**
  - Crea poderosos decoradores y métodos de clase.

Prohibido:
- Bibliotecas externas (no `pip install`)
- Operaciones de E/S de archivos (concéntrate en el procesamiento en memoria)
- Algoritmos complejos (mantén el enfoque en los patrones funcionales)
- Usar `eval()` o `exec()`
- Variables globales (abrazar la pureza funcional cuando sea posible)


Python es un lenguaje interpretado (más precisamente, tiene una etapa de compilación a bytecode que ocurre en tiempo de ejecución). Cuando ejecutas un script Python:
  - El intérprete compila tu código a bytecode (.pyc)
  - La máquina virtual de Python ejecuta ese bytecode

eval()	Evaluar expresión	eval("3*4") → 12
exec()	Ejecutar bloque de código	exec("print('Hola')")

## EX0
Las funciones lambda (también llamadas funciones anónimas) son funciones pequeñas, de una sola línea, sin nombre, que se definen en el lugar donde se van a usar.
    lambda argumentos: expresión

# Función tradicional
def sumar_tradicional(a, b):
    return a + b

# Función lambda equivalente
sumar_lambda = lambda a, b: a + b

# Ambas se usan igual
print(sumar_tradicional(3, 5))  # 8
print(sumar_lambda(3, 5))       # 8


# Requisitos de Implementación

- `artifact_sorter(artifacts)` - Ordenar artefactos mágicos:
  - Usa `sorted()` con una lambda para ordenar por nivel de 'power' (descendente)
  - Cada artefacto es un dict: `{'name': str, 'power': int, 'type': str}`
  - Devuelve la lista ordenada

- `power_filter(mages, min_power)` - Filtrar magos por poder:
  - Usa `filter()` con una lambda para encontrar magos con poder >= min_power
  - Cada mago es un dict: `{'name': str, 'power': int, 'element': str}`
  - Devuelve una lista de magos filtrados

- `spell_transformer(spells)` - Transformar nombres de hechizos:
  - Usa `map()` con una lambda para añadir prefijo `**` y sufijo `**`
  - Entrada: lista de nombres de hechizos (cadenas)
  - Devuelve una lista de nombres de hechizos transformados

- `mage_stats(mages)` - Calcular estadísticas:
  - Usa lambdas con `max()`, `min()` para encontrar:
    - Nivel de poder del mago más poderoso
    - Nivel de poder del mago menos poderoso
    - Nivel de poder promedio (redondeado a 2 decimales)
  - Devuelve dict: `{'max_power': int, 'min_power': int, 'avg_power': float}`



## EX1
Las funciones pueden ser pasadas como argumentos, devueltas desde otras funciones y almacenadas en estructuras de datos.

¿Cómo habilitan las funciones de orden superior la reutilización y composición de código? ¿Qué hace que las funciones sean "ciudadanas de primera clase" en Python?


¿Desde qué paquete se recomienda usar `Callable`? ¿Cuál es el propósito de `callable()`?
Callable es un tipo (type hint) que representa cualquier objeto que puede ser llamado como una función. Es decir, cualquier objeto que se pueda invocar con () (paréntesis).
  - Callable es un tipo que representa "algo que se puede llamar"
  - Como una función, método, lambda, clase, o cualquier objeto con __call__

# Jerarquía de conceptos

Funciones de orden superior
├── Reciben funciones como argumentos
│   └── Ejemplo: map(), filter(), sorted(key=...)
├── Devuelven funciones
│   └── Ejemplo: decoradores, closures, fábricas
└── Permiten composición
    └── Ejemplo: pipelines, encadenamiento

Ciudadanas de primera clase
├── Asignables a variables
├── Almacenables en estructuras
├── Pasables como argumentos
├── Retornables como valores
└── Tienen atributos (como objetos)

Callable (typing)
├── Type hint para funciones
├── Callable[[params], return_type]
└── Mejora documentación y type checking

callable() (built-in)
├── Verifica si objeto es invocable
├── Útil para validación dinámica
├── Funciona en tiempo de ejecución
└── Esencial para metaprogramación

## Requisitos de Implementación

- `spell_combiner(spell1, spell2)` - Combinar dos hechizos:
  - Devuelve una nueva función que llama a ambos hechizos con los mismos argumentos
  - El hechizo combinado debe devolver una tupla con ambos resultados
  - Ejemplo: `combined = spell_combiner(fireball, heal)`

- `power_amplifier(base_spell, multiplier)` - Amplificar poder del hechizo:
  - Devuelve una función con la misma firma que el hechizo original
  - Devuelve un nuevo hechizo donde el poder se multiplica antes de lanzarlo
  - Ejemplo: `mega_fireball = power_amplifier(fireball, 3)`

- `conditional_caster(condition, spell)` - Lanzar hechizo condicionalmente:
  - Devuelve un nuevo hechizo que solo se lanza si una condición es True
  - Si la condición falla, devuelve 'Spell fizzled'
  - Tanto la condición como el hechizo reciben los mismos argumentos

- `spell_sequence(spells)` - Crear secuencia de hechizos:
  - Devuelve una función que lanza todos los hechizos en orden
  - Cada hechizo recibe los mismos argumentos
  - Devuelve una lista de todos los resultados de los hechizos


## EX2

Las funciones en Python sí tienen memoria y recuerdan el entorno donde fueron creadas. Esto se llama closure (clausura).Lo hacen capturando variables en esos closure.

¿Cómo permiten los closures que las funciones "recuerden" su entorno de creación? 
Los closures capturan variables por referencia y mantiene vivo el entorno

¿Cuáles son los beneficios del alcance léxico en la programación funcional?
1. Encapsulación y privacidad (sin clases)
2. Configuración dinámica
3. Currificación (Currying) # Función currificada: transforma f(a,b,c) en f(a)(b)(c)
4. Manejo de eventos y callbacks

¿Por qué está prohibido `global` pero permitido `nonlocal`?
```python
# Ejemplo de 'global' (generalmente desaconsejado)
contador_global = 0

def usar_global():
    global contador_global
    contador_global += 1
    return contador_global

print(usar_global())  # 1

# Ejemplo de 'nonlocal' (útil y aceptado en closures)
def funcion_externa():
    contador_local = 0
    
    def funcion_interna():
        nonlocal contador_local
        contador_local += 1
        return contador_local
    
    return funcion_interna

contar = funcion_externa()
print(contar())  # 1
```

 ¿Cuáles son las diferencias clave?
Diferencias clave entre global y nonlocal
```python
# 1. Ámbito de acción
x = "global"

def exterior():
    x = "exterior"
    
    def interior():
        # global x  # Busca en el ámbito GLOBAL (fuera de la función)
        # nonlocal x  # Busca en el ámbito EXTERIOR más cercano (de exterior)
        pass
```

## Requisitos de Implementación

- `mage_counter()` - Crear un closure contador:
  - Devuelve una función que cuenta cuántas veces ha sido llamada
  - Cada llamada debe devolver el recuento actual (comenzando desde 1)
  - El contador debe persistir entre llamadas
  - Crear dos contadores separados debe producir estados independientes
  - Usa closure para mantener el estado sin variables globales

- `spell_accumulator(initial_power)` - Crear acumulador de poder:
  - Devuelve una función que acumula poder con el tiempo
  - Cada llamada añade la cantidad dada al poder total
  - Devuelve el nuevo poder total después de cada adición
  - Comienza con `initial_power` como base

- `enchantment_factory(enchantment_type)` - Crear funciones de encantamiento:
  - Devuelve una función que aplica el encantamiento especificado
  - La función devuelta toma un nombre de ítem y devuelve una descripción encantada
  - Formato: 'tipo_encantamiento nombre_ítem' (ej., 'Flaming Sword')
  - Cada fábrica crea funciones con diferentes tipos de encantamiento

- `memory_vault()` - Crear un sistema de gestión de memoria:
  - Devuelve un dict con las funciones 'store' y 'recall'
  - Función 'store': toma (key, value) y almacena la memoria
  - Función 'recall': toma (key) y devuelve el valor almacenado o 'Memory not found'
  - Usa closure para mantener el almacenamiento de memoria privado



## EX3
1. ¿Qué es functools y para qué sirve?
functools es un módulo de la biblioteca estándar que proporciona herramientas para trabajar con funciones y objetos callables. 
Su propósito es facilitar la programación funcional y la manipulación avanzada de funciones en Python.
import functools

# Las herramientas más importantes:
 1. reduce()    → Agregación de datos
 2. partial()   → Fijar argumentos de funciones
 3. lru_cache() → Memorización automática
  4x. wraps()     → Preservar metadatos de funciones
 5. singledispatch() → Sobrecarga de funciones
 6. total_ordering → Generar métodos de comparación


Herramienta	    Propósito	            Ejemplo de uso	
reduce	        Agregación de datos	    reduce(lambda a,b: a+b, [1,2,3])
partial 	    Fijar argumentos	    partial(multiplicar, 2)
lru_cache	    Memorización	            @lru_cache(maxsize=128)
wraps	        Preservar metadatos	    @wraps(func)
singledispatch	Sobrecarga de funciones	@singledispatch
total_ordering	Generar comparaciones	@total_ordering


## Requisitos de Implementación

- `spell_reducer(spells, operation)` - Reducir poderes de hechizos:
  - Usa `functools.reduce` para combinar todos los poderes de hechizos
  - Soporta operaciones: 'add', 'multiply', 'max', 'min'
  - Usa funciones del módulo `operator` (add, mul, etc.)
  - Devuelve el valor reducido final
  - Si `spells` está vacío, devuelve 0
  - Si la operación es desconocida, maneja el error adecuadamente

- `partial_enchanter(base_enchantment)` - Crear aplicaciones parciales:
  - Toma una función de encantamiento base con firma `(power: int, element: str, target: str) -> str`
  - Usa `functools.partial` para crear 3 versiones especializadas
  - Cada versión pre-completa `power = 50` y el elemento

- `memoized_fibonacci(n)` - Fibonacci con caché:
  - Usa el decorador `functools.lru_cache` para memoización
  - Implementa el cálculo de la secuencia de Fibonacci
  - La función debe devolver el n-ésimo número de Fibonacci
  - El caché debe mejorar el rendimiento para llamadas repetidas
  - Devuelve el n-ésimo número de fibonacci

[imagen[172, 642, 271, 703]]

Puedes verificar que el caché funciona a través de `memoized_fibonacci.cache_info()`.

- `spell_dispatcher()` - Crear sistema de despacho simple:
  - Usa el decorador `functools.singledispatch` para crear un sistema de hechizos
  - La función base recibe `Any` y maneja tipos de hechizo desconocidos
  - Maneja diferentes tipos: `int` (hechizo de daño), `str` (encantamiento), `list` (multi-lanzamiento)
  - Devuelve la función despachadora
  - Cada tipo debe tener un comportamiento de hechizo apropiado


## EX4

aprenden a crear decoradores `@staticmethod` y entenderás cómo funcionan los decoradores con las clases.

Decoradores: El ejemplo más elegante de funciones de orden superior
Los decoradores son funciones de orden superior que envuelven otras funciones para extender su comportamiento.

```python
# Decorador básico (función de orden superior)
def medir_tiempo(func):
    import time
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"{func.__name__} tomó {fin - inicio:.4f} segundos")
        return resultado
    return wrapper

# Aplicar el decorador
@medir_tiempo
def operacion_lenta():
    import time
    time.sleep(0.5)
    return "Listo"

@medir_tiempo
def operacion_rapida():
    return "Rápido"

# Reutilización: el mismo decorador se aplica a diferentes funciones
print(operacion_lenta())   # operacion_lenta tomó 0.5001 segundos
print(operacion_rapida())  # operacion_rapida tomó 0.0000 segundos

# Decoradores con parámetros
def repetir(veces):
    def decorador(func):
        def wrapper(*args, **kwargs):
            resultados = []
            for _ in range(veces):
                resultados.append(func(*args, **kwargs))
            return resultados
        return wrapper
    return decorador

@repetir(3)
def saludar(nombre):
    return f"Hola {nombre}"

print(saludar("Ana"))  # ['Hola Ana', 'Hola Ana', 'Hola Ana']
```


## Requisitos de Implementación

- `spell_timer(func)` - Decorador de medición de tiempo:
  - Crea un decorador que mide el tiempo de ejecución de la función
  - Imprime "Casting nombre_función..." antes de la ejecución
  - Imprime "Spell completed in X.XXX seconds" después de la ejecución (3 decimales)
  - Usa `functools.wraps` para preservar los metadatos de la función original
  - Devuelve el resultado de la función original

- `power_validator(min_power)` - Fábrica de decoradores de validación de poder:
  - Crea un decorador que valida niveles de poder
  - Aplicado sobre una función independiente
  - Si el poder es válido (>= min_power), ejecuta la función normalmente
  - Si es inválido, devuelve "Insufficient power for this spell"
  - Usa `functools.wraps` adecuadamente

- `retry_spell(max_attempts)` - Decorador de reintentos:
  - Crea un decorador que reintenta hechizos fallidos
  - Si la función lanza una excepción, reintenta hasta `max_attempts` veces
  - Imprime "Spell failed, retrying... (attempt n/max_attempts)"
  - Si todos los intentos fallan, devuelve "Spell casting failed after max_attempts attempts"
  - Si un intento tiene éxito, devuelve su resultado normalmente

- Clase `MageGuild` - Demostrar `staticmethod`:
  - `validate_mage_name(name)` - Método estático que verifica si el nombre es válido
    - El nombre es válido si tiene al menos 3 caracteres y contiene solo letras/espacios
  - `cast_spell(self, spell_name, power)` - Método de instancia
    - Debe usar el decorador `power_validator` con `min_power=10`
    - Cuando el poder es válido, devuelve "Successfully cast spell_name with <power> power"
    - De lo contrario, devuelve "Insufficient power for this spell"
    
    
   
✅ Lo que mypy normal sí verifica:
Type hints incorrectos - Si usas un tipo incorrecto en una anotación

Incompatibilidad de tipos - Si pasas un str donde esperan int

Funciones sin anotaciones - Si algunas funciones no tienen type hints (dará advertencias)

Errores de importación - Si importas módulos que no existen

Uso incorrecto de tipos genéricos - Como list[int] vs list[str]

❌ Lo que mypy normal NO verifica (pero --strict sí):
Funciones sin anotaciones de tipo (solo da advertencias)

Variables sin tipo explícito

Retornos implícitos (None)

Uso de Any de forma implícita

Funciones sin anotaciones en métodos de clase
