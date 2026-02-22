from dataclasses import dataclass


@dataclass
class Product:
    product_id: str
    name: str
    regular_price: float | None
    promo_price: float | None
    brand: str | None
    city_id: str
