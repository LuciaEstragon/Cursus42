"""
Exercise 0: Space Station Data
Basic Pydantic model with Field validation.
"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class SpaceStation(BaseModel):
    """Model Pydantic for a space station with basic validation."""

    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(None, max_length=200)


def main() -> None:
    """Demonstrate valid and invalid space station instances."""
    print("Space Station Data Validation")
    print("=" * 30)

    # --- Valid station ---
    valid_data = {
        "station_id": "ISS001",
        "name": "International Space Station",
        "crew_size": 6,
        "power_level": 85.5,
        "oxygen_level": 92.3,
        "last_maintenance": "2025-01-15T10:30:00",
        "is_operational": True,
        "notes": "All systems nominal",
    }
    station = SpaceStation(**valid_data)
    print("\nValid station created:")
    print(f"  ID: {station.station_id}")
    print(f"  Name: {station.name}")
    print(f"  Crew: {station.crew_size} people")
    print(f"  Power: {station.power_level}%")
    print(f"  Oxygen: {station.oxygen_level}%")
    status = "Operational" if station.is_operational else "Non-operational"
    print(f"  Status: {status}")

    # --- Invalid station (crew_size > 20) ---
    print("\nExpected validation error:")
    invalid_data = valid_data.copy()
    invalid_data["crew_size"] = 25
    try:
        _ = SpaceStation(**invalid_data)
    except Exception as e:
        print(f"  {e}")


if __name__ == "__main__":
    main()
