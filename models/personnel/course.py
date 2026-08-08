"""Personnel order model."""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..mixins import TimestampMixin
from .personnel_base import PersonnelBase


# pylint: disable=too-few-public-methods
class Course(PersonnelBase, TimestampMixin):
    """Course model representing a user's course."""

    __tablename__ = "courses"
    __table_args__ = {"schema": "personnel"}  # noqa: RUF012

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("personnel.users.id"), nullable=False)
    course_name = Column(String, nullable=False)

    user = relationship("User", back_populates="personnel.courses")
    exam_results = relationship(
        "CourseExamResults",
        back_populates="personnel.course",
        cascade="all, delete-orphan",
    )
