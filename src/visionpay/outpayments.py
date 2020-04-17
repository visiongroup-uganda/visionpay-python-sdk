import uuid

from .client import Visionpay
from .utils import validate_phone_number


class Outpayments(Visionpay, object):
    def getTransactionStatus(
            self,
            transaction_id,
            **kwargs):
        url = "/outpayments"

        return super(Outpayments, self).getTransactionStatus(
            transaction_id, url)

    def transfer(
            self,
            mobile,
            amount,
            processing_number,
            narration="",
            **kwargs):
            # type: (String,String,String,String,String,String,String) -> json
        ref = str(uuid.uuid4())
        data = {
            "msisdn": validate_phone_number(mobile),
            "amount": str(amount),
            "processingNumber": processing_number,
            "narration": narration}

        url = "{0}/outpayments".format(super(Outpayments, self).config.baseUrl)
        self.request("POST", url, headers, data)
        return {"transaction_ref": ref}
