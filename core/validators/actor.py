import typing as tp

from core.validators._base import BaseValidator


class ActorCreatingValidator(BaseValidator):
    actor: str
    actor2: tp.Optional[str] = None
    district: str
    city_id: int
    postal_code: str
    phone: str


class ActorPartialUpdatingValidator(BaseValidator):
    actor: tp.Optional[str] = None
    actor2: tp.Optional[str] = None
    district: tp.Optional[str] = None
    city_id: tp.Optional[int] = None
    postal_code: tp.Optional[str] = None
    phone: tp.Optional[str] = None
