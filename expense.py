import json
from datetime import datetime

# List to store transactions
transactions = []

def add_transaction(amount, category, description):
    """
    Add a transaction to the transactions list.
    Args:
        amount (float): The transaction amount
        category (str): The transaction category (e.g., Food, Transport)
        description (str): A brief description
    Returns:
        dict: The added transaction
    """
    date = datetime.now().strftime("%Y-%m-%d")
    transaction = {
        "amount": amount,
        "category": category,
        "description": description,
        "date": date
    }
    transactions.append(transaction)
    return transaction

def get_all_transactions():
    """
    Get all transactions.
    Returns:
        list: List of all transaction dictionaries
    """
    return transactions

def get_transactions_by_category(category):
    """
    Get transactions filtered by category (case-insensitive).
    Args:
        category (str): The category to filter by
    Returns:
        list: List of transaction dictionaries matching the category
    """
    return [t for t in transactions if t["category"].lower() == category.lower()]

def get_expense_summary():
    """
    Calculate total spent and per-category totals.
    Returns:
        dict: Dictionary with 'total' (float) and 'categories' (dict of category: total)
    """
    total = 0.0
    categories = {}
    for transaction in transactions:
        amount = transaction["amount"]
        category = transaction["category"]
        total += amount
        categories[category] = categories.get(category, 0.0) + amount
    return {"total": total, "categories": categories}

def load_transactions(filename="expenses.json"):
    """
    Load transactions from a JSON file.
    Args:
        filename (str): The JSON file to load (default: expenses.json)
    """
    global transactions
    try:
        with open(filename, "r") as file:
            transactions = json.load(file)
    except FileNotFoundError:
        transactions = []  # Start with empty list if file doesn't exist
    except json.JSONDecodeError:
        print("Error: Invalid JSON file. Starting with empty transactions.")
        transactions = []

def save_transactions(filename="expenses.json"):
    """
    Save transactions to a JSON file.
    Args:
        filename (str): The JSON file to save to (default: expenses.json)
    """
    try:
        with open(filename, "w") as file:
            json.dump(transactions, file, indent=4)
    except Exception as e:
        print(f"Error saving transactions: {e}")