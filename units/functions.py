import json
def open_json(file_name):
    """
    открываем файл json
    :return: [{}]
    """
    with open(file_name, encoding='utf-8') as json_file:
        data = json.load(json_file)

    return data

def sort_data(data):
    """
    сортировка данных
    :return:отсортированный список данных
    """
    sort_data_list = [operation for operation in data if operation["state"] == "EXECUTED"]

    return sort_data_list

def mask_number_card(number_card):
    """
    маскировка номеров карт
    :return:отсортированный номер карты
    """
    for number in number_card:
        sort_numbers_card = number["from"]
        mask = list(sort_numbers_card)
        mask[-5] = "*"
        mask[-6] = "*"
        mask[-7] = "*"
        mask[-8] = "*"
        mask[-9] = "*"
        mask[-10] = "*"

        return("".join(mask))

def mask_number_score(number_score):
    """
    маскировка номера счета
    :param number_score:
    :return: отсортированный номер счета
    """
    pass




