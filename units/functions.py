import json

def open_json(file_name: list[dict]) -> list[dict]:
    """
    открываем файл json
    :return: список библиотек
    """
    with open(file_name, encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data

def sort_data(data: list[dict]) -> list[dict]:
    """
    сортировка данных
    :return:отсортированный список данных
    """
    sort_data_list = []
    for operation in data:
        try:
            if operation["state"] == "EXECUTED":
                sort_data_list.append(operation)
        except:
            continue
    return sort_data_list

def mask_number_card(number_card: dict) -> str:
    """
    маскировка номеров карт
    :return:отсортированный номер карты
    """
    try:
       sort_numbers_card = number_card["from"]
       # mask = list(sort_numbers_card)
       sort_numbers_card = sort_numbers_card.split(' ')
       mask = list(sort_numbers_card[-1])
       if len(mask) == 16:
           mask[-5] = "* "
           mask[-6] = "*"
           mask[-7] = "*"
           mask[-8] = " *"
           mask[-9] = "*"
           mask[-10] = "*"
           mask[-11] = "*"
           mask[-12] = " *"
       else:
           mask[-5] = "* "
           mask[-6] = "*"
           mask[-7] = "*"
           mask[-8] = " *"
           mask[-9] = "*"
           mask[-10] = "*"
           mask[-11] = "*"
           mask[-12] = " *"
           mask[-13] = "*"
           mask[-14] = "*"
           mask[-15] = "*"
           mask[-16] = " *"
       return sort_numbers_card[0] + " " + "".join(mask)
    except:
       return "Номер карты неизвестен"

def mask_number_score(number_score: dict) -> str:
    """
    маскировка номера счета
    :param number_score:
    :return: отсортированный номер счета
    """
    try:
        sort_number_score = number_score["to"]
        sort_number_score_element = sort_number_score.split(" ")
        mask_number_score = list(sort_number_score_element[-1])
        mask_number_score[-5] = "*"
        mask_number_score[-6] = " *"
        number_slice = mask_number_score[-6:]
        return sort_number_score_element[0] + "".join(number_slice)
    except:
        return "счет карты неизвестен"

def sort_data_by_date(data: list[dict]) -> list[dict]:
    """
    сортирует входные данные по дате
    :return: отсортированные данные по дате
    """
    date_obj = sorted(data, key=lambda x: x['date'], reverse=True)
    return date_obj









