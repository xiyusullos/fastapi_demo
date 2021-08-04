import typing as tp

from core.validators._base import BaseValidator


class AddressCreatingValidator(BaseValidator):
    address: str
    address2: tp.Optional[str] = None
    district: str
    city_id: int
    postal_code: str
    phone: str


class AddressPartialUpdatingValidator(BaseValidator):
    address: tp.Optional[str] = None
    address2: tp.Optional[str] = None
    district: tp.Optional[str] = None
    city_id: tp.Optional[int] = None
    postal_code: tp.Optional[str] = None
    phone: tp.Optional[str] = None
