# Código vulnerable para demostrar Eros Code Analysis Agent

def process_payment(card_number, amount):
    # SQL Injection vulnerabilidad
    query = f"UPDATE accounts SET balance = balance - {amount} WHERE card='{card_number}'"
    
    # Hardcoded credentials
    api_key = "sk-12345abcdef"
    
    # No validación de entrada
    result = db.execute(query)
    return {"success": True, "balance": result}

# Código con problemas de performance
def get_user_data(user_id):
    users = []  # Query N+1
    orders = []  # Sin paginación
    for i in range(1000000):
        users.append(query(f"SELECT * FROM users WHERE id={i}"))
    return users