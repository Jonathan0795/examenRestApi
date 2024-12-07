from typing import Optional

from pydantic import BaseModel


class AlumnoBase(BaseModel):
    documento: str
    nombre: str
    apellido: str


class AlumnoCreated(AlumnoBase):
    pass


class AlumnoUpdated(AlumnoBase):
    aprobado: bool
    nota: float


class AlumnoRespose(AlumnoBase):
    alumno_id: int
    aprobado: Optional[bool]
    nota: Optional[float]

    class Config:
        from_attributes = True
