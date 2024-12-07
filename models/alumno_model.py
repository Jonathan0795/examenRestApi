from sqlalchemy import Column, Integer, String, Boolean, Float
from database import Base
from models.mixins import Timestamp


class Alumno(Base, Timestamp):
    __tablename__ = 'tb_alumnos'
    alumno_id = Column(Integer, primary_key=True, autoincrement=True)
    documento = Column(String(8), primary_key=True)
    nombre = Column(String(200), nullable=False)
    apellido = Column(String(200), nullable=False)
    aprobado = Column(Boolean, nullable=False, default=False)
    nota = Column(Float(), nullable=True)

    @property
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}