import unittest
import pytest
import types
try:
    from unittest import mock
except ImportError:
    import mock
from requests import Request, Session

from .utils import mocked_requests_get, mocked_requests_post, mocked_requests_session
from payhere.errors import ValidationError
from payhere.client import Payhere
from payhere.outpayments import Outpayments


class TestOutpayments(unittest.TestCase):

    @mock.patch('requests.post', side_effect=mocked_requests_post)
    def setUp(self, mock_get):
        self.config = {
            "PAYHERE_APP_ID": "110000",
            "PAYHERE_USERNAME": "sdk",
            "PAYHERE_PASSWORD": "sdk@2020"
        }
        client = Outpayments(self.config)
        self.client = client

    def tearDown(self):
        pass

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_client_instantiate(self, mock_get):

        client = Outpayments(self.config)

        assert isinstance(client, Outpayments)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_invalid_uuid(self, mock_get):
        with self.assertRaises(ValidationError):
            config = self.config
            client = Outpayments(config)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_invalid_mobile(self, mock_get):
        with self.assertRaises(ValidationError):
            ref = self.client.transfer(amount="600", mobile="2567721234569", processing_number="123456789", narration="dd")
        with self.assertRaises(ValidationError):
            ref = self.client.transfer(amount="600", mobile="256712123456", processing_number="123456789", narration="dd")

    @mock.patch.object(Payhere, "request", side_effect=mocked_requests_session)
    def test_transfer(self, mock_get):

        ref = self.client.transfer(amount="600", mobile="256772123456", processing_number="123456789", narration="dd")

        assert isinstance(ref, dict)
        assert "processing_number" in ref.keys()

    @mock.patch.object(Payhere, "request", side_effect=mocked_requests_session)
    def test_get_transaction_status(self, mock_get):
        status = self.client.getTransactionStatus("dummy")
        assert isinstance(status, dict)
        assert "amount" in status.keys()
