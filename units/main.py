from units.functions import sort_data, open_json, sort_data_by_date, mask_number_score, mask_number_card

def account_transactions():
    """
    выполнение операции по счетам
    :return:операции по счетам
    """
    sorted_data_operations = sort_data(open_json('operations.json'))
    sorted_account_transactions = sort_data_by_date(sorted_data_operations)
    for operation in sorted_account_transactions[0:5]:
        mask_card = mask_number_card(operation)
        mask_score = mask_number_score(operation)
        time_operation = '.'.join(operation["date"][0:10].split('-')[::-1])
        print(f"{time_operation}\n Перевод организации {mask_card} -> {mask_score}")
        print()

account_transactions()





