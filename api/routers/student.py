from fastapi import APIRouter
from typing import List
from .. import database,schemas,models
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,status
from .. repository import student,address

router = APIRouter(
    prefix="/api/student",
    tags=['Students']
)

get_db = database.get_db


@router.get('/', response_model=List[schemas.ShowStudent])
def all(db: Session = Depends(get_db),limit:int = 5,skip :int = 0):
    return student.get_all_students(db,limit,skip)
    

@router.post('/', status_code=status.HTTP_201_CREATED)
def create_students(request: schemas.Student,db: Session = Depends(get_db)):
    return student.create(request,db)

@router.get('/{id}', status_code=200, response_model=schemas.ShowStudent)
def get_students(id:int,db: Session = Depends(get_db)):
    return student.get_student_by_id(id, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int, db: Session = Depends(get_db)):
    return student.destroy(id,db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request: schemas.Student, db: Session = Depends(get_db)):
    return student.update(id,request, db)









