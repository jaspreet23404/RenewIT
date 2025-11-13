import bcrypt
from db_config import connect_docs_db

def set_reminder_preference(email, days_before_expiration, reminder_type):
    """
    Saves or updates user's reminder preferences (days + type) in the document_and_reminders_database.
    """
    try:
        connection = connect_docs_db()
        if connection is None:
            print("❌ Could not connect to documents database.")
            return

        cursor = connection.cursor()

        # Check if the user already has a preference
        cursor.execute("SELECT * FROM reminder_preferences WHERE email = %s", (email,))
        existing = cursor.fetchone()

        if existing:
            cursor.execute("""
                UPDATE reminder_preferences
                SET days_before_expiration = %s, reminder_type = %s
                WHERE email = %s
            """, (days_before_expiration, reminder_type, email))
        else:
            cursor.execute("""
                INSERT INTO reminder_preferences (email, days_before_expiration, reminder_type)
                VALUES (%s, %s, %s)
            """, (email, days_before_expiration, reminder_type))

        connection.commit()
        print(f"✅ Reminder preference set to {days_before_expiration} days before expiry via {reminder_type.upper()}.")

    except Error as e:
        print(f"❌ Error while setting reminder preference: {e}")

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
