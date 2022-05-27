from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException,status
from sqlmodel import select


def get_all(db: Session):
    addresses = db.query(models.Address).all()
    return addresses

def get_by_id(id:int, db: Session):
    return db.query(models.Address).filter(models.Address.id == id)



def create(request: schemas.Address,db: Session):
    new_address = models.Address(**request.dict())
    db.add(new_address)
    db.commit()
    db.refresh(new_address)
    return new_address

def destroy(id:int, db: Session):
    address = get_by_id(id,db)
    if not address.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Address with id {id} not found")

    address.delete(synchronize_session=False)
    db.commit()
    return 'done'


def update(id:int, request:schemas.AddressBase, db:Session):
    address = get_by_id(id, db)
    if not address.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Address with id {id} not found")

    address.update(request.dict())
    db.commit()
    return 'updated'

def show(id:int,db:Session):
    address_view = get_by_id(id, db).first()
    if not address_view:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Address with the id {id} is not available")
    return address_view




