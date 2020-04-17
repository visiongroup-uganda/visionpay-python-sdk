import uuid

from .client import Visionpay
from .utils import validate_phone_number


class Inpayments(Visionpay, object):
    def getTransactionStatus(
            self,
            transaction_id,
            **kwargs):
        url = "/inpayments"

        return super(Inpayments, self).getTransactionStatus(
            transaction_id, url)

    def requestToPay(
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

        url = "{0}/inpayments".format(super(Inpayments, self).config.baseUrl)
        self.request("POST", url, headers, data)
        return {"transaction_ref": ref}
