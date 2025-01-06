from budget import create_budget_table
from database import authenticate_user, create_user_table, register_user
from transaction import add_transaction, create_transactions_table, get_transactions


def main():
    try:
        # Setup (creating tables if they don't exist)
        create_user_table()
        create_transactions_table()
        create_budget_table()

        # Ask for user action (register or login)
        print("Welcome to the Personal Finance Manager!")
        action = input("Would you like to (r)egister or (l)ogin? (r/l): ").strip().lower()

        if action == 'r':
            # Register a new user
            username = input("Enter a username: ").strip()
            password = input("Enter a password: ").strip()
            email = input("Enter your email: ").strip()
            register_user(username, password, email)
            print(f"User {username} registered successfully!")

        elif action == 'l':
            # Login existing user
            username = input("Enter your username: ").strip()
            password = input("Enter your password: ").strip()
            
            if authenticate_user(username, password):
                print("User authenticated successfully!")
            else:
                print("Authentication failed!")
                return

        else:
            print("Invalid action selected! Exiting.")
            return

        # Once the user is authenticated, allow them to interact with the system
        while True:
            print("\nWhat would you like to do?")
            print("1. Add Transaction")
            print("2. View Transactions")
            print("3. Exit")
            
            choice = input("Enter your choice (1-3): ").strip()

            if choice == '1':
                # Add Transaction
                amount = float(input("Enter the amount: "))
                category = input("Enter the category (e.g., Food, Salary): ").strip()
                date = input("Enter the transaction date (YYYY-MM-DD): ").strip()
                transaction_type = input("Enter transaction type (income/expense): ").strip().lower()

                if transaction_type not in ['income', 'expense']:
                    print("Invalid transaction type! Please enter 'income' or 'expense'.")
                    continue

                # Assuming user_id is 1 for this example
                add_transaction(1, amount, category, date, transaction_type)
                print(f"Transaction of {amount} ({transaction_type}) for {category} added.")

            elif choice == '2':
                # View Transactions
                transactions = get_transactions(1)
                if not transactions:
                    print("No transactions found.")
                else:
                    print("Transactions:")
                    for transaction in transactions:
                        print(transaction)

            elif choice == '3':
                # Exit the application
                print("Exiting the application. Goodbye!")
                break

            else:
                print("Invalid choice! Please select between 1-3.")

    except Exception as e:
        print(f"An error occurred: {e}")
main()
