from wirecardpy.utils import util, constants


class Payment(object):
    @staticmethod
    def create(order_id, payment_data):
        url = util.get_base_url() + constants.ORDER_PAYMENT_URL.format(order_id)
        return util.request_post(url=url, data=payment_data)
