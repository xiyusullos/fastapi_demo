import typing as tp

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from core.configs.db import SQLALCHEMY_DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)
MySQLSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Generator[yield_type, send_type, return_type]
def get_db() -> tp.Generator[Session, None, None]:
    db: tp.Optional[Session] = None
    try:
        db = MySQLSession()
        yield db
    finally:
        if db is not None:
            db.close()
