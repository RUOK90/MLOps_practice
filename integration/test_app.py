# TODO(everyone): 웹서버의 healthz가 response code 200 확인


import app


def test_healthz():
    assert app.app.test_client().get('/healthz').status_code == 200
