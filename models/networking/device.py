"""Networking device model."""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .networking_base import NetworkingBase
from ..mixins import TimestampMixin


class Device(NetworkingBase, TimestampMixin):
    """Represents a networking device."""

    __tablename__ = "devices"
    __table_args__ = {"schema": "networking"}

    id = Column(Integer, primary_key=True)
    network_id = Column(Integer, ForeignKey("networking.networks.id"), nullable=False)
    name = Column(String(100), nullable=False)
    ip_address = Column(String(15), unique=True, nullable=False)

    network = relationship("Network", back_populates="networking.devices")

    def __repr__(self):
        return f"<Device(id={self.id!r}, name={self.name!r}, ip_address={self.ip_address!r})>"
