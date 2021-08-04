from core.models._all import Address as Model
from core.repositories._base import CRUDRepository
from core.resources._base import CRUDResource
from core.transformers.address import Address as Transformer
from core.validators.address import (
    AddressCreatingValidator as Validator1,
    AddressPartialUpdatingValidator as Validator2
)


class AddressResource(CRUDResource):
    name = 'address'
    name_doc = '地址'
    path = '/addresses'

    repository = CRUDRepository(Model)
    Transformer = Transformer

    create_Validator = Validator1
    partial_update_Validator = Validator2


resource = AddressResource().register_resource()
