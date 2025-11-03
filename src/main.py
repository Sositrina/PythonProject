from src.reading_files import get_transactions
from src.transaction_sorting import process_transactions
from src.transaction_filter import file_selection, transaction_status

def main():
    file_choice = file_selection()
    transactions = get_transactions(file_choice)
    status = transaction_status()

    filtered = [t for t in transactions if t.get("state", "").upper() == status.upper()
                or t.get("status", "").upper() == status.upper()]

    process_transactions(filtered)




if __name__ == "__main__":
    main()
