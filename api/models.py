from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship
from typing import List, Union


class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True, index=True)
    address_line1 = Column(String(255))
    address_line2= Column(String(255))
    city= Column(String(50))
    pin= Column(Integer)
    s_id = Column(Integer, ForeignKey('students.id')) 
    owner = relationship("Student", back_populates="addresses")




class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, index=True)
    student_name = Column(String(255))  
    student_class = Column(Integer)
    student_session = Column(String(16))
    address_line1 = Column(String(255))
    address_line2= Column(String(255))
    city= Column(String(50))
    pin= Column(Integer) 
    addresses = relationship('Address', back_populates="owner")