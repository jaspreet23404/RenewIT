from mysql.connector import Error
from datetime import datetime
from db_config import connect_user_db, connect_docs_db


def view_dashboard(user_email):
    """Display the user's dashboard with document stats and reminder preferences."""
    try:
        # Connect to the documents database
        docs_conn = connect_docs_db()
        cursor_docs = docs_conn.cursor()

        # 1️⃣ Total documents for this user
        cursor_docs.execute("SELECT COUNT(*) FROM documents WHERE user_email = %s", (user_email,))
        total_docs = cursor_docs.fetchone()[0]

        # 2️⃣ Documents expiring within the next 30 days
        cursor_docs.execute("""
            SELECT COUNT(*) 
            FROM documents 
            WHERE user_email = %s AND expiry_date BETWEEN CURDATE() AND DATE_ADD(CURDATE(), INTERVAL 30 DAY)
        """, (user_email,))
        expiring_soon = cursor_docs.fetchone()[0]

        # 3️⃣ Nearest upcoming expiry
        cursor_docs.execute("""
            SELECT doc_name, expiry_date 
            FROM documents 
            WHERE user_email = %s 
            ORDER BY expiry_date ASC 
            LIMIT 1
        """, (user_email,))
        next_expiry = cursor_docs.fetchone()

        # Connect to user database to get reminder preference
        user_conn = connect_user_db()
        cursor_user = user_conn.cursor()
        cursor_user.execute("SELECT reminder_days FROM reminder_preferences WHERE user_email = %s", (user_email,))
        reminder_pref = cursor_user.fetchone()

        # Display the dashboard
        print("\n==================== 📊 DASHBOARD ====================")
        print(f"📁 Total Documents: {total_docs}")
        print(f"⏳ Expiring in Next 30 Days: {expiring_soon}")

        if next_expiry:
            print(f"⚠️ Next Expiry: {next_expiry[0]} on {next_expiry[1]}")
        else:
            print("✅ No upcoming expirations found.")

        if reminder_pref:
            print(f"🔔 Reminder Set: {reminder_pref[0]} days before expiry")
        else:
            print("🔕 No reminder preference set.")
        print("======================================================\n")

    except Error as e:
        print(f"❌ Error while loading dashboard: {e}")

    finally:
        # Close all connections
        if 'cursor_docs' in locals(): cursor_docs.close()
        if 'docs_conn' in locals() and docs_conn.is_connected(): docs_conn.close()
        if 'cursor_user' in locals(): cursor_user.close()
        if 'user_conn' in locals() and user_conn.is_connected(): user_conn.close()
