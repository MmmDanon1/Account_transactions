import os.path

from units.functions import open_json

def test_open_json(fixture_open_json, fixture_test_operations):
    assert open_json(fixture_open_json) == fixture_test_operations
