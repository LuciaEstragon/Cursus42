#!/usr/bin/env python3

# ************************************************************************ #
#                                                                          #
#                                                      :::      ::::::::   #
#   data_stream.py                                   ::+::    :+:    :+:   #
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


# ------------------ Clases del Ejercicio 0 (reutilizadas) ------------------
class DataProcessor(ABC):
    def __init__(self)-> None:
        self._storage: deque[Any] = deque()
        self._rank = 0
        self._total_processed = 0   # nuevo atributo para estadísticas

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._storage:
            raise IndexError("No data to output")
        rank, value = self._storage.popleft()
        return (rank, value)

    def get_stats(self) -> tuple[int, int]:
        """Devuelve (total_processed, remaining)"""
        return (self._total_processed, len(self._storage))


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
        else:
            items = [str(x) for x in data]
        for item in items:
            self._storage.append((self._rank, item))
            self._rank += 1
            self._total_processed += 1


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
            self._total_processed += 1


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return all(
                isinstance(k, str) and isinstance(v, str)
                for k, v in data.items()
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
            line = " ".join(f"{k}: {v}" for k, v in entry.items())
            self._storage.append((self._rank, line))
            self._rank += 1
            self._total_processed += 1


class DataStream():
    def __init__(self) -> None:
        self._processors: List[DataProcessor] = []
        # almacena una lista ordenada de objetos que heredan de DataProcessor

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: List[Any]) -> None:
        for element in stream:
            handled = False
            for proc in self._processors:
                if proc.validate(element):
                    proc.ingest(element)
                    handled = True
                    break
            if not handled:
                print(f"DataStream error - "
                      f"Can't process element in stream: {element}")

    def print_processors_stats(self) -> None:
        if not self._processors:
            print("No processor found, no data")
            return
        print("=== DataStream statistics ===")
        for proc in self._processors:
            total, remaining = proc.get_stats()
            name = proc.__class__.__name__
            print(f"{name}: total {total} items processed, "
                  f"remaining {remaining} on processor")


# ------------------------------------
if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===")
    ds = DataStream()
    print("Initialize Data Stream...")
    ds.print_processors_stats()

    print("Registering Numeric Processor")
    ds.register_processor(NumericProcessor())

    stream_data = [
        'Hello world',
        [3.14, -1, 2.71],
        [{'log_level': 'WARNING',
         'log_message': 'Telnet access! Use ssh instead'},
         {'log_level': 'INFO', 'log_message': 'User will is connected'}],
        42,
        ['Hi', 'five']
    ]
    print("Send first batch of data on stream:")
    print(stream_data)
    ds.process_stream(stream_data)
    ds.print_processors_stats()

    print("Registering other data processors")
    ds.register_processor(TextProcessor())
    ds.register_processor(LogProcessor())

    print("Send the same batch again")
    ds.process_stream(stream_data)
    ds.print_processors_stats()

    print("Consume some elements from the data processors: "
          "Numeric 3, Text 2, Log 1")
    # Extraer elementos de cada procesador (están en orden de registro)
    numeric = ds._processors[0]
    text = ds._processors[1]
    log = ds._processors[2]
    for _ in range(3):
        numeric.output()
    for _ in range(2):
        text.output()
    for _ in range(1):
        log.output()

    ds.print_processors_stats()
