from sqlalchemy.orm import Session
from models.note import Note
from database.db import SessionLocal

def show_notes():
    db = SessionLocal()
    notes = db.query(Note).all()
    db.close()

    if not notes:
        print("No hay notas disponibles.")
    else:
        for note in notes:
            print(f"\nID: {note.id}\nTítulo: {note.title}\nContenido: {note.content}")
