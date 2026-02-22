import logging

from pathlib import Path
from dataclasses import asdict

import pandas as pd

from magnit_parser.client import MagnitClient
from magnit_parser.config import CITIES, CATEGORY_ID, DEFAULT_LIMIT
from magnit_parser.parser import MagnitParser

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

logger = logging.getLogger(__name__)


def main() -> None:
    logger.info('Parser started')
    client = MagnitClient()
    parser = MagnitParser(client)

    products = []

    for city, config in CITIES.items():
        logger.info(f'Start parsing city: {city}')

        for product in parser.parse_category(
            city=city,
            city_id=config['city_id'],
            store_code=config['store_code'],
            category_id=CATEGORY_ID,
            limit=DEFAULT_LIMIT,
        ):
            products.append(asdict(product))

    df = pd.DataFrame(products)
    output_dir = Path('results')
    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / 'magnit_products.csv'
    df.to_csv(output_path, index=False)
    logger.info(f'Saved results to {output_path}')
    logger.info('Parser finished successfully')


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logger.exception(f'Fatal error: {e}')
