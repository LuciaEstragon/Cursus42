
IMPORTANTE:  Pydantic instalado > pip install pydantic


=======================

Explicación breve de los ejercicios

Estos ejercicios te introducen a Pydantic v2, la librería de validación de datos más potente de Python, mediante un temática espacial. Vas a crear modelos de datos que representan estaciones espaciales, informes de contacto alienígena y misiones tripuladas, aplicando diferentes niveles de validación:

    Exercise 0: Conceptos básicos: BaseModel, Field con restricciones (rangos, longitudes, opcionales) y conversión automática de tipos.

    Exercise 1: Validaciones personalizadas con @model_validator(mode='after') para implementar reglas de negocio complejas que afectan a varias campos a la vez.

    Exercise 2: Modelos anidados (CrewMember dentro de SpaceMission) y validaciones que dependen de la lista completa de tripulantes (ej. requisitos de rango y experiencia para misiones largas).

Cada ejercicio incluye una función main() que demuestra un caso válido y otro inválido, mostrando los errores de validación tal como pide el enunciado.


============================

¡Excelente pregunta! Esos son los tres pilares fundamentales de Pydantic. Te explico qué es cada uno y para qué sirve exactamente:

---

## 1. `BaseModel` (la base de todo)

**¿Qué es?** Es la clase padre de la que **heredan** todos tus modelos de datos.

**¿Qué hace?**
- Convierte tus clases en **estructuras de datos validades**.
- Cuando creas una instancia (ej: `SpaceStation(**datos)`), Pydantic automáticamente:
  1. **Valida** que los tipos sean correctos (si pasas un `str` con fecha, lo convierte a `datetime`).
  2. **Comprueba** las restricciones (mínimos, máximos, longitudes).
  3. Te da errores claros si algo falla.
  4. Te permite acceder a los atributos con notación de punto (`.crew_size`).

**Analogía:** Es como un **molde para galletas**. Tú defines la forma (campos y reglas) y Pydantic se asegura de que la masa (los datos) salga perfecta o te avise de que está mal.

---

## 2. `Field` (el configurador de atributos)

**¿Qué es?** Es una **función** que usas dentro de tu modelo para darle instrucciones extra a un campo específico.

**¿Qué hace?**
- Define **restricciones de validación**: 
  - `gt` / `ge` (mayor que / mayor o igual que)
  - `lt` / `le` (menor que / menor o igual que)
  - `min_length` / `max_length` (longitud mínima/máxima de strings)
  - `pattern` (expresiones regulares)
- Define **valores por defecto** (si no se pasa el dato).
- Añade **metadatos** (descripciones para documentación automática como Swagger).

**Ejemplo de tu código:**
```python
crew_size: int = Field(..., ge=1, le=20)
# El "..." significa que es OBLIGATORIO. 
# ge=1 -> debe ser >= 1.
# le=20 -> debe ser <= 20.
```
Si no usas `Field`, solo pones `crew_size: int`, Pydantic solo comprueba que sea `int`, pero no que esté entre 1 y 20.

---

## 3. `@model_validator` (el validador a nivel de modelo)

**¿Qué es?** Es un **decorador** (una función que modifica otra función) que aplica validaciones personalizadas que afectan a **varios campos a la vez**.

**¿Qué hace?**
- Se ejecuta **después** de que Pydantic haya validado cada campo por separado.
- Te permite escribir lógica de negocio compleja que depende de la relación entre campos.
- En Pydantic v2 (la que usas), la sintaxis correcta es `@model_validator(mode='after')`. 
  - El `mode='after'` significa que el modelo ya está creado (con todos sus campos) y tú puedes revisarlo entero y lanzar errores si algo no cuadra.

**Ejemplo de tu código:**
```python
@model_validator(mode='after')
def validate_business_rules(self) -> "AlienContact":
    # Aquí 'self' es el objeto ya validado.
    # Puedes comparar campos:
    if self.signal_strength > 7.0 and self.message_received is None:
        raise ValueError("Strong signals should include a message")
    return self  # ¡IMPORTANTE! Siempre devuelves 'self'
```

**¿Por qué es importante?** Reemplaza al viejo `@validator` (de Pydantic v1) que estaba obsoleto y solo validaba un campo a la vez. Ahora con `@model_validator` puedes hacer reglas mucho más potentes (ej: "Si la misión dura más de 365 días, al menos el 50% de la tripulación debe tener 5+ años de experiencia").

---

## Resumen rápido (tabla mental)

| Importación | ¿Qué es? | ¿Cuándo se usa? |
| :--- | :--- | :--- |
| **`BaseModel`** | Clase padre | Para **crear** tu propio modelo (ej: `class SpaceStation(BaseModel):`) |
| **`Field`** | Función configuradora | Para poner **reglas** (rangos, longitudes) y **valores por defecto** a cada campo. |
| **`@model_validator`** | Decorador | Para escribir reglas **complejas** que necesitan mirar varios campos a la vez (ej: "Si es físico, debe estar verificado"). |

---

**Bonus:** El `...` (tres puntos) que ves dentro de `Field(...)` es la forma que tiene Pydantic de decir **"Este campo es obligatorio, no tiene valor por defecto"**. Si pones `Field(default=True)`, entonces es opcional y si no se pasa, toma `True`.

¿Te queda más claro? Si quieres, puedo profundizar en cómo funciona la conversión automática de tipos o en la diferencia entre `mode='before'` y `mode='after'`.


