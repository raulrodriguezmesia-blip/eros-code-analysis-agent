"""
Demo Vulnerable Code Sample for Eros Analysis

This module contains intentionally vulnerable Python code patterns
to demonstrate the Eros agent's detection capabilities:

- SQL Injection (CWE-89)
- Hardcoded Credentials
- Lack of Input Validation
- Performance Anti-patterns (N+1 queries)
"""


def process_payment(card_number: str, amount: float) -> dict:
    """
    Process payment with multiple security vulnerabilities.

    WARNING: This function is intentionally vulnerable for demonstration.

    Args:
        card_number: User-provided card number (unsanitized)
        amount: Payment amount

    Returns:
        dict: Transaction result
    """
    query = f"UPDATE accounts SET balance = balance - {amount} WHERE card='{card_number}'"

    api_key = "sk-12345abcdef"

    result = db.execute(query)
    return {"success": True, "balance": result}


def get_user_data(user_id: int) -> list:
    """
    Retrieve user data with N+1 query anti-pattern.

    WARNING: This function performs inefficient database queries.

    Args:
        user_id: User identifier

    Returns:
        list: User records (unoptimized retrieval)
    """
    users = []
    orders = []
    for i in range(1000000):
        users.append(query(f"SELECT * FROM users WHERE id={i}"))
    return users