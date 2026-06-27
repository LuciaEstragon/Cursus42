"""
Exercise 1: Alien Contact Logs
Custom validation using @model_validator for complex business rules.
"""

from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, model_validator


class ContactType(str, Enum):
    """Allowed contact types."""

    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    """Model for an alien contact report with custom business rules."""

    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(..., ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    message_received: Optional[str] = Field(None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def validate_business_rules(self) -> "AlienContact":
        """
        Apply custom validation rules:
        - Contact ID must start with 'AC'
        - Physical contact must be verified
        - Telepathic contact requires at least 3 witnesses
        - Strong signals (> 7.0) should include a message
        """
        # Rule 1: ID prefix
        if not self.contact_id.startswith("AC"):
            raise ValueError("contact_id must start with 'AC'")

        # Rule 2: Physical contacts must be verified
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        # Rule 3: Telepathic requires at least 3 witnesses
        if (
            self.contact_type == ContactType.TELEPATHIC
            and self.witness_count < 3
        ):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
                )

        # Rule 4: Strong signals should include a message
        if self.signal_strength > 7.0 and self.message_received is None:
            raise ValueError(
                "Strong signals (>7.0) should include a received message"
                )

        return self


def main() -> None:
    """Demonstrate valid and invalid alien contact reports."""
    print("Alien Contact Logs Validation")
    print("=" * 35)

    # --- Valid contact ---
    valid_data = {
        "contact_id": "AC12345",
        "timestamp": "2025-02-10T14:30:00",
        "location": "Sector 7, Nebula",
        "contact_type": ContactType.RADIO,
        "signal_strength": 5.2,
        "duration_minutes": 30,
        "witness_count": 2,
        "message_received": "Hello from the stars!",
        "is_verified": False,
    }
    contact = AlienContact(**valid_data)
    print("\nValid contact created:")
    print(f"  ID: {contact.contact_id}")
    print(f"  Type: {contact.contact_type.value}")
    print(f"  Verified: {contact.is_verified}")

    # --- Invalid contact: physical not verified ---
    print("\nExpected validation error (physical not verified):")
    invalid_data = valid_data.copy()
    invalid_data["contact_id"] = "AC99999"
    invalid_data["contact_type"] = ContactType.PHYSICAL
    invalid_data["is_verified"] = False
    try:
        _ = AlienContact(**invalid_data)
    except Exception as e:
        print(f"  {e}")

    # --- Invalid contact: strong signal without message ---
    print("\nExpected validation error (strong signal no message):")
    invalid_data2 = valid_data.copy()
    invalid_data2["contact_id"] = "AC88888"
    invalid_data2["signal_strength"] = 8.5
    invalid_data2["message_received"] = None
    try:
        _ = AlienContact(**invalid_data2)
    except Exception as e:
        print(f"  {e}")


if __name__ == "__main__":
    main()