3. Comparación con el desempaquetado de listas (*)
Para que veas la diferencia:

Operador	Para qué sirve	Ejemplo
* (un asterisco)	Desempaqueta listas/tuplas en argumentos posicionales	func(*[1, 2, 3]) → func(1, 2, 3)
** (dos asteriscos)	Desempaqueta diccionarios en argumentos con nombre	func(**{"a": 1, "b": 2}) → func(a=1, b=2)

NO son punteros. Son un operador de desempaquetado.


# EX0
class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10)  # Cadena, 3-10 caracteres
    name: str = Field(..., min_length=1, max_length=50)        # Cadena, 1-50 caracteres
    crew_size: int = Field(..., ge=1, le=20)                   # Entero, 1-20 personas
    power_level: float = Field(..., ge=0.0, le=100.0)          # Flotante, 0.0-100.0 por ciento
    oxygen_level: float = Field(..., ge=0.0, le=100.0)         # Flotante, 0.0-100.0 por ciento
    last_maintenance: datetime                                 # Campo DateTime
    # los siguientes no son obligatorios, porque tienen valor por defecto, o no son (...), y pydantic o rellena None 
    is_operational: bool = Field(default=True)                 # Booleano, por defecto `True`
    notes: Optional[str] = Field(None, max_length=200)         # Cadena opcional, máximo 200 caracteres

# EX1
class AlienContact(BaseModel):
    contact_id: str = Field(..., min_length=5, max_length=15)  # Cadena, 5-15 caracteres
    timestamp: datetime                                        # DateTime 
    location: str = Field(..., min_length=3, max_length=100)   # Cadena, 3-100 caracteres
    contact_type: ContactType                                  # Enum `ContactType`
    signal_strength: float = Field(..., ge=0.0, le=10.0)       # Flotante, escala 0.0-10.0
    duration_minutes: int = Field(..., ge=1, le=1440)          # Entero, 1-1440 (máximo 24 horas)
    witness_count: int = Field(..., ge=1, le=100)              # Entero, 1-100 personas
    message_received: Optional[str] = Field(None, max_length=500)  # Cadena opcional, máximo 500 caracteres
    is_verified: bool = Field(default=False)                   # Booleano, por defecto `False`

    # reglas de negocio:  @model_validator(mode='after')  # existen (mode='before')
    @model_validator(mode="after")
    def validate_business_rules(self) -> "AlienContact":
        # Regla 1: El ID de contacto debe comenzar con 'AC' (Alien Contact).
        if not self.contact_id.startswith("AC"):
            raise ValueError("contact_id must start with 'AC'")

        # Regla 2: Los informes de contacto físico (`physical`) deben ser verificados.
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        # Regla 3: El contacto telepático requiere al menos 3 testigos.
        if (
            self.contact_type == ContactType.TELEPATHIC
            and self.witness_count < 3
        ):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
                )

        # Regla 4: Las señales fuertes (> 7.0) deberían incluir mensajes recibidos.
        if self.signal_strength > 7.0 and self.message_received is None:
            raise ValueError(
                "Strong signals (>7.0) should include a received message"
                )

        return self


# EX2
Dominar los modelos anidados de Pydantic y las relaciones complejas de datos.

Define los rangos de tripulación: `cadet`, `officer`, `lieutenant`, `captain`, `commander`



Miembro individual de la tripulación con estos campos:

- `member_id`: Cadena, 3-10 caracteres
- `name`: Cadena, 2-50 caracteres
- `rank`: Enum `Rank`
- `age`: Entero, 18-80 años
- `specialization`: Cadena, 3-30 caracteres
- `years_experience`: Entero, 0-50 años
- `is_active`: Booleano, por defecto `True`

### Modelo `SpaceMission`

Misión con lista de tripulación y estos campos:

- `mission_id`: Cadena, 5-15 caracteres
- `mission_name`: Cadena, 3-100 caracteres
- `destination`: Cadena, 3-50 caracteres
- `launch_date`: DateTime
- `duration_days`: Entero, 1-3650 días (máximo 10 años)
- `crew`: Lista de `CrewMember`, 1-12 miembros
- `mission_status`: Cadena, por defecto 'planned'
- `budget_millions`: Flotante, 1.0-10000.0 millones de dólares

### Reglas de Validación de la Misión

Implementa `@model_validator(mode='after')` con estos requisitos de seguridad:

- El ID de la misión debe comenzar con 'M'.
- Debe tener al menos un Comandante o Capitán.
- Las misiones largas (>365 días) necesitan 50% de tripulación experimentada (5+ años).
- Todos los miembros de la tripulación deben estar activos.





# CORRECCION

Esta actividad incluye herramientas de generación de datos para ayudarte a probar tus modelos de Pydantic:

- `data_generator.py` - Genera datos de prueba realistas para todos los ejercicios.
- `data_exporter.py` - Exporta datos en formatos JSON, CSV y Python.
- `generated_data/` - Conjuntos de datos pregenerados listos para usar.

Estructura e los test: 

tu_proyecto/
├── ex0/
│   └── space_station.py
├── ex1/
│   └── alien_contact.py
├── ex2/
│   └── space_crew.py
├── tools/                    # <--- ¡IMPORTANTE! Aquí van los generadores
│   ├── data_generator.py
│   └── data_exporter.py
└── generated_data/           # <--- Datos pre-generados (JSON/CSV)
    ├── space_stations.json
    ├── alien_contacts.json
    └── space_missions.json
