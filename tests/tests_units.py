import os.path

from units.functions import open_json, sort_data, mask_number_card, mask_number_score


def test_open_json(fixture_open_json, fixture_test_operations):
    assert open_json(fixture_open_json) == fixture_test_operations

def test_sort_date(selected_datа, fixture_sort_data):
    assert sort_data(selected_datа) == fixture_sort_data

def test_mask_number_card(sort_data_user, fixture_number_card):
    assert mask_number_card(sort_data_user) == fixture_number_card

def test_mask_number_score(sort_data_user, fixture_mask_number_score):
    assert mask_number_score(sort_data_user) == fixture_mask_number_score