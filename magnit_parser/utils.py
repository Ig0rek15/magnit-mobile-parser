def extract_brand(details: list[dict]) -> str | None:
    for block in details:
        if block.get('type') == 'tableType':
            for param in block.get('parameters', []):
                if param.get('name') == 'Бренд':
                    return param.get('value')
    return None


def normalize_price(price: int | None) -> float | None:
    if price is None:
        return None
    return price / 100
