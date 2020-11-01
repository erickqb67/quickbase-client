import json
import pathlib

import pytest


def _data_from_file(data_file):
    p = pathlib.Path(__file__).parent / 'data' / 'mocks' / data_file
    with open(str(p), 'r') as f:
        return json.load(f)


_mocks = [
    ('GET', '/apps/abcdefg', 'get_app.json'),
    ('GET', '/tables?appId=abcdefg', 'get_tables_for_app.json'),
    ('GET', '/tables/aaaaaa?appId=abcdefg', 'get_table.json'),
]


@pytest.fixture()
def qb_api_mock(requests_mock):
    for method, endpoint, f in _mocks:
        requests_mock.request(
            method, f'https://api.quickbase.com/v1{endpoint}', json=_data_from_file(f))