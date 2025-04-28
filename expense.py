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