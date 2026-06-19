"""Network model."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .networking_base import NetworkingBase
from ..mixins import TimestampMixin


# pylint: disable=too-few-public-methods
class Network(NetworkingBase, TimestampMixin):
    """Represents a network."""

    __tablename__ = "networks"
    __table_args__ = {"schema": "networking"}

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)

    devices = relationship("Device", back_populates="networking.network")
