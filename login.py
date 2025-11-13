import bcrypt
from db_config import connect_user_db

def login_user(email, password):
    conn = connect_user_db()
    cursor = conn.cursor()

    query = "SELECT username, password_hash FROM users WHERE email = %s"
    cursor.execute(query, (email,))
    result = cursor.fetchone()

    if result and bcrypt.checkpw(password.encode('utf-8'), result[1].encode('utf-8')):
        print(f"✅ Login successful! Welcome, {result[0]}.")
        conn.close()
        return result[0]
    else:
        print("❌ Invalid credentials.")
        conn.close()
        return None
