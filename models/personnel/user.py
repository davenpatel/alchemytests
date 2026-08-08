"""User model for personnel management."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from ..mixins import TimestampMixin
from .personnel_base import PersonnelBase


# pylint: disable=too-few-public-methods
class User(PersonnelBase, TimestampMixin):
    """User model representing a personnel user."""

    __tablename__ = "users"
    __table_args__ = {"schema": "personnel"}  # noqa: RUF012

    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)

    orders = relationship("Order", back_populates="personnel.user")
    courses = relationship("Course", back_populates="personnel.user")
    exam_results = relationship("CourseExamResults", back_populates="personnel.user")
