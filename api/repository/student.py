from sqlalchemy.orm import Session
from .. import models, schemas,database
from fastapi import HTTPException,status
from . import address
from .. utilities import StudentUtility
# from ..hashing import Hash


databases = database.database

def get_all(db: Session):
    students = db.query(models.Student).all()
    return students

def create(request: schemas.Student,db:Session):
    new_student = models.Student(**request.dict())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return StudentUtility.create(new_student.id,db)

def destroy(id:int,db: Session):
    student = db.query(models.Student).filter(models.Student.id == id)

    if not student.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Student with id {id} not found")

    student.delete(synchronize_session=False)
    db.commit()
    return 'done'


def update(id:int,request:schemas.StudentBase, db:Session):
    student = db.get(models.Student, id)
    if not student:
        raise HTTPException(status_code=404, detail=f"Student with {id} not found")
    student_data = request.dict(exclude_unset=True)
    for key, value in student_data.items():
        setattr(student, key, value)
    db.add(student)
    db.commit()
    db.refresh(student)
    student_status = StudentUtility.change(id,db)
    if student_status == False:
        StudentUtility.create(id,db)
        return 'updated'
    return 'updated'


  
def show(id:int,db:Session):
    student = db.query(models.Student).filter(models.Student.id == id).first()
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} is not available")
    return student

