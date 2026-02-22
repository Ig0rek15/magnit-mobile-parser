import requests


class MagnitClient:
    BASE_URL = 'https://middle-api.magnit.ru'

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
        category_id: int,
        store_code: str,
        limit: int,
        offset: int,
    ) -> dict:
        url = f'{self.BASE_URL}/v2/goods/search'

        payload = {
            'cityId': city_id,
            'sort': {'order': 'desc', 'type': 'popularity'},
            'categories': [category_id],
            'storeCode': store_code,
            'storeType': 'express',
            'pagination': {'limit': limit, 'offset': offset},
            'catalogType': '2',
        }

        response = self.session.post(url, json=payload, timeout=15)
        response.raise_for_status()
        return response.json()

    def get_product_details(
        self,
        product_id: str,
        store_code: str,
        city_id: str,
    ) -> dict:
        url = (
            f'{self.BASE_URL}/v2/goods/{product_id}/stores/{store_code}'
            f'?catalogtype=2&cityid={city_id}'
            f'&storetype=express&targetCart=express'
        )

        response = self.session.get(url, timeout=15)
        response.raise_for_status()
        return response.json()
