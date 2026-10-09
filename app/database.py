import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "smart_resolution.db"


def get_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def create_table():
    connection = get_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            problem_description TEXT NOT NULL,
            category TEXT NOT NULL,
            priority TEXT NOT NULL,
            reasoning TEXT,
            suggested_contact TEXT,
            contact_email TEXT,
            contact_phone TEXT,
            recommended_action TEXT,
            estimated_response_time TEXT,
            status TEXT DEFAULT 'Open',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS ticket_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticket_id INTEGER NOT NULL,
            old_status TEXT,
            new_status TEXT NOT NULL,
            remarks TEXT,
            changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (ticket_id) REFERENCES tickets(id)
        )
    """)

    connection.commit()
    connection.close()