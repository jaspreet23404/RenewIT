# manage_dates.py
import bcrypt
from db_config import connect_docs_db

def add_document(user_email, doc_name, doc_type, expiry_date):
    conn = connect_docs_db()
    cursor = conn.cursor()

    query = "INSERT INTO documents (user_email, doc_name, doc_type, expiry_date) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (user_email, doc_name, doc_type, expiry_date))
    conn.commit()

    print("✅ Document added successfully!")
    conn.close()

def view_documents(user_email):
    conn = connect_docs_db()
    cursor = conn.cursor()

    query = "SELECT doc_name, doc_type, expiry_date FROM documents WHERE user_email = %s"
    cursor.execute(query, (user_email,))
    result = cursor.fetchall()

    if not result:
        print("⚠️ No documents found.")
    else:
        print("\n📋 Your Saved Documents:")
        for row in result:
            print(f"- {row[0]} ({row[1]}), expires on {row[2]}")

    conn.close()
