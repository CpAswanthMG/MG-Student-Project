from pydantic import BaseModel
from typing import List, Union,Optional

class AddressBase(BaseModel):
	address_line1 : Optional[str] 
	address_line2 : Optional[str] 
	city : Optional[str] 
	pin : Optional[int] 
	s_id : Optional[int]  

class Address(AddressBase):
	address_line1 : str 
	address_line2 : str
	city : str
	pin : int 
	s_id : int

	class Config():
		orm_mode = True

class StudentBase(BaseModel):
	student_name : Optional[str] 
	student_class : Optional[int] 
	student_session : Optional[str]
	address_line1 : Optional[str] 
	address_line2 : Optional[str]
	city : Optional[str]
	pin : Optional[int]
	

class Student(StudentBase):
	student_name : str 
	student_class : int 
	student_session : str
	address_line1 : str 
	address_line2 : str
	city : str
	pin : int
	class Config():
		orm_mode = True


class ShowStudent(BaseModel):
	student_name : str 
	student_class : int 
	student_session : str
	addresses : List[Address] =[]

	class Config():
		orm_mode = True

class ShowOwner(BaseModel):
	student_name : str 
	student_class : int 
	student_session : str

	class Config():
		orm_mode = True


class ShowAddress(BaseModel):
	address_line1 : str 
	address_line2 : str
	city : str
	pin : int 
	owner : ShowOwner

	class Config():
		orm_mode = True