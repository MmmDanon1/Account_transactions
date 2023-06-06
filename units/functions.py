import json
def open_json(file_name):
    """
    открываем файл json
    :return: список библиотек
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
    for number in number_score:
        sort_number_score = number["to"]

        sort_number_score_element = sort_number_score.split(" ")
        mask_number_score = list(sort_number_score_element[1])
        mask_number_score[-5] = "*"
        mask_number_score[-6] = " *"
        number_slice = mask_number_score[-6:]

        return sort_number_score_element[0] + "".join(number_slice)




