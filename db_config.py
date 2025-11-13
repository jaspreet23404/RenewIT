import mysql.connector
from mysql.connector import Error

# --- Connect to user database ---
def connect_user_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",         
            password="admin123",  
            database="user_database"
        )
        if connection.is_connected():
            print("✅ Connected to user_database")
            return connection
    except Error as e:
        print(f"❌ Error: {e}")
        return None


# --- Connect to document and reminders database ---
def connect_docs_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",         
            password="admin123",  
            database="document_and_reminders_database"
        )
        if connection.is_connected():
            print("✅ Connected to document_and_reminders_database")
            return connection
    except Error as e:
        print(f"❌ Error: {e}")
        return None
