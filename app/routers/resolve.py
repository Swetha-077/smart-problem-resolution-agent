from fastapi import APIRouter
from app.models.schemas import ProblemRequest, ResolutionResponse
from app.core.resolver import resolve_problem
from app.database import get_connection

router = APIRouter()


@router.post("/resolve", response_model=ResolutionResponse)
def resolve(request: ProblemRequest):
    result = resolve_problem(request.problem_description)

    connection = get_connection()

    cursor = connection.execute(
        """
        INSERT INTO tickets (
            problem_description,
            category,
            priority,
            reasoning,
            suggested_contact,
            contact_email,
            contact_phone,
            recommended_action,
            estimated_response_time
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            request.problem_description,
            result["category"],
            result["priority"],
            result["reasoning"],
            result["suggested_contact"],
            result["contact_email"],
            result["contact_phone"],
            result["recommended_action"],
            result["estimated_response_time"]
        )
    )

    ticket_id = cursor.lastrowid

    connection.execute(
        """
        INSERT INTO ticket_history (
            ticket_id,
            old_status,
            new_status,
            remarks
        )
        VALUES (?, ?, ?, ?)
        """,
        (
            ticket_id,
            None,
            "Open",
            "Ticket created"
        )
    )

    connection.commit()
    connection.close()

    return result


@router.get("/tickets")
def get_tickets():
    connection = get_connection()

    rows = connection.execute(
        "SELECT * FROM tickets ORDER BY id DESC"
    ).fetchall()

    connection.close()

    return [dict(row) for row in rows]


@router.put("/tickets/{ticket_id}/status")
def update_ticket_status(ticket_id: int, status: str):
    allowed_statuses = ["Open", "In Progress", "Resolved"]

    if status not in allowed_statuses:
        return {
            "error": "Invalid status",
            "allowed_statuses": allowed_statuses
        }

    connection = get_connection()

    ticket = connection.execute(
        "SELECT status FROM tickets WHERE id = ?",
        (ticket_id,)
    ).fetchone()

    if ticket is None:
        connection.close()
        return {
            "error": "Ticket not found"
        }

    old_status = ticket["status"]

    connection.execute(
        "UPDATE tickets SET status = ? WHERE id = ?",
        (status, ticket_id)
    )

    connection.execute(
        """
        INSERT INTO ticket_history (
            ticket_id,
            old_status,
            new_status,
            remarks
        )
        VALUES (?, ?, ?, ?)
        """,
        (
            ticket_id,
            old_status,
            status,
            "Status updated"
        )
    )

    connection.commit()
    connection.close()

    return {
        "message": "Ticket status updated successfully",
        "ticket_id": ticket_id,
        "old_status": old_status,
        "new_status": status
    }


@router.get("/tickets/{ticket_id}/history")
def get_ticket_history(ticket_id: int):
    connection = get_connection()

    rows = connection.execute(
        """
        SELECT *
        FROM ticket_history
        WHERE ticket_id = ?
        ORDER BY id ASC
        """,
        (ticket_id,)
    ).fetchall()

    connection.close()

    return [dict(row) for row in rows]


@router.get("/dashboard")
def get_dashboard():
    connection = get_connection()

    total = connection.execute(
        "SELECT COUNT(*) FROM tickets"
    ).fetchone()[0]

    open_tickets = connection.execute(
        "SELECT COUNT(*) FROM tickets WHERE status = 'Open'"
    ).fetchone()[0]

    in_progress = connection.execute(
        "SELECT COUNT(*) FROM tickets WHERE status = 'In Progress'"
    ).fetchone()[0]

    resolved = connection.execute(
        "SELECT COUNT(*) FROM tickets WHERE status = 'Resolved'"
    ).fetchone()[0]

    connection.close()

    return {
        "total_tickets": total,
        "open_tickets": open_tickets,
        "in_progress": in_progress,
        "resolved": resolved
    }