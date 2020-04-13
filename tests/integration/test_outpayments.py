from pytest_bdd import scenario, given, when, then, parsers
import re
import os
import pytest
from click.testing import CliRunner
from payhere.outpayments import Outpayments

pytest.globalDict = {}


@scenario('features/outpayments.feature', 'Transfer Money to another account')
def test_outpayments():
    pass


@given("I have a valid APP-ID, username and password")
def user_credentials():
    config = {
        "PAYHERE_APP_ID": os.environ.get("PAYHERE_APP_ID"),
        "PAYHERE_USERNAME": os.environ.get("PAYHERE_USERNAME"),
        "PAYHERE_PASSWORD": os.environ.get("PAYHERE_PASSWORD"),
    }
    client = Outpayments(config)
    pytest.globalDict["client"] = client


@when("I transfer with the following payment details\n| note         | amount | message | mobile     | product_id |\n| test payment | 600    | message | 0782631873 |")
def successful_transfer():
    ref = pytest.globalDict["client"].transfer(
        amount="600", mobile="256772123456", processing_number="123456789", narration="dd")
    pytest.globalDict["ref"] = ref

    assert isinstance(ref, dict)
    assert "processing_number" in ref.keys()


@when("I check for transaction Status")
def check_transaction_status():
    status = pytest.globalDict["client"].getTransactionStatus(pytest.globalDict["ref"]["processing_number"])
    pytest.globalDict["status"] = status
    assert isinstance(status, dict)
    assert "amount" in status.keys()


@then("It should be successful")
def sucessful_transaction():
    assert pytest.globalDict["status"]["status"] == "SUCCESSFUL"
