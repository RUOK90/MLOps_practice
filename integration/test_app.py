# TODO(everyone): 웹서버의 healthz가 response code 200 확인


import requests


def test_healthz():
    assert requests.get('http://127.0.0.1:5000/healthz').status_code == 200
