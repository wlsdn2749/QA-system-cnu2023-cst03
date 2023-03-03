from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship

from database import Base
import datetime

class Board(Base):
    __tablename__ = "board"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    content = Column(String(300))
    create_at = Column(DateTime, default=datetime.datetime.utcnow)
    view_count = Column(Integer, default=0)
    rec_count = Column(Integer, default=0)
