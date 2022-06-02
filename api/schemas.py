from pydantic import BaseModel
from typing import List, Union,Optional

class AddressBase(BaseModel):
	address_line1 : str 
	address_line2 : str
	city : str
	pin : int 

class Address(AddressBase):
	id : int
	class Config():
		orm_mode = True


class StudentBase(BaseModel):
	student_name : str
	student_class : int 
	student_session : str
	

class Student(StudentBase):
	addresses : List[AddressBase]
	class Config():
		orm_mode = True


class ShowStudent(StudentBase):
	id : int
	addresses : List[Address]
	class Config():
		orm_mode = True





