import enum
from sqlalchemy import Column, String, Integer, ForeignKey, Enum
from sqlalchemy.orm import relationship
from models.base import BaseModel


class PositionEnum(enum.Enum):
    """Enum for player positions"""

    GK = "GK"
    DEF = "DEF"
    MID = "MID"
    FWD = "FWD"


class Player(BaseModel):
    """Player model representing football players in the FPL system"""

    __tablename__ = "players"

    name = Column(String(100), nullable=False, index=True)
    position = Column(Enum(PositionEnum), nullable=False, index=True)
    team_id = Column(Integer, ForeignKey("teams.id"), nullable=False, index=True)
    nationality = Column(String(50), nullable=True)
    age = Column(Integer, nullable=True)
    photo_url = Column(String(255), nullable=True)

    # Relationship
    team = relationship("Team", back_populates="players")

    def __repr__(self):
        return (
            f"<Player(id={self.id}, name='{self.name}', "
            f"position='{self.position.value}', team_id={self.team_id})>"
        )
