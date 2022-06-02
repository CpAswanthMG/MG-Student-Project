from sqlalchemy.orm import Session
from . import models, schemas


def student_List_Utils(request:dict,address:list) -> dict:
	return {
		"id":request.id,
		"student_name" : request.student_name,
		"student_class" : request.student_class,
		"student_session" : request.student_session,
		"addresses" : address
	}

def list_address_utils(request:int,db:Session):
	address_list = []
	address = db.query(models.Address).filter(models.Address.s_id == request).all()
	for add in address:
		address_list.append({
			"id":add.id,
			"address_line1" : add.address_line1, 
			"address_line2" : add.address_line2,
			"city" : add.city,
			"pin" : add.pin
		})
	return address_list







	
