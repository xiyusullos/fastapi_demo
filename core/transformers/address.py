from typing import Optional

from core.transformers._base import OrmTransformer


class Address(OrmTransformer):
    address: str
    address2: str = Optional[None]
    district: str
    city_id: int
    postal_code: str
    phone: str
    # location: str
    # last_update: int
