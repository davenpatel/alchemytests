from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .networking_base import NetworkingBase
from ..mixins import TimestampMixin

class Router(NetworkingBase, TimestampMixin):
    __tablename__ = "routers"
    __table_args__ = {"schema": "networking"} 

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    model = Column(String(50), nullable=False)

    # Relationships
    network_id = Column(Integer, ForeignKey("networking.networks.id"), nullable=False)
    network = relationship("Network", back_populates="networking.routers")