from wirecardpy.utils import util
from wirecardpy.utils import constants


class Anticipation(object):
    @staticmethod
    def estimates(access_token, amount):
        url = util.get_base_url() + constants.ANTICIPATION_ESTIMATIVE_URL.format(amount)
        return util.request_post(url, {})

    @staticmethod
    def execute(access_token, amount):
        pass
