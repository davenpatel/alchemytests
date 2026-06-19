"""Personnel order model."""

from sqlalchemy import Column, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship
from .personnel_base import PersonnelBase
from ..mixins import TimestampMixin


class Order(PersonnelBase, TimestampMixin):
    """Order model representing a user's order."""

    __tablename__ = "orders"
    __table_args__ = {"schema": "personnel"}

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("personnel.users.id"), nullable=False)
    total = Column(Float, nullable=False, default=0.0)

    user = relationship("User", back_populates="personnel.orders")
    line_items = relationship(
        "LineItem", back_populates="personnel.order", cascade="all, delete-orphan"
    )
