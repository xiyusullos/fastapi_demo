from typing import Optional

from ._base import OrmTransformer

class MasterTaskInfo(OrmTransformer):
    id: int
    task_name: str
    task_alias: str