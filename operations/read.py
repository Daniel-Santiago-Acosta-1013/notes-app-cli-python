from sqlalchemy.orm import Session
from models.note import Note
from database.db import SessionLocal
import markdown
import json

def show_notes():
    db = SessionLocal()
    notes = db.query(Note).all()
    db.close()

    if not notes:
        print("No hay notas disponibles.")
    else:
        for note in notes:
            content_html = markdown.markdown(note.content)
            print(f"\nID: {note.id}\nTítulo: {note.title}\nContenido:\n{content_html}")


def search_and_filter_notes():
    keyword = input("Palabra clave para buscar (presione ENTER para omitir): ")
    tag_name = input("Nombre de la etiqueta para filtrar (presione ENTER para omitir): ")

    db = SessionLocal()

    query = db.query(Note)

    if keyword:
        query = query.filter(Note.title.contains(keyword) | Note.content.contains(keyword))

    if tag_name:
        query = query.join(Note.tags).filter(Tag.name == tag_name)

    notes = query.all()
    db.close()

    if not notes:
        print("No se encontraron notas.")
    else:
        for note in notes:
            print(f"\nID: {note.id}\nTítulo: {note.title}\nContenido: {note.content}")

def export_notes():
    db = SessionLocal()
    notes = db.query(Note).all()
    db.close()

    notes_data = [
        {"id": note.id, "title": note.title, "content": note.content}
        for note in notes
    ]

    with open("notes_export.json", "w") as f:
        json.dump(notes_data, f, ensure_ascii=False, indent=2)

    print("Notas exportadas a 'notes_export.json'.")


def import_notes():
    file_path = input("Ruta del archivo JSON a importar: ")

    try:
        with open(file_path, "r") as f:
            notes_data = json.load(f)
    except FileNotFoundError:
        print(f"No se pudo encontrar el archivo '{file_path}'.")
        return

    db = SessionLocal()

    for note_data in notes_data:
        note = Note(title=note_data["title"], content=note_data["content"])
        db.add(note)

    db.commit()
    db.close()

    print(f"Notas importadas desde '{file_path}'.")

