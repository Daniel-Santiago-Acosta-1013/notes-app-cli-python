from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from database.db import Base
from models.tag import note_tag
import datetime


class Note(Base):
    __tablename__ = 'notes'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    content = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    tags = relationship("Tag", secondary=note_tag, backref="notes")


    def __repr__(self):
        return f"<Note(id={self.id}, title='{self.title}', content='{self.content}', created_at='{self.created_at}', updated_at='{self.updated_at}')>"
