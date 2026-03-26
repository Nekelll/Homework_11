def filter_by_state(transaction, state="EXECUTED"):

    new_transactions = []

    for item in transaction:
        if item.get("state") == state:
            new_transactions.append(item)

    return new_transactions


def sort_by_date(transaction, reverse=True):

    pairs = []

    for item in transaction:
        date = item['date']
        pairs.append((date, item))

    pairs.sort(reverse=reverse)

    sorted_list = []
    for date, pair in pairs:
        sorted_list.append(pair)

    return sorted_list


if __name__ == "__main__":
    transactions = [
        {"id": 1, "state": "EXECUTED", "date": "2024-01-15T10:30:00.000", "amount": 5000},
        {"id": 2, "state": "CANCELED", "date": "2024-01-10T14:20:00.000", "amount": 1000},
        {"id": 3, "state": "EXECUTED", "date": "2024-01-20T09:15:00.000", "amount": 2500}
    ]

# executed = filter_by_state(transactions)
# canceled = filter_by_state(transactions, state="CANCELED")
#
# print(executed)
# print(canceled)
print(sort_by_date(transactions))
# print(sort_by_date(transactions, False))

