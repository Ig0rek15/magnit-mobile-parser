import requests

from magnit_parser.config import (
    BASE_URL,
    SEARCH_SORT,
    STORE_TYPE,
    CATALOG_TYPE,
    TARGET_CART,
    REQUEST_TIMEOUT,
)


class MagnitClient:
    def __init__(self) -> None:
        self.session = requests.Session()
        self.session.headers.update(
            {
                'Content-Type': 'application/json',
                'User-Agent': 'MagnitOmni/8.92.0',
                'X-Device-Platform': 'iOS',
            }
        )

    def search_goods(
        self,
        city_id: str,
        store_code: str,
        category_id: int,
        limit: int,
        offset: int,
    ) -> dict:
        url = f'{BASE_URL}/v2/goods/search'

        payload = {
            'cityId': city_id,
            'sort': SEARCH_SORT,
            'categories': [category_id],
            'storeCode': store_code,
            'storeType': STORE_TYPE,
            'pagination': {'limit': limit, 'offset': offset},
            'catalogType': CATALOG_TYPE,
        }

        response = self.session.post(url, json=payload, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        return response.json()

    def get_product_details(
        self,
        product_id: str,
        store_code: str,
        city_id: str,
    ) -> dict:
        url = (
            f'{BASE_URL}/v2/goods/{product_id}/stores/{store_code}'
            f'?catalogtype={CATALOG_TYPE}'
            f'&cityid={city_id}'
            f'&storetype={STORE_TYPE}'
            f'&targetCart={TARGET_CART}'
        )

        response = self.session.get(url, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        return response.json()
