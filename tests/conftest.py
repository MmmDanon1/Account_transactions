import os

import pytest as pytest

@pytest.fixture
def fixture_open_json():
    return os.path.join(os.path.dirname(__file__), 'test_operations.json')
@pytest.fixture
def fixture_test_operations():
    return [
  {
    "id": 464419177,
    "state": "CANCELED",
    "date": "2018-07-15T18:44:13.346362",
    "operationAmount": {
      "amount": "71024.64",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод с карты на счет",
    "from": "Visa Gold 9657499677062945",
    "to": "Счет 19213886662094884261"
  },
  {
    "id": 560813069,
    "state": "CANCELED",
    "date": "2019-12-03T04:27:03.427014",
    "operationAmount": {
      "amount": "17628.50",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод с карты на карту",
    "from": "MasterCard 1796816785869527",
    "to": "Visa Classic 7699855375169288"
  },
  {
    "id": 894961746,
    "state": "EXECUTED",
    "date": "2019-08-04T20:17:25.443322",
    "operationAmount": {
      "amount": "2523.44",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 33721541831646393763",
    "to": "Счет 68774571780974952778"
  },
  {
    "id": 360577236,
    "state": "EXECUTED",
    "date": "2019-09-07T07:20:13.889610",
    "operationAmount": {
      "amount": "18536.73",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод с карты на карту",
    "from": "Maestro 4284341727554246",
    "to": "МИР 1582474475547301"
  },
  {
    "id": 285353808,
    "state": "EXECUTED",
    "date": "2018-08-06T16:22:54.643491",
    "operationAmount": {
      "amount": "82946.19",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 12189246980267075758"
  },
  {
    "id": 416017997,
    "state": "EXECUTED",
    "date": "2019-05-07T01:32:37.142797",
    "operationAmount": {
      "amount": "29033.65",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод с карты на карту",
    "from": "МИР 4878656375033856",
    "to": "Maestro 6890749237669619"
  }
]

@pytest.fixture
def selected_datа():
  return [{
    "id": 560813069,
    "state": "CANCELED",
    "date": "2019-12-03T04:27:03.427014",
    "operationAmount": {
      "amount": "17628.50",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод с карты на карту",
    "from": "MasterCard 1796816785869527",
    "to": "Visa Classic 7699855375169288"
  },
  {
    "id": 894961746,
    "state": "EXECUTED",
    "date": "2019-08-04T20:17:25.443322",
    "operationAmount": {
      "amount": "2523.44",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 33721541831646393763",
    "to": "Счет 68774571780974952778"
  },
  {
    "id": 360577236,
    "state": "EXECUTED",
    "date": "2019-09-07T07:20:13.889610",
    "operationAmount": {
      "amount": "18536.73",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод с карты на карту",
    "from": "Maestro 4284341727554246",
    "to": "МИР 1582474475547301"
  },
  {
    "id": 285353808,
    "state": "EXECUTED",
    "date": "2018-08-06T16:22:54.643491",
    "operationAmount": {
      "amount": "82946.19",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 12189246980267075758"
  },
  {
    "id": 416017997,
    "state": "EXECUTED",
    "date": "2019-05-07T01:32:37.142797",
    "operationAmount": {
      "amount": "29033.65",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод с карты на карту",
    "from": "МИР 4878656375033856",
    "to": "Maestro 6890749237669619"
  }
]
@pytest.fixture
def fixture_sort_data():
  return [{
    "id": 894961746,
    "state": "EXECUTED",
    "date": "2019-08-04T20:17:25.443322",
    "operationAmount": {
      "amount": "2523.44",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 33721541831646393763",
    "to": "Счет 68774571780974952778"
  },
  {
    "id": 360577236,
    "state": "EXECUTED",
    "date": "2019-09-07T07:20:13.889610",
    "operationAmount": {
      "amount": "18536.73",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод с карты на карту",
    "from": "Maestro 4284341727554246",
    "to": "МИР 1582474475547301"
  },
  {
    "id": 285353808,
    "state": "EXECUTED",
    "date": "2018-08-06T16:22:54.643491",
    "operationAmount": {
      "amount": "82946.19",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 12189246980267075758"
  },
  {
    "id": 416017997,
    "state": "EXECUTED",
    "date": "2019-05-07T01:32:37.142797",
    "operationAmount": {
      "amount": "29033.65",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод с карты на карту",
    "from": "МИР 4878656375033856",
    "to": "Maestro 6890749237669619"
  }
]



