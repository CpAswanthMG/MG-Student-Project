from sqlalchemy.orm import Session
from . import models, schemas


class StudentUtility:
	def create(id: int, db:Session):
		student = db.get(models.Student, id)
		new_data = {
			'address_line1' : student.address_line1,
			'address_line2' : student.address_line2,
			'city' : student.city,
			'pin' : student.pin,
			's_id' : id
		}
		new_address = models.Address(**new_data)
		db.add(new_address)
		db.commit()
		db.refresh(new_address)
		return 'created'

	def change(id:int, db:Session):
		address = db.query(models.Address).filter(models.Address.s_id == id).first()
		student = db.get(models.Student, id)
		if not address:
			return False
		update_data = {
			'address_line1' : student.address_line1,
			'address_line2' : student.address_line2,
			'city' : student.city,
			'pin' : student.pin,
			's_id' : id
		}
		for key, value in update_data.items():
			setattr(address, key, value)
		db.add(address)
		db.commit()
		db.refresh(address)
		return 'updated'


	
