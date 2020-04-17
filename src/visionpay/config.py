from .errors import ConfigurationError


class VisionpayConfig(object):

    def __init__(self, conf):
        """

        config={

            VISIONPAY_ENVIRONMENT: os.environ.get("VISIONPAY_ENVIRONMENT"),
            VISIONPAY_BASE_URL: os.environ.get("VISIONPAY_BASE_URL"),
            VISIONPAY_VERSION: os.environ.get("VISIONPAY_VERSION"),
            VISIONPAY_APP_ID: os.environ.get("VISIONPAY_APP_ID"),
            VISIONPAY_USERNAME: os.environ.get("VISIONPAY_USERNAME"),
            VISIONPAY_PASSWORD: os.environ.get("VISIONPAY_PASSWORD"),


        }


        """
        self._config = conf

    def get_property(self, property_name):
        if property_name not in self._config.keys():
            return None
        return self._config[property_name]

    @property
    def environment(self):
        return self.get_property('VISIONPAY_ENVIRONMENT') or "sandbox"

    @property
    def version(self):
        return self.get_property('VISIONPAY_VERSION') or "v1"

    @property
    def baseUrl(self):
        if self.environment == "sandbox":
            "http://sandbox.visionpay.ug/" + self.version
        return self.get_property(
            'VISIONPAY_BASE_URL') or "http://sandbox.visionpay.ug/" + self.version

    @property
    def app_id(self):
        key = self.get_property('VISIONPAY_APP_ID')
        if not key:
            raise ConfigurationError(
                "VISIONPAY_APP_ID is missing in the configuration")
        else:
            key

    @property
    def username(self):
        key = self.get_property('VISIONPAY_USERNAME')
        if not key:
            raise ConfigurationError(
                "VISIONPAY_USERNAME is missing in the configuration")
        else:
            key

    @property
    def password(self):
        key = self.get_property('VISIONPAY_PASSWORD')
        if not key:
            raise ConfigurationError(
                "VISIONPAY_PASSWORD is missing in the configuration")
        else:
            return key
