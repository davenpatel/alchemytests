from sqlalchemy import Column, DateTime, Integer, String, func
from sqlalchemy.orm import relationship
from .personnel_base import PersonnelBase
from ..mixins import TimestampMixin

class User(PersonnelBase, TimestampMixin):
    __tablename__ = "users"
    __table_args__ = {"schema": "personnel"} 

    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)

    orders = relationship("Order", back_populates="personnel.user")



