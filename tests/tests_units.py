import os.path

from units.functions import open_json, sort_date


def test_open_json(fixture_open_json, fixture_test_operations):
    assert open_json(fixture_open_json) == fixture_test_operations

def test_sort_date(selected_datа, fixture_sort_data):
    assert sort_date(selected_datа) == fixture_sort_data