from sqlalchemy.orm import Session
from models.note import Note
from database.db import SessionLocal

def create_note():
    title = input("Título de la nota: ")
    content = input("Contenido de la nota: ")

    note = Note(title=title, content=content)

    db = SessionLocal()
    db.add(note)
    db.commit()
    db.refresh(note)
    db.close()

    print(f"Nota creada con ID: {note.id}")
