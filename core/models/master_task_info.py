from sqlalchemy import CHAR, Column, DECIMAL, DateTime, Enum, Index, LargeBinary, String, TIMESTAMP, Text, text
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, MEDIUMINT, SET, TINYINT, VARCHAR, YEAR

from core.models._base import BaseModel as Base


class MasterTaskInfo(Base):
    __tablename__ = 'master_task_info'

    id = Column(BIGINT(20), primary_key=True)
    task_name = Column(String(255))
    task_alias = Column(String(255))
