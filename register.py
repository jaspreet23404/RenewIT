import bcrypt
from db_config import connect_user_db

def register_user(username, email, password):
    connection = connect_user_db()
    if not connection:
        return
    
    cursor = connection.cursor()
    
    # Hash the password
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    try:
        query = "INSERT INTO users (username, email, password_hash) VALUES (%s, %s, %s)"
        cursor.execute(query, (username, email, hashed))
        connection.commit()
        print("✅ User registered successfully!")
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        cursor.close()
        connection.close()

