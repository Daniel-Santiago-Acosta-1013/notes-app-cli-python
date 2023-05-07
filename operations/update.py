from sqlalchemy.orm import Session
from models.note import Note
from database.db import SessionLocal

def update_note():
    note_id = int(input("ID de la nota a actualizar: "))

    db = SessionLocal()
    note = db.query(Note).filter(Note.id == note_id).first()

    if not note:
        print(f"No se encontró la nota con ID: {note_id}")
        return

    new_title = input(f"Título actual: {note.title}\nNuevo título: ")
    new_content = input(f"Contenido actual: {note.content}\nNuevo contenido: ")

    note.title = new_title if new_title else note.title
    note.content = new_content if new_content else note.content

    db.commit()
    db.close()

    print(f"Nota con ID {note_id} actualizada.")
