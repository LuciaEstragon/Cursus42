#!/usr/bin/env python3

# ************************************************************************ #
#                                                                          #
#                                                      :::      ::::::::   #
#   data_pipeline.py                                 ::+::    :+:    :+:   #
#                                                  +:+ +:+         +:+     #
#   By: lestrada <lestrada@student.42.es>        +#+  +:+       +#+        #
#                                              +#+#+#+#+#+   +#+           #
#   Created: 2026/05/06          by lestrada        #+#    #+#             #
#   Updated: 2026/05/10          by lestrada       ###   ########.es       #
#                                                                          #
# ************************************************************************ #


from abc import ABC, abstractmethod
from collections import deque
from typing import Any, Union, List, Dict, Protocol
import json


# ------------------ Clases DataProcessor (igual que antes) ------------------
class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: deque[Any] = deque()
        self._rank: int = 0
        self._total_processed = 0

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


# ------------------ ExportPlugin (Protocol) ------------------
class ExportPlugin(Protocol):
    def process_output(self, data: List[tuple[int, str]]) -> None:
        """Procesa una lista de tuplas (rango, valor) y la exporta."""


class CSVExportPlugin():
    def process_output(self, data: List[tuple[int, str]]) -> None:
        if not data:
            print("No data to export as CSV")
            return
        lines = ["rank,value"]
        for rank, value in data:
            # Escapar comillas dobles si aparecen en value
            escaped = value.replace('"', '""')
            lines.append(f'{rank},"{escaped}"')
        csv_string = "\n".join(lines)
        print("CSV Export:")
        print(csv_string)


class JSONExportPlugin():
    def process_output(self, data: List[tuple[int, str]]) -> None:
        if not data:
            print("No data to export as JSON")
            return
        # Convertir a lista de diccionarios
        json_list = [{"rank": rank, "value": value} for rank, value in data]
        json_string = json.dumps(json_list, indent=2)
        print("JSON Export:")
        print(json_string)


# ------------------ DataStream con output_pipeline ------------------
class DataStream():
    def __init__(self) -> None:
        self._processors: List[DataProcessor] = []

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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        """
        Extrae `nb` elementos de CADA procesador registrado (si hay
        suficientes) y los pasa al plugin para exportación.
        """
        all_data: List[tuple[int, str]] = []
        for proc in self._processors:
            for _ in range(nb):
                try:
                    rank, value = proc.output()
                    all_data.append((rank, value))
                except IndexError:
                    # No hay más datos en este procesador
                    break
        plugin.process_output(all_data)

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


# ------ Escenario de prueba (similar al ejercicio 1 + pipeline) -------
if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===")
    ds = DataStream()
    print("Registering Numeric, Text and Log Processors")
    ds.register_processor(NumericProcessor())
    ds.register_processor(TextProcessor())
    ds.register_processor(LogProcessor())

    stream_data = [
        'Hello world',
        [3.14, -1, 2.71],
        [{'log_level': 'WARNING',
         'log_message': 'Telnet access! Use ssh instead'},
         {'log_level': 'INFO', 'log_message': 'User will is connected'}],
        42,
        ['Hi', 'five']
    ]
    print("Processing stream...")
    ds.process_stream(stream_data)
    ds.print_processors_stats()

    print()
    print("--- Exporting 2 elements from each processor using CSV plugin ---")
    ds.output_pipeline(2, CSVExportPlugin())
    ds.print_processors_stats()

    print()
    print("--- Exporting 1 more element from each processor using JSON "
          "plugin ---")
    ds.output_pipeline(1, JSONExportPlugin())
    ds.print_processors_stats()
