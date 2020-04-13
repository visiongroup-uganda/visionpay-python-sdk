from .errors import ConfigurationError


class PayhereConfig(object):

    def __init__(self, conf):
        """

        config={

            PAYHERE_ENVIRONMENT: os.environ.get("PAYHERE_ENVIRONMENT"),
            PAYHERE_BASE_URL: os.environ.get("PAYHERE_BASE_URL"),
            PAYHERE_VERSION: os.environ.get("PAYHERE_VERSION"),
            PAYHERE_APP_ID: os.environ.get("PAYHERE_APP_ID"),
            PAYHERE_USERNAME: os.environ.get("PAYHERE_USERNAME"),
            PAYHERE_PASSWORD: os.environ.get("PAYHERE_PASSWORD"),


        }


        """
        self._config = conf

    def get_property(self, property_name):
        if property_name not in self._config.keys():
            return None
        return self._config[property_name]

    @property
    def environment(self):
        return self.get_property('PAYHERE_ENVIRONMENT') or "sandbox"

    @property
    def version(self):
        return self.get_property('PAYHERE_VERSION') or "v1"    

    @property
    def baseUrl(self):
        if self.environment == "sandbox":
            "http://sandbox.payhere.africa/" + self.version
        return self.get_property(
            'PAYHERE_BASE_URL') or "http://sandbox.payhere.africa/" + self.version

    @property
    def app_id(self):
        key = self.get_property('PAYHERE_APP_ID')
        if not key:
            raise ConfigurationError(
                "PAYHERE_APP_ID is missing in the configuration")
        else:
            key
   
    @property
    def username(self):
        key = self.get_property('PAYHERE_USERNAME')
        if not key:
            raise ConfigurationError(
                "PAYHERE_USERNAME is missing in the configuration")
        else:
            key

    @property
    def password(self):
        key = self.get_property('PAYHERE_PASSWORD')
        if not key:
            raise ConfigurationError(
                "PAYHERE_PASSWORD is missing in the configuration")
        else:
            return key
