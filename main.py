from expense import (add_transaction, transactions, get_all_transactions,
                     get_transactions_by_category, get_expense_summary,
                     load_transactions, save_transactions)


def main():
    # Load transactions at startup
    load_transactions()

    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Transaction")
        print("2. View All Transactions")
        print("3. View Transactions by Category")
        print("4. Summarize Expenses")
        print("5. Exit")
        choice = input("Enter choice (1-5): ")

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
            transactions_list = get_all_transactions()
            if transactions_list:
                print("\nAll Transactions:")
                for i, t in enumerate(transactions_list, 1):
                    print(f"{i}. Amount: {t['amount']}, Category: {t['category']}, "
                          f"Description: {t['description']}, Date: {t['date']}")
            else:
                print("\nNo transactions available.")
        elif choice == "3":
            category = input("Enter category to filter (e.g., Food, Transport): ").strip()
            if not category:
                print("Category cannot be empty!")
                continue
            transactions_list = get_transactions_by_category(category)
            if transactions_list:
                print(f"\nTransactions for Category '{category}':")
                for i, t in enumerate(transactions_list, 1):
                    print(f"{i}. Amount: {t['amount']}, Category: {t['category']}, "
                          f"Description: {t['description']}, Date: {t['date']}")
            else:
                print(f"\nNo transactions found for category '{category}'.")
        elif choice == "4":
            summary = get_expense_summary()
            print("\nExpense Summary:")
            if summary["total"] > 0:
                print(f"Total Spent: ${summary['total']:.2f}")
                print("By Category:")
                for category, total in summary["categories"].items():
                    print(f"- {category}: ${total:.2f}")
            else:
                print("No expenses to summarize.")
        elif choice == "5":
            transactions_list = get_all_transactions()  # Use function for consistency
            print("\nAll Transactions:")
            if transactions_list:
                for i, t in enumerate(transactions_list, 1):
                    print(f"{i}. Amount: {t['amount']}, Category: {t['category']}, "
                          f"Description: {t['description']}, Date: {t['date']}")
            else:
                print("No transactions added.")
            save_transactions()  # Save transactions before exiting
            print("Transactions saved. Exiting...")
            break
        else:
            print("Invalid choice! Please enter 1-5.")


if __name__ == "__main__":
    main()