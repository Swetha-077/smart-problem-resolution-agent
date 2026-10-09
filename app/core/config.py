"""
Application configuration. Loads environment variables (e.g. API keys) from a .env file.
"""
import os
import json
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
DEPARTMENTS_PATH = BASE_DIR / "data" / "departments.json"


class Settings:
    ANTHROPIC_API_KEY: str = os.getenv("ANTHROPIC_API_KEY", "")
    MODEL_NAME: str = os.getenv("MODEL_NAME", "claude-sonnet-4-5")
    APP_NAME: str = "Smart Problem Resolution Agent"


settings = Settings()


def load_departments() -> dict:
    with open(DEPARTMENTS_PATH, "r", encoding="utf-8") as f:
        return json.load(f)
