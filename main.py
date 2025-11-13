from register import register_user
from login import login_user
from manage_dates import add_document, view_documents
from reminder_preference import set_reminder_preference
from dashboard import dashboard

print("=== Welcome to RenewIT: Document Expiration Reminder System ===")
choice = input("Enter 1 to Register or 2 to Login: ")

if choice == "1":
    username = input("Enter your Name: ")
    email = input("Enter your Email: ")
    password = input("Enter your Password: ")
    register_user(username, email, password)

elif choice == "2":
    email = input("Enter your Email: ")
    password = input("Enter your Password: ")
    user_name = login_user(email, password)
    
    if user_name:
        print(f"\n✅ Welcome, {user_name}!")
        while True:
            print("\n--- MAIN MENU ---")
            print("1. Add Document")
            print("2. View Documents")
            print("3. Set Reminder Preference")
            print("4. View Dashboard")
            print("5. Logout")

            ch = input("Enter your choice: ")

            if ch == "1":
                doc_name = input("Document Name: ")
                doc_type = input("Document Type: ")
                expiry_date = input("Expiry Date (YYYY-MM-DD): ")
                add_document(email, doc_name, doc_type, expiry_date)

            elif ch == "2":
                view_documents(email)

            elif ch == "3":
                days = int(input("Enter number of days before expiry to get reminders: "))
                reminder_type = input("Enter reminder type (email/sms): ").lower()
                set_reminder_preference(email, days, reminder_type)


            elif ch == "4":
                dashboard(email)

            elif ch == "5":
                print("👋 Logged out successfully. Goodbye!")
                break

            else:
                print("❌ Invalid choice. Please try again.")
else:
    print("❌ Invalid input. Please restart and enter 1 or 2.")
