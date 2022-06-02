from sqlalchemy.orm import Session
from .. import models, schemas,database
from fastapi import HTTPException,status
from . import address
from .. utils import list_address_utils,student_List_Utils
# from ..hashing import Hash


databases = database.database

def get_all_students(db: Session,limit:int = 100,skip :int = 0):
    students = db.query(models.Student).offset(skip).limit(limit).all()
    student_list = []
    for student in students:
        address_list=list_address_utils(student.id,db)
        student_list.append(student_List_Utils(student,address_list))
    return student_list

def create(request: schemas.ShowStudent,db:Session):
    new_student = models.Student(
        student_name = request.student_name,
        student_class = request.student_class,
        student_session = request.student_session
    )
    db.add(new_student)
    db.commit()     
    db.refresh(new_student)
    if new_student:
        if address.create(new_student.id, request.addresses,db):
            return True
    return False

def get_student_by_id(id:int,db:Session):
    student = db.query(models.Student).filter(models.Student.id == id).first()
    address_list=list_address_utils(student.id,db)
    student_detail=student_List_Utils(student,address_list)
    if not student_detail:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Student with the id {id} is not available")
    return student_detail

def destroy(id:int,db: Session):
    student = db.query(models.Student).filter(models.Student.id == id)
    addresses = db.query(models.Address).filter(models.Address.s_id == id)
    for add in addresses:
        address.destroy(add.id,db)
    student.delete(synchronize_session=False)
    db.commit()
    return True


def update(id:int,request:schemas.StudentBase, db:Session):
    student = db.query(models.Student).filter(models.Student.id == id)
    if not student:
        raise HTTPException(status_code=404, detail=f"Student with {id} not found")
    update_data = {
        "student_name" : request.student_name,
		"student_class" : request.student_class,
		"student_session" : request.student_session
    }
    student.update(update_data)
    db.commit()
    if student:
        if address.update(id, request.addresses,db):
            return True
    return False 


  


