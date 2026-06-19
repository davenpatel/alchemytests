"""Base class for personnel models."""

from sqlalchemy.orm import DeclarativeBase


# pylint: disable=too-few-public-methods
class PersonnelBase(DeclarativeBase):
    """Base class for personnel models."""

    __abstract__ = True
