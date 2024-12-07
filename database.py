from typing import Generator
import logging
from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker, Session, declarative_base

logger = logging.getLogger(__name__)
Base = declarative_base()

SQLALCHEMY_DATABASE_URL = URL.create(
    "mysql+mysqlconnector",
    username="MYSQL_USERNAME",
    password="MYSQL_PASSWORD",
    host="HOST_DATABASE",
    database="ALUMNOS_CIBERTEC",
)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    echo=False,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Database:

    def __init__(self) -> None:
        self._engine = engine

    def create_database(self) -> None:
        Base.metadata.create_all(self._engine)


db_instance = Database()
db_instance.create_database()


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    except Exception:
        logger.exception("Session rollback because of exception")
        db.rollback()
        raise
    finally:
        db.close()
