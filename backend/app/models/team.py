from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base import BaseModel


class Team(BaseModel):
    """Team model representing football teams in the FPL system"""

    __tablename__ = "teams"

    name = Column(String(100), nullable=False, unique=True, index=True)
    short_name = Column(String(10), nullable=False, unique=True, index=True)
    stadium = Column(String(100), nullable=True)
    manager = Column(String(100), nullable=True)
    logo_url = Column(String(255), nullable=True)

    # Relationship
    players = relationship("Player", back_populates="team")

    def __repr__(self):
        return (
            f"<Team(id={self.id}, name='{self.name}', short_name='{self.short_name}')>"
        )
