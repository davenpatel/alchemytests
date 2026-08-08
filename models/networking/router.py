"""Router model."""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..mixins import TimestampMixin
from .networking_base import NetworkingBase


# pylint: disable=too-few-public-methods
class Router(NetworkingBase, TimestampMixin):
    """Represents a router in the network."""

    __tablename__ = "routers"
    __table_args__ = {"schema": "networking"}  # noqa: RUF012

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    model = Column(String(50), nullable=False)

    # Relationships
    network_id = Column(Integer, ForeignKey("networking.networks.id"), nullable=False)
    network = relationship("Network", back_populates="networking.routers")
