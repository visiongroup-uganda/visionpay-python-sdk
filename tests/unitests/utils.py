import requests
import unittest
try:
    from unittest import mock
except ImportError:
    import mock


class MockResponse:
    def __init__(self, json_data, status_code, headers={}):
        self.json_data = json_data
        self.status_code = status_code
        self.headers = headers

    def json(self):
        return self.json_data


def mocked_requests_get(*args, **kwargs):
    if "/inpayments" in args[0]:
        return MockResponse({
            "amount": 100,
            "msisdn": 4656473839,
            "processingNumber": 947354,
            "narration": "narr",
            "status": "SUCCESSFUL"
        }, 200)

    return MockResponse(None, 404)


def mocked_requests_post(*args, **kwargs):

    if "inpayments" in args[0]:
        return MockResponse({"key2": "value2"}, 200)

    return MockResponse(None, 404)


def mocked_requests_session(*args, **kwargs):
    if "/inpayments" in args[1] and args[0] == 'POST':
        return MockResponse({}, 200)
    elif "transfer" in args[1] and args[0] == 'POST':
        return MockResponse({}, 200)
    elif ("/inpayments" in args[1] or "/outpayments" in args[1]) and args[0] == 'GET':
        return MockResponse({
            "amount": 100,
            "msisdn": 4656473839,
            "processingNumber": 947354,
            "narration": "narr",
            "status": "SUCCESSFUL"
        }, 200)
    else:
        return MockResponse({}, 200)
