from typing import List, Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.services import get_db
from ..transformers.master_alias_info import MasterTaskInfo as Transformer
from ..models.master_task_info import MasterTaskInfo as Model



resource_name = "master_task_info"
resource_name_cn = "主任务"
resource_path = "master_task_infos"
router = APIRouter(prefix=f'/{resource_path}')


async def handle(*,
           # db: Session = Depends(get_db),
           page: int = 1,
           page_size: int = 10,):
    async for db in get_db():
        skip = (page - 1) * page_size
        data = db.query(Model).offset(skip).limit(page_size).all()
        return data
    else:
        pass

class Operation():
    method: str = 'POST'
    path: str  = '/'
    validator: Any = None
    transformer: Any = None
    pre_handle: Any = None
    handle: handle
    post_handle: Any = None

    @classmethod
    async def full_handle(cls):
        if cls.post_handle is not None:
            cls.post_handle()

        cls.handle()

        if cls.post_handle is not None:
            cls.post_handle()

