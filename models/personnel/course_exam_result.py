"""Personnel order model."""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..mixins import TimestampMixin
from .personnel_base import PersonnelBase


# pylint: disable=too-few-public-methods
class CourseExamResult(PersonnelBase, TimestampMixin):
    """Course exam results model."""

    __tablename__ = "course_exam_results"
    __table_args__ = {"schema": "personnel"}  # noqa: RUF012

    id = Column(Integer, primary_key=True)
    course_id = Column(Integer, ForeignKey("personnel.courses.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("personnel.users.id"), nullable=False)
    date_taken = Column(String, nullable=False)
    score = Column(Integer, nullable=False)

    course = relationship("Course", back_populates="personnel.course_exam_results")
    user = relationship("User", back_populates="personnel.course_exam_results")
