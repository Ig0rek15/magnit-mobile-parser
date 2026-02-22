from dataclasses import dataclass


@dataclass(slots=True)
class Product:
    product_id: str
    name: str
    regular_price: float | None
    promo_price: float | None
    brand: str | None
    city: str
