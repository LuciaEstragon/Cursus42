#!/usr/bin/env python3

# ************************************************************************ #
#                                                                          #
#                                                      :::      ::::::::   #
#   data_processor.py                                ::+::    :+:    :+:   #
#                                                  +:+ +:+         +:+     #
#   By: lestrada <lestrada@student.42.es>        +#+  +:+       +#+        #
#                                              +#+#+#+#+#+   +#+           #
#   Created: 2026/05/06          by lestrada        #+#    #+#             #
#   Updated: 2026/05/10          by lestrada       ###   ########.es       #
#                                                                          #
# ************************************************************************ #


from abc import ABC, abstractmethod
from collections import deque
from typing import Any, Union, List, Dict


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: deque[Any] = deque()
        self._rank = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Comprueba si el dato puede ser procesado."""
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        """Procesa los datos y los almacena internamente."""
        pass

    def output(self) -> tuple[int, str]:
        """
        Extrae el dato más antiguo y lo devuelve junto con su rango.
        Lanza IndexError si no hay datos.
        """
        if not self._storage:
            raise IndexError("No data to output")
        rank, value = self._storage.popleft()
        return (rank, value)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list) and all(
            isinstance(x, (int, float)) for x in data
        ):
            return True
        return False

    def ingest(self, data: Union[int, float, List[Union[int, float]]]) -> None:
        if not self.validate(data):
            raise TypeError("Invalid data for NumericProcessor")
        if isinstance(data, (int, float)):
            items = [str(data)]
        else:  # lista de números
            items = [str(x) for x in data]
        for item in items:
            self._storage.append((self._rank, item))
            self._rank += 1


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list) and all(isinstance(x, str) for x in data):
            return True
        return False

    def ingest(self, data: Union[str, List[str]]) -> None:
        if not self.validate(data):
            raise TypeError("Invalid data for TextProcessor")
        if isinstance(data, str):
            items = [data]
        else:
            items = data
        for item in items:
            self._storage.append((self._rank, item))
            self._rank += 1


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            # comprobar que todas las claves y valores son strings
            return all(
                isinstance(key, str) and isinstance(value, str)
                for key, value in data.items()
            )
        if isinstance(data, list) and all(
            isinstance(item, dict) for item in data
        ):
            return all(self.validate(item) for item in data)
        return False

    def ingest(
        self, data: Union[Dict[str, str], List[Dict[str, str]]]
    ) -> None:
        if not self.validate(data):
            raise TypeError("Invalid data for LogProcessor")
        if isinstance(data, dict):
            items = [data]
        else:
            items = data
        for entry in items:
            # Convertir dict a cadena con formato "clave: valor"
            line = " ".join(f"{k}: {v}" for k, v in entry.items())
            self._storage.append((self._rank, line))
            self._rank += 1


# ==================== PRUEBAS (según el enunciado) ====================
if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")

    # NumericProcessor
    print("\nTesting Numeric Processor...")
    np = NumericProcessor()
    print("  Trying to validate input '42':", np.validate(42))
    print("  Trying to validate input 'Hello':", np.validate("Hello"))
    print("  Test invalid ingestion of string 'foo' without prior validation:")
    try:
        np.ingest("foo")  # mypy warning intencionado, pero lanza excepción
    except TypeError as e:
        print(f"    Got exception: {e}")
    print("  Processing data: [1, 2, 3, 4, 5]")
    np.ingest([1, 2, 3, 4, 5])
    print("  Extracting 3 values...")
    for i in range(3):
        rank, val = np.output()
        print(f"    Numeric value {rank}: {val}")

    # TextProcessor
    print("\nTesting Text Processor...")
    tp = TextProcessor()
    print("  Trying to validate input '42':", tp.validate(42))
    print("  Processing data: ['Hello', 'Nexus', 'World']")
    tp.ingest(["Hello", "Nexus", "World"])
    print("  Extracting 1 value...")
    rank, val = tp.output()
    print(f"    Text value {rank}: {val}")

    # LogProcessor
    print("\nTesting Log Processor...")
    lp = LogProcessor()
    print("  Trying to validate input 'Hello':", lp.validate("Hello"))
    logs = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!"}
    ]
    print(f"  Processing data: {logs}")
    lp.ingest(logs)
    print("  Extracting 2 values...")
    for i in range(2):
        rank, val = lp.output()
        print(f"    Log entry {rank}: {val}")
