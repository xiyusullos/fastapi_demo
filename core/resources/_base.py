import typing as tp

from fastapi import APIRouter

from core.actions._base import ListAction, BaseAction, DetailAction, CreateAction, PartialUpdateAction, DeleteAction
from core.repositories._base import BaseRepository
from core.transformers._base import BaseTransformer, OrmTransformer
from core.validators._base import BaseValidator


class BaseResource():
    name: str
    name_doc: str
    path: str
    router: APIRouter = APIRouter()
    Actions: tp.List[tp.Type[BaseAction]] = []

    repository: BaseRepository
    Transformer: tp.Type[BaseTransformer]

    def __init__(self):
        self.router: APIRouter = APIRouter(prefix=self.path, tags=[self.name_doc])

    def register_resource(self):
        for Action in self.Actions:
            Action(self.repository, self.Transformer).register_action(self.router)

        return self


class CRUDResource(BaseResource):
    Transformer: tp.Type[OrmTransformer]

    create_Validator: BaseValidator = None
    partial_update_Validator: BaseValidator = None

    enable_list: bool = True
    enable_create: bool = True
    enable_detail: bool = True
    enable_partial_update: bool = True
    enable_delete: bool = True

    def register_resource(self):
        if self.enable_list:
            (ListAction(self.repository, self.Transformer)
             .register_action(self.router))

        if self.enable_create:
            (CreateAction(self.repository, self.Transformer, Validator=self.create_Validator)
             .register_action(self.router))

        if self.enable_detail:
            (DetailAction(self.repository, self.Transformer)
             .register_action(self.router))

        if self.enable_partial_update:
            (PartialUpdateAction(self.repository, self.Transformer, Validator=self.partial_update_Validator)
             .register_action(self.router))

        if self.enable_delete:
            (DeleteAction(self.repository, self.Transformer)
             .register_action(self.router))

        return super().register_resource()
