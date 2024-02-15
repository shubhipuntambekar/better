import requests


def test_register_resource_success():
    url = 'http://127.0.0.1:5000/user'
    data = {'mobile_no': '9424051980'}
    response = requests.post(url=url, json=data)
    assert response.status_code == 200


def test_register_resource_failure():
    url = 'http://127.0.0.1:5000/user'
    data = {'mobile_no': '2405180332'}
    response = requests.post(url=url, json=data)
    assert response.status_code == 400
