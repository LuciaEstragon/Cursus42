"""
Exercise 2: Space Crew Management
Nested Pydantic models and complex mission validation.
"""

from datetime import datetime
from enum import Enum
from typing import List

from pydantic import BaseModel, Field, model_validator


class Rank(str, Enum):
    """Crew ranks."""

    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    """Individual crew member."""

    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    """Mission with a crew list and validation rules."""

    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)  # max 10 years
    crew: List[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission_rules(self) -> "SpaceMission":
        """
        Custom mission validation:
        - Mission ID must start with 'M'
        - At least one Commander or Captain in crew
        - Long missions (>365 days) need >= 50% experienced crew (5+ years)
        - All crew members must be active
        """
        # Rule 1: ID prefix
        if not self.mission_id.startswith("M"):
            raise ValueError("mission_id must start with 'M'")

        # Rule 2: At least one Commander or Captain
        if not any(
            member.rank in (Rank.COMMANDER, Rank.CAPTAIN)
            for member in self.crew
        ):
            raise ValueError(
                "Mission must have at least one Commander or Captain"
                )

        # Rule 3: All crew active
        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")

        # Rule 4: Long missions need 50% experienced crew (>=5 years)
        if self.duration_days > 365:
            experienced = sum(1 for m in self.crew if m.years_experience >= 5)
            total = len(self.crew)
            if experienced / total < 0.5:
                raise ValueError(
                    "Long missions (>365 days) require at least 50% "
                    "experienced crew (5+ years)"
                )

        return self


def main() -> None:
    """Demonstrate valid and invalid missions."""
    print("Space Crew Management Validation")
    print("=" * 35)

    # Build a valid crew
    crew_data = [
        {
            "member_id": "C001",
            "name": "Alice",
            "rank": Rank.COMMANDER,
            "age": 45,
            "specialization": "Pilot",
            "years_experience": 20,
            "is_active": True,
        },
        {
            "member_id": "C002",
            "name": "Bob",
            "rank": Rank.CAPTAIN,
            "age": 38,
            "specialization": "Engineer",
            "years_experience": 12,
            "is_active": True,
        },
        {
            "member_id": "C003",
            "name": "Charlie",
            "rank": Rank.OFFICER,
            "age": 30,
            "specialization": "Scientist",
            "years_experience": 8,
            "is_active": True,
        },
        {
            "member_id": "C004",
            "name": "Diana",
            "rank": Rank.LIEUTENANT,
            "age": 28,
            "specialization": "Medic",
            "years_experience": 5,
            "is_active": True,
        },
    ]

    # --- Valid mission (short) ---
    valid_mission_data = {
        "mission_id": "M12345",
        "mission_name": "Alpha Centauri Expedition",
        "destination": "Alpha Centauri",
        "launch_date": "2026-03-15T09:00:00",
        "duration_days": 200,
        "crew": crew_data,
        "mission_status": "planned",
        "budget_millions": 500.0,
    }
    mission = SpaceMission(**valid_mission_data)
    print("\nValid mission created:")
    print(f"  Mission ID: {mission.mission_id}")
    print(f"  Name: {mission.mission_name}")
    print(f"  Crew size: {len(mission.crew)}")
    print(f"  Duration: {mission.duration_days} days")

    # --- Invalid mission: no Commander/Captain ---
    print("\nExpected validation error (no Commander or Captain):")
    bad_crew = crew_data.copy()
    # Change first crew member's rank to cadet (remove commander)
    bad_crew[0]["rank"] = Rank.CADET
    bad_crew[1]["rank"] = Rank.OFFICER  # No captain either
    invalid_data = valid_mission_data.copy()
    invalid_data["crew"] = bad_crew
    try:
        _ = SpaceMission(**invalid_data)
    except Exception as e:
        print(f"  {e}")

    # --- Invalid mission: long duration but not enough experienced crew ---
    print("\nExpected validation error (long mission, <50% experienced):")
    inexperienced_crew = crew_data.copy()
    # Make two members inexperienced
    inexperienced_crew[2]["years_experience"] = 2
    inexperienced_crew[3]["years_experience"] = 1
    invalid_data2 = valid_mission_data.copy()
    invalid_data2["duration_days"] = 400  # >365
    invalid_data2["crew"] = inexperienced_crew
    try:
        _ = SpaceMission(**invalid_data2)
    except Exception as e:
        print(f"  {e}")


if __name__ == "__main__":
    main()
