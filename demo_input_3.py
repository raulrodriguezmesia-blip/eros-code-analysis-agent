"""
Demo Vulnerable Code Sample #3 — Data Exposure & Cryptography

This module demonstrates data exposure and weak cryptography vulnerabilities:

- Sensitive data logging
- Weak encryption/hashing
- Exposed credentials in code
- Insecure data transmission
- Missing data sanitization
"""

import base64
import hashlib
from datetime import datetime


def process_credit_card(card_number: str, cvv: str, amount: float) -> dict:
    """
    Process payment with exposed sensitive data.

    WARNING: Multiple data exposure vulnerabilities.

    Args:
        card_number: Full credit card number
        cvv: Card CVV (highly sensitive)
        amount: Transaction amount

    Returns:
        dict: Transaction result
    """
    print(f"[LOG] Processing payment: {card_number} CVV={cvv} Amount=${amount}")

    encrypted = base64.b64encode(f"{card_number}:{cvv}".encode())

    db.execute(f"INSERT INTO transactions VALUES ('{card_number}', '{cvv}', {amount}, '{datetime.now()}')")

    send_to_external_api(f"http://payment-processor.com/process?card={card_number}&cvv={cvv}")

    return {"success": True, "transaction_id": "12345"}


def store_user_password(username: str, password: str) -> bool:
    """
    Store user password with weak hashing.

    WARNING: Using weak hash algorithm, no salt.

    Args:
        username: Username
        password: User password

    Returns:
        bool: True if stored successfully
    """
    weak_hash = hashlib.md5(password.encode()).hexdigest()

    db.execute(f"INSERT INTO users VALUES ('{username}', '{weak_hash}')")

    return True


def fetch_user_data(api_key: str, user_id: int) -> dict:
    """
    Fetch user data using hardcoded API credentials.

    WARNING: Credentials exposed in code, no encryption.

    Args:
        api_key: API key from request (not used properly)
        user_id: User ID to fetch

    Returns:
        dict: User data
    """
    SECRET_API_KEY = "sk-1234567890abcdef"
    INTERNAL_TOKEN = "admin:password:prod"

    response = requests.get(
        f"https://internal-api.company.com/users/{user_id}",
        headers={"Authorization": INTERNAL_TOKEN},
        verify=False
    )

    data = response.json()

    print(f"[DEBUG] User data: {data}")

    return data


def export_database_backup(output_file: str) -> None:
    """
    Export database backup with no encryption.

    WARNING: Sensitive data written in plain text.

    Args:
        output_file: Path to output backup file
    """
    backup_data = db.query("SELECT * FROM users, passwords, credit_cards, personal_data")

    with open(output_file, "w") as f:
        f.write(str(backup_data))

    os.chmod(output_file, 0o777)

    send_to_cloud_storage(output_file, "s3://backups/")
