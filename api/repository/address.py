from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException,status
from sqlmodel import select


# def get_all(db: Session):
#     addresses = db.query(models.Address).all()
#     return addresses

# def get_by_id(id:int, db: Session):
#     return db.query(models.Address).filter(models.Address.id == id)



def create(id: int, requests:list,db:Session) -> bool:
    print(db)
    for request in requests:
        new_data = {
            'address_line1' : request.address_line1,
            'address_line2' : request.address_line2,
            'city' : request.city,
            'pin' : request.pin,
            's_id' : id
        }
        new_address = models.Address(**new_data)
        db.add(new_address)
        db.commit()
        db.refresh(new_address)
    return "created"

def update(id:int, requests:list, db:Session) -> bool:
    len_request = len(requests)
    addresses = db.query(models.Address).filter(models.Address.s_id == id)
    len_address = len(addresses)
    flag = len_address is len_request
    if not flag:
        create(id,requests[len_request-1],db)
    for request in requests:
        for address in addresses:
            update_data = {
                    'address_line1' : request.address_line1,
                    'address_line2' : request.address_line2,
                    'city' : request.city,
                    'pin' : request.pin,
                    's_id' : id
            }
            for key, value in update_data.items():
                setattr(address, key, value)
            db.add(address)
            db.commit()
            db.refresh(address)
    return True
      

def destroy(id:int, db: Session):
    address=db.query(models.Address).filter(models.Address.id == id)
    if not address.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Address with id {id} not found")
    address.delete(synchronize_session=False)
    db.commit()
    return True



# def show(id:int,db:Session):
#     address_view = get_by_id(id, db).first()
#     if not address_view:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"Address with the id {id} is not available")
#     return address_view




