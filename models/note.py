from sqlalchemy import Column, Integer, String
from database.db import Base

class Note(Base):
    __tablename__ = 'notes'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    content = Column(String, nullable=False)

    def __repr__(self):
        return f"<Note(id={self.id}, title='{self.title}', content='{self.content}')>"
