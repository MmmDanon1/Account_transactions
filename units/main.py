from datetime import datetime

from units.functions import sort_data, open_json, sort_data_by_date, mask_number_score, mask_number_card

def account_transactions():
    """
    выполнение операции по счетам
    :return:операции по счетам
    """
    sorted_data_operations = sort_data(open_json('operations.json'))
    sorted_account_transactions = sort_data_by_date(sorted_data_operations)

    first_operation = sorted_account_transactions[0]
    mask_card = mask_number_card(first_operation)
    mask_score = mask_number_score(first_operation)
    time_operation = datetime.strptime(first_operation["date"], "%Y-%m-%dT%H:%M:%S.%f")

    second_operation = sorted_account_transactions[1]
    mask_card_1 = mask_number_card(second_operation)
    mask_score_1 = mask_number_score(second_operation)
    time_operation_1 = datetime.strptime(second_operation["date"], "%Y-%m-%dT%H:%M:%S.%f")

    third_operation = sorted_account_transactions[2]
    mask_card_2 = mask_number_card(third_operation)
    mask_score_2 = mask_number_score(third_operation)
    time_operation_2 = datetime.strptime(third_operation["date"], "%Y-%m-%dT%H:%M:%S.%f")

    fourth_operation = sorted_account_transactions[3]
    mask_card_3 = mask_number_card(fourth_operation)
    mask_score_3 = mask_number_score(fourth_operation)
    time_operation_3 = datetime.strptime(fourth_operation["date"], "%Y-%m-%dT%H:%M:%S.%f")

    fifth_operation = sorted_account_transactions[4]
    mask_card_4 = mask_number_card(fifth_operation)
    mask_score_4 = mask_number_score(fifth_operation)
    time_operation_4 = datetime.strptime(fifth_operation["date"], "%Y-%m-%dT%H:%M:%S.%f")

    print(f"{time_operation}\n Перевод организации {mask_card} -> {mask_score}")
    print()
    print(f"{time_operation_1}\n Перевод организации {mask_card_1} -> {mask_score_1}")
    print()
    print(f"{time_operation_2}\n Перевод организации {mask_card_2} -> {mask_score_2}")
    print()
    print(f"{time_operation_3}\n Перевод организации {mask_card_3} -> {mask_score_3}")
    print()
    print(f"{time_operation_4}\n Перевод организации {mask_card_4} -> {mask_score_4}")

account_transactions()





