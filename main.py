import pandas as pd

from magnit_parser.client import MagnitClient
from magnit_parser.parser import MagnitParser


def main() -> None:
    client = MagnitClient()
    parser = MagnitParser(client)

    category_id = 63963  # Молочка
    store_code = '771865'

    products = []

    for city_id in ['355', '1141']:  # Москва, Питер
        for product in parser.parse_category(
            city_id=city_id,
            category_id=category_id,
            store_code=store_code,
        ):
            products.append(product.__dict__)

    df = pd.DataFrame(products)
    df.to_csv('magnit_products.csv', index=False)


if __name__ == '__main__':
    main()
