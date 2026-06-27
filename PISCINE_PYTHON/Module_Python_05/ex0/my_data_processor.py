'''
Informe de Ingeniería: 
¡Bienvenido al Código Nexus! 
Construye la base de nuestro sistema de procesamiento de datos. 
Crearás la arquitectura base del procesador y demostrarás cómo diferentes tipos de datos pueden compartir interfaces de procesamiento comunes mientras mantienen sus características únicas.

Este ejercicio requiere el uso de clases abstractas usando ABC (Clase Base Abstracta). Primero crearemos clases separadas que compartan interfaces comunes. En el siguiente ejercicio, se unificarán en el mismo flujo de trabajo.

Configura la siguiente arquitectura:

- Una clase abstracta `DataProcessor` que herede de `ABC` y defina la interfaz de procesamiento común.
- Tres clases especializadas `NumericProcessor`, `TextProcessor` y `LogProcessor` que hereden de la clase `DataProcessor` y procesarán diferentes tipos de datos.
- Dos métodos abstractos en `DataProcessor`: `validate`, que comprobará si los datos de entrada son apropiados para el procesador de datos actual, y `ingest`, que procesará los datos de entrada. 
    Cada clase especializada necesitará sobrescribir estos métodos.
- Un método estándar en `DataProcessor`: `output`, que devolverá los datos ingeridos.

Debes cumplir con las siguientes restricciones:

- El método `validate` se definirá como `validate(self, data: Any) -> bool` en la clase `DataProcessor`. Los métodos sobrescritos en las clases especializadas compartirán la misma firma, ya que no pueden saber qué datos se enviarán y deben aceptar cualquier tipo. Este método devuelve un `bool` que indica si los datos proporcionados pueden ser ingeridos por este procesador de datos.
- El método `ingest` se definirá como `ingest(self, data: Any) -> None` en la clase `DataProcessor`. Los métodos sobrescritos en las clases especializadas tendrán sus propias firmas específicas para coincidir con los tipos que esperan. En caso de que el usuario no valide los datos antes de llamar a `ingest` y proporcione datos inválidos, se debe lanzar una excepción.
- El método `output` se definirá como `output(self) -> tuple[int, str]` en la clase `DataProcessor`. No es necesario sobrescribirlo en las clases especializadas.
- El `NumericProcessor` ingiere `int`, `float` y listas de ambos tipos (incluyendo listas de tipos mixtos). Luego convierte los datos en cadenas y los almacena internamente, esperando ser extraídos usando el método `output`. La firma del método `ingest` sobrescrito debe reflejar los tipos aceptados.
- El `TextProcessor` ingiere `str` y listas de cadenas. Almacena los datos internamente, esperando ser extraídos usando el método `output`. La firma del método `ingest` sobrescrito debe reflejar los tipos aceptados.
- El `LogProcessor` ingiere un `dict` de pares clave-valor de tipo cadena, y listas de ese tipo. Luego convierte los datos en cadenas y los almacena internamente, esperando ser extraídos usando el método `output`. La firma del método `ingest` sobrescrito debe reflejar los tipos aceptados.
- El método `output` extraerá el dato más antiguo almacenado internamente en el procesador de datos, junto con el rango de procesamiento asociado dentro del procesador de datos. El dato se elimina entonces del procesador de datos.

Finalmente, prueba tu arquitectura:
- Crea instancias para cada clase especializada.
- Prueba datos válidos e inválidos para cada clase a través del método `validate`.
- Prueba al menos un dato inválido con el método `ingest` sin validación previa, y comprueba que lanza una excepción. Esto te dejará con una advertencia de mypy, a propósito.
- Ingiere varios datos para cada procesador de datos y luego extráelos usando `output`.



Comprobaciones comunes para VALIDATE:
Solo str: isinstance(data, str)
Solo int: isinstance(data, int)
int o float: isinstance(data, (int, float))
Lista de int o float: isinstance(data, list) and all(isinstance(x, (int, float)) for x in data)
Diccionario: isinstance(data, dict)

El metodo INGEST tiene que castear el tipo de dato para obtener un array de srt()
a = 10
print(type(a)) # <class 'int'>
a = str(a)
print(type(a)) # <class 'str'>

El método OUTPUT extraerá el dato más antiguo -> FIFO (First In, First Out)
Si usas una lista normal de Python:
append() al final es O(1) (rápido).
Pero pop(0) para extraer el primero es O(n), porque debe desplazar todos los elementos restantes una posición hacia la izquierda. Si procesas muchos datos, esto se vuelve lento.

Si usas deque (del módulo collections):
from collections import deque
append() al final es O(1).
popleft() para extraer el primero también es O(1) (constante, muy rápido).

Además, deque está específicamente diseñado para este tipo de uso: colas y pilas de doble extremo.
'''


from abc import ABC, abstractmethod
from collections import deque


