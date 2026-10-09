CATEGORY_KEYWORDS = {
    "Finance": [
        "salary",
        "salary payment",
        "payment",
        "pay",
        "payroll",
        "money",
        "expense",
        "reimbursement",
        "invoice",
        "fee",
        "refund",
        "transaction",
        "financial",
        "bank",
        "billing",
        "account"
    ],

    "HR": [
        "leave",
        "employee",
        "attendance",
        "joining",
        "resignation",
        "holiday",
        "hr",
        "human resource"
    ],

    "IT": [
        "wifi",
        "wi-fi",
        "internet",
        "computer",
        "laptop",
        "software",
        "hardware",
        "network",
        "printer",
        "projector",
        "system",
        "login",
        "password",
        "email",
        "website"
    ],

    "Facilities": [
        "air conditioner",
        "ac",
        "classroom",
        "fan",
        "light",
        "electricity",
        "water",
        "plumbing",
        "furniture",
        "room",
        "building",
        "maintenance"
    ],

    "Security": [
        "security",
        "unauthorized",
        "intruder",
        "theft",
        "stolen",
        "danger",
        "threat",
        "restricted",
        "suspicious"
    ]
}


PRIORITY_KEYWORDS = {
    "Critical": [
        "emergency",
        "fire",
        "accident",
        "danger",
        "life threatening"
    ],

    "High": [
        "urgent",
        "critical",
        "not working",
        "error",
        "failed",
        "failure",
        "security",
        "stolen"
    ],

    "Medium": [
        "issue",
        "problem",
        "unable",
        "need",
        "request"
    ],

    "Low": [
        "question",
        "information",
        "suggestion"
    ]
}


DEPARTMENT_DETAILS = {
    "IT": {
        "contact": "IT Department",
        "email": "it-support@company.com",
        "phone": "+1-800-555-0101",
        "time": "Within 2 hours"
    },

    "HR": {
        "contact": "HR Department",
        "email": "hr@company.com",
        "phone": "+1-800-555-0102",
        "time": "Within 1 business day"
    },

    "Finance": {
        "contact": "Finance Department",
        "email": "finance@company.com",
        "phone": "+1-800-555-0103",
        "time": "Within 1 business day"
    },

    "Facilities": {
        "contact": "Facilities Department",
        "email": "facilities@company.com",
        "phone": "+1-800-555-0104",
        "time": "Within 4 hours"
    },

    "Security": {
        "contact": "Security Department",
        "email": "security@company.com",
        "phone": "+1-800-555-0105",
        "time": "Immediately"
    }
}


def detect_category(problem):
    text = problem.lower()

    scores = {}

    for category, keywords in CATEGORY_KEYWORDS.items():
        score = 0

        for keyword in keywords:
            if keyword in text:
                # Longer phrases get higher importance
                if " " in keyword:
                    score += 3
                else:
                    score += 1

        scores[category] = score

    # Select category with highest score
    best_category = max(scores, key=scores.get)

    # If no keyword matched
    if scores[best_category] == 0:
        return "General"

    return best_category


def detect_priority(problem):
    text = problem.lower()

    for priority in ["Critical", "High", "Medium", "Low"]:
        for keyword in PRIORITY_KEYWORDS[priority]:
            if keyword in text:
                return priority

    return "Medium"


def resolve_problem(problem):
    category = detect_category(problem)
    priority = detect_priority(problem)

    if category == "General":
        return {
            "category": "General",
            "priority": priority,
            "reasoning": "The problem does not clearly match a specific department.",
            "suggested_contact": "Help Desk",
            "contact_email": "helpdesk@company.com",
            "contact_phone": "+1-800-555-0100",
            "recommended_action": "Contact the help desk and provide the complete problem details.",
            "estimated_response_time": "Within 1 business day"
        }

    details = DEPARTMENT_DETAILS[category]

    return {
        "category": category,
        "priority": priority,
        "reasoning": (
            f"The problem contains keywords associated with the "
            f"{category} department."
        ),
        "suggested_contact": details["contact"],
        "contact_email": details["email"],
        "contact_phone": details["phone"],
        "recommended_action": (
            f"Contact {details['contact']} and provide the problem details "
            f"so it can be handled appropriately."
        ),
        "estimated_response_time": details["time"]
    }