"""
Pydantic models used for request validation and response formatting.
"""
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field


class PriorityLevel(str, Enum):
    CRITICAL = "Critical"
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"


class ProblemRequest(BaseModel):
    problem_description: str = Field(
        ...,
        min_length=5,
        max_length=2000,
        description="Free-text description of the problem the user is facing.",
        examples=["My laptop won't turn on and I have a client demo in 30 minutes."],
    )
    user_name: Optional[str] = Field(
        default=None, description="Optional name of the person reporting the issue."
    )


class ResolutionResponse(BaseModel):
    category: str
    priority: PriorityLevel
    reasoning: str
    suggested_contact: str
    contact_email: str
    contact_phone: str
    recommended_action: str
    estimated_response_time: str