class DataProcessor(ABC):
    @abstractmethod
    def validate(self, data: any) -> bool:
        """  
        Comprobará si los datos de entrada son apropiados para el procesador de datos actual  
        Los métodos sobrescritos en las clases especializadas compartirán la misma firma, ya que no pueden saber qué datos se enviarán y deben aceptar cualquier tipo. 
        Este método devuelve un `bool` que indica si los datos proporcionados pueden ser ingeridos por este procesador de datos.
        """
        pass

    @abstractmethod
    def ingest(self, data: any) -> None:
        """
        Procesará los datos de entrada
        Los métodos sobrescritos en las clases especializadas tendrán sus propias firmas específicas para coincidir con los tipos que esperan. 
        En caso de que el usuario no valide los datos antes de llamar a `ingest` y proporcione datos inválidos, se debe lanzar una excepción.
        """
        pass

    def output(self) -> tuple[int, str]:
        """
        Devolverá los datos ingeridos
        No es necesario sobrescribirlo en las clases especializadas.
        - El método `output` extraerá el dato más antiguo almacenado internamente en el procesador de datos, 
            junto con el rango de procesamiento asociado dentro del procesador de datos.
            El dato se elimina entonces del procesador de datos.
        """
        if not self._storage:
            raise IndexError("No data to output")
        rank, value = self._storage.popleft()
        return (rank, value)



class NumericProcessor(DataProcessor):
    """
    Ingiere `int`, `float` y listas de ambos tipos (incluyendo listas de tipos mixtos).
    Luego convierte los datos en cadenas y los almacena internamente, esperando ser extraídos usando el método `output`.
    La firma del método `ingest` sobrescrito debe reflejar los tipos aceptados.
    """
    def validate(self, data: any) -> bool:
        """  
        Comprobará si los datos de entrada son apropiados para el procesador de datos actual  
        Los métodos sobrescritos en las clases especializadas compartirán la misma firma, ya que no pueden saber qué datos se enviarán y deben aceptar cualquier tipo. 
        Este método devuelve un `bool` que indica si los datos proporcionados pueden ser ingeridos por este procesador de datos.
        """
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list) and all(isinstance(x, (int, float)) for x in data):
            return True
        return False

    def ingest(self, data: any) -> None:
        """
        Procesará los datos de entrada
        Los métodos sobrescritos en las clases especializadas tendrán sus propias firmas específicas para coincidir con los tipos que esperan. 
        En caso de que el usuario no valide los datos antes de llamar a `ingest` y proporcione datos inválidos, se debe lanzar una excepción.
        """
        if not self.validate(data):
            raise TypeError("Invalid data for NumericProcessor")
        # Convertir a lista de strings
        if isinstance(data, (int, float)):
            items = [str(data)]
        else:  # lista
            items = [str(x) for x in data]
        for item in items:
            self._storage.append((self._rank, item))
            self._rank += 1
    
class TextProcessor(DataProcessor):
    """
    ingiere `str` y listas de cadenas.
    Almacena los datos internamente, esperando ser extraídos usando el método `output`.
    La firma del método `ingest` sobrescrito debe reflejar los tipos aceptados.
    """
    def validate(self, data: any) -> bool:
        """  
        Comprobará si los datos de entrada son apropiados para el procesador de datos actual  
        Los métodos sobrescritos en las clases especializadas compartirán la misma firma, ya que no pueden saber qué datos se enviarán y deben aceptar cualquier tipo. 
        Este método devuelve un `bool` que indica si los datos proporcionados pueden ser ingeridos por este procesador de datos.
        """
        if isinstance(data, str):
            return True
        return False

    def ingest(self, data: any) -> None:
        """
        Procesará los datos de entrada
        Los métodos sobrescritos en las clases especializadas tendrán sus propias firmas específicas para coincidir con los tipos que esperan. 
        En caso de que el usuario no valide los datos antes de llamar a `ingest` y proporcione datos inválidos, se debe lanzar una excepción.
        """
        if not self.validate(data):
            raise TypeError("Invalid data for NumericProcessor")
        # Convertir a lista de strings
        items = [str(data)]
        for item in items:
            self._storage.append((self._rank, item))
            self._rank += 1
    

class LogProcessor(DataProcessor):
    """
    ingiere un `dict` de pares clave-valor de tipo cadena, y listas de ese tipo. 
    Luego convierte los datos en cadenas y los almacena internamente, esperando ser extraídos usando el método `output`.
    La firma del método `ingest` sobrescrito debe reflejar los tipos aceptados.
    """
    def validate(self, data: any) -> bool:
        """  
        Comprobará si los datos de entrada son apropiados para el procesador de datos actual  
        Los métodos sobrescritos en las clases especializadas compartirán la misma firma, ya que no pueden saber qué datos se enviarán y deben aceptar cualquier tipo. 
        Este método devuelve un `bool` que indica si los datos proporcionados pueden ser ingeridos por este procesador de datos.
        """
        pass

    def ingest(self, data: any) -> None:
        """
        Procesará los datos de entrada
        Los métodos sobrescritos en las clases especializadas tendrán sus propias firmas específicas para coincidir con los tipos que esperan. 
        En caso de que el usuario no valide los datos antes de llamar a `ingest` y proporcione datos inválidos, se debe lanzar una excepción.
        """
        pass