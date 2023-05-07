from sqlalchemy.orm import Session
from models.note import Note
from database.db import SessionLocal

def delete_note():
    note_id = int(input("ID de la nota a eliminar: "))

    db = SessionLocal()
    note = db.query(Note).filter(Note.id == note_id).first()

    if not note:
        print(f"No se encontró la nota con ID: {note_id}")
        return

    db.delete(note)
    db.commit()
    db.close()

    print(f"Nota con ID {note_id} eliminada.")
