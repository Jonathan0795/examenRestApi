from typing import Optional, List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from models.alumno_model import Alumno
from schemas.estudiante_schemas import AlumnoCreated, AlumnoRespose, AlumnoUpdated

router = APIRouter(prefix='/alumno', tags=['alumno'])


@router.post('/create', response_model=AlumnoRespose)
async def crear_alumno(payload: AlumnoCreated, db: Session = Depends(get_db)):
    alumno: Optional[Alumno] = db.query(Alumno).filter_by(documento=payload.documento).first()
    if alumno:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'El alumno ya se encuentra registado con ese número de documento {payload.documento}')
    nuevo_alumno = Alumno(**payload.model_dump())
    db.add(nuevo_alumno)
    db.commit()
    return nuevo_alumno


@router.patch('update', response_model=AlumnoRespose)
async def actualizar_alumno(alumno_id: int, payload: AlumnoUpdated, db: Session = Depends(get_db)):
    alumno_query = db.query(Alumno).filter_by(alumno_id=alumno_id)
    alumno: Optional[Alumno] = alumno_query.first()
    if not alumno:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='El alumno no se encuentra registado.')
    updated_alumno = payload.model_dump(exclude_unset=True)
    alumno_query.update(updated_alumno, synchronize_session=False)
    db.commit()
    return alumno_query.first()


@router.delete('/delete')
async def eliminar_alumno(alumno_id: int, db: Session = Depends(get_db)):
    alumno = db.query(Alumno).filter_by(alumno_id=alumno_id).first()
    if not alumno:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='El alumno no se encuentra registado.')
    db.delete(alumno)
    db.commit()
    return {"message": f"El alumno con ID {alumno_id} ha sido eliminado exitosamente."}


@router.get('/listado', response_model=List[AlumnoRespose])
async def listado_alumnos(db: Session = Depends(get_db)):
    estudiantes = db.query(Alumno).all()
    return estudiantes
