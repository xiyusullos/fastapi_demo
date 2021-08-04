from core.models._all import Actor as Model
from core.repositories._base import CRUDRepository
from core.resources._base import CRUDResource
from core.transformers.actor import Actor as Transformer
from core.validators.actor import (
    ActorCreatingValidator as Validator1,
    ActorPartialUpdatingValidator as Validator2
)


class ActorResource(CRUDResource):
    name = 'actor'
    name_doc = '演员'
    path = '/actors'

    repository = CRUDRepository(Model)
    Transformer = Transformer

    create_Validator = Validator1
    partial_update_Validator = Validator2


resource = ActorResource().register_resource()
