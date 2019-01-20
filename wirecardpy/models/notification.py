from wirecardpy.utils import util
from wirecardpy.utils import constants


class Notification(object):
    @staticmethod
    def create(access_token, data):
        url = util.get_base_url() + constants.NOTIFICATION_URL
        return util.request_post(url, data, access_token=access_token)

    def remove(access_token, notification_id):
        url = util.get_base_url() + constants.REMOVE_NOTIFICATION_URL.format(notification_id)
        return util.request_delete(url, access_token=access_token)
