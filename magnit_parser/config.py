BASE_URL = 'https://middle-api.magnit.ru'

DEFAULT_LIMIT = 20
DEFAULT_OFFSET = 0
REQUEST_TIMEOUT = 15
MIN_AVAILABLE_QUANTITY = 0

CATEGORY_ID = 63963  # Молочка

CITIES = {
    'moscow': {
        'city_id': '355',
        'store_code': '771865',
    },
    'spb': {
        'city_id': '355',
        'store_code': '791671',
    },
}

SEARCH_SORT = {'order': 'desc', 'type': 'popularity'}

STORE_TYPE = 'express'
CATALOG_TYPE = '2'
TARGET_CART = 'core_mm'
