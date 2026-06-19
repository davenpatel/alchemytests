"""Base class for personnel models."""

from sqlalchemy.orm import DeclarativeBase


class PersonnelBase(DeclarativeBase):
    """Base class for personnel models."""

    __abstract__ = True
