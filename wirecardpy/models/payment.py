from wirecardpy import util


class Payment(object):
    @staticmethod
    def create(order_id, payment_data):
        url = 'https://sandbox.moip.com.br/v2/orders/{0}/payments'.format(order_id)

        return util.request_post(url=url, data=payment_data).json()
