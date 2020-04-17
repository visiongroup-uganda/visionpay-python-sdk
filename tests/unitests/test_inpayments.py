import unittest
import pytest
import types
try:
    from unittest import mock
except ImportError:
    import mock

from requests import Request, Session

from .utils import mocked_requests_get, mocked_requests_post, mocked_requests_session
from visionpay.errors import ValidationError
from visionpay.client import Visionpay
from visionpay.inpayments import Inpayments


class TestInpayments(unittest.TestCase):

    @mock.patch('requests.post', side_effect=mocked_requests_post)
    def setUp(self, mock_get):
        self.config = {
            "VISIONPAY_APP_ID": "110000",
            "VISIONPAY_USERNAME": "sdk",
            "VISIONPAY_PASSWORD": "sdk@2020"
        }
        client = Inpayments(self.config)
        self.client = client

    def tearDown(self):
        pass

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_client_instantiate(self, mock_get):

        client = Inpayments(self.config)

        assert isinstance(client, Inpayments)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_invalid_uuid(self, mock_get):
        with self.assertRaises(ValidationError):
            config = self.config
            client = Inpayments(config)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_invalid_mobile(self, mock_get):
        with self.assertRaises(ValidationError):
            ref = self.client.requestToPay(mobile="256712123456", amount="600",
                                           processing_number="123456789", narration="dd")
        with self.assertRaises(ValidationError):
            ref = self.client.requestToPay(mobile="254712123456", amount="600",
                                           processing_number="123456789", narration="dd")

    @mock.patch.object(Visionpay, "request", side_effect=mocked_requests_session)
    def test_request_to_pay(self, mock_get):

        ref = self.client.requestToPay(mobile="256772123456", amount="600", processing_number="123456789", narration="dd")

        assert isinstance(ref, dict)
        assert "processing_number" in ref.keys()

    @mock.patch.object(Visionpay, "request", side_effect=mocked_requests_session)
    def test_get_transaction_status(self, mock_get):
        status = self.client.getTransactionStatus("dummy")
        assert isinstance(status, dict)
        assert "amount" in status.keys()
