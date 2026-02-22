from typing import Generator

from magnit_parser.client import MagnitClient
from magnit_parser.models import Product
from magnit_parser.utils import extract_brand, normalize_price


class MagnitParser:
    def __init__(self, client: MagnitClient) -> None:
        self.client = client

    def parse_category(
        self,
        city_id: str,
        category_id: int,
        store_code: str,
        limit: int = 20,
    ) -> Generator[Product, None, None]:
        offset = 0

        while True:
            data = self.client.search_goods(
                city_id=city_id,
                category_id=category_id,
                store_code=store_code,
                limit=limit,
                offset=offset,
            )

            items = data.get('items', [])
            if not items:
                break

            for item in items:
                if item.get('quantity', 0) <= 0:
                    continue

                product_id = item.get('id')
                details = self.client.get_product_details(
                    product_id=product_id,
                    store_code=store_code,
                    city_id=city_id,
                )

                brand = extract_brand(details.get('details', []))

                yield Product(
                    product_id=product_id,
                    name=item.get('name'),
                    regular_price=normalize_price(
                        details.get('promotion', {}).get('oldPrice')
                    ),
                    promo_price=normalize_price(details.get('price')),
                    brand=brand,
                    city_id=city_id,
                )

            offset += limit
