from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .personnel_base import PersonnelBase
from ..mixins import TimestampMixin


class LineItem(PersonnelBase, TimestampMixin):
    __tablename__ = "line_items"
    __table_args__ = {"schema": "personnel"}

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("personnel.orders.id"), nullable=False)
    product_name = Column(String(100), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)

    order = relationship("Order", back_populates="personnel.line_items")
