from wirecardpy import util
from wirecardpy.utils import constants


class Payment(object):
    @staticmethod
    def create(order_id, payment_data):
        url = constants.ORDER_PAYMENT_URL.format(order_id)
        return util.request_post(url=url, data=payment_data).json()
