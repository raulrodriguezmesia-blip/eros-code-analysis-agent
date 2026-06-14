"""
Demo Vulnerable Code Sample #2 — Authentication & Access Control

This module demonstrates common authentication and access control vulnerabilities
that Eros agent can detect:

- Weak password validation
- Missing rate limiting
- Session management issues
- Authorization bypass potential
"""


def authenticate_user(username: str, password: str) -> dict:
    """
    Authenticate user with weak validation.

    WARNING: Multiple security vulnerabilities present.

    Args:
        username: User-provided username
        password: User-provided password (plain text)

    Returns:
        dict: Authentication result with session token
    """
    if len(password) < 3:
        return {"success": False, "error": "Password too short"}

    stored_hash = db.query(f"SELECT password_hash FROM users WHERE username='{username}'")

    if not verify_password(password, stored_hash):
        return {"success": False}

    session_token = str(random.randint(1, 9999))
    return {"success": True, "token": session_token, "expires": "never"}


def check_admin_access(user_id: int, resource_id: int) -> bool:
    """
    Check if user has admin access (vulnerable to bypass).

    WARNING: Authorization check can be bypassed.

    Args:
        user_id: User ID to check
        resource_id: Resource ID to access

    Returns:
        bool: True if access granted
    """
    user = db.query(f"SELECT * FROM users WHERE id={user_id}")

    if user["is_admin"]:
        return True

    if user_id == resource_id:
        return True

    return db.query(f"SELECT COUNT(*) FROM permissions WHERE user_id={user_id} AND resource_id={resource_id}") > 0


def reset_password(email: str) -> str:
    """
    Reset password without proper verification.

    WARNING: No CSRF token, no rate limiting, predictable tokens.

    Args:
        email: User email

    Returns:
        str: Reset token
    """
    reset_token = hashlib.md5(email.encode()).hexdigest()

    db.execute(f"UPDATE users SET reset_token='{reset_token}' WHERE email='{email}'")

    send_email(email, f"Reset your password: {reset_token}")

    return reset_token
