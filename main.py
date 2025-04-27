from expense import add_transaction, transactions  # Added transactions import

def main():
    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Transaction")
        print("2. Exit")
        choice = input("Enter choice (1-2): ")

        if choice == "1":
            try:
                amount = float(input("Enter amount: "))
                if amount <= 0:
                    print("Amount must be positive!")
                    continue
                category = input("Enter category (e.g., Food, Transport): ").strip()
                if not category:
                    print("Category cannot be empty!")
                    continue
                description = input("Enter description: ").strip()
                if not description:
                    print("Description cannot be empty!")
                    continue

                transaction = add_transaction(amount, category, description)
                print("Transaction added successfully:")
                print(f"Amount: {transaction['amount']}, Category: {transaction['category']}, "
                      f"Description: {transaction['description']}, Date: {transaction['date']}")
            except ValueError:
                print("Invalid amount! Please enter a number.")
        elif choice == "2":
            print("\nAll Transactions:")
            if transactions:
                for i, t in enumerate(transactions, 1):
                    print(f"{i}. Amount: {t['amount']}, Category: {t['category']}, "
                          f"Description: {t['description']}, Date: {t['date']}")
            else:
                print("No transactions added.")
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please enter 1 or 2.")

if __name__ == "__main__":
    main()