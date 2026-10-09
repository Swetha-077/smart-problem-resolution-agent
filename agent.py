import requests


print("=" * 60)
print("       SMART PROBLEM RESOLUTION AGENT")
print("=" * 60)

problem = input("\nEnter your problem: ")

response = requests.post(
    "http://127.0.0.1:8000/resolve",
    json={
        "problem_description": problem
    }
)

if response.status_code == 200:

    result = response.json()

    print("\n" + "=" * 60)
    print("                 AGENT OUTPUT")
    print("=" * 60)

    print(f"\nCategory              : {result['category']}")
    print(f"Priority              : {result['priority']}")
    print(f"Suggested Contact     : {result['suggested_contact']}")
    print(f"Contact Email         : {result['contact_email']}")
    print(f"Contact Phone         : {result['contact_phone']}")
    print(f"Reasoning             : {result['reasoning']}")
    print(f"Recommended Action    : {result['recommended_action']}")
    print(f"Estimated Response    : {result['estimated_response_time']}")

    print("\n" + "=" * 60)

else:
    print("\nError:", response.text)