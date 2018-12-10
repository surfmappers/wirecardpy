from wirecardpy.utils.util import is_sandbox

# Define both API urls
BASE_URL_SANDBOX = 'https://sandbox.moip.com.br/v2/'
BASE_URL_LIVE = 'https://api.moip.com.br/v2/'

# DDefine which one will be used
BASE_URL = BASE_URL_SANDBOX if is_sandbox() else BASE_URL_LIVE

# Order constants
ORDER_URL = BASE_URL + 'orders/'
ORDER_PAYMENT_URL = BASE_URL + ORDER_URL + '{0}/payments'
