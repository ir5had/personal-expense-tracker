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
    # Get current date as string (e.g., "2025-04-26")
    date = datetime.now().strftime("%Y-%m-%d")

    # Create transaction dictionary
    transaction = {
        "amount": amount,
        "category": category,
        "description": description,
        "date": date
    }

    # Add to transactions list
    transactions.append(transaction)
    return transaction