from operations import create, read, update, delete

def print_menu():
    print("Menú de opciones:")
    print("1. Crear nota")
    print("2. Mostrar notas")
    print("3. Actualizar nota")
    print("4. Eliminar nota")
    print("5. Buscar y filtrar notas")
    print("6. Exportar notas")
    print("7. Importar notas")
    print("8. Salir")

def main():
    while True:
        print_menu()
        option = input("Ingrese la opción deseada: ")

        if option == "1":
            create.create_note()
        elif option == "2":
            read.show_notes()
        elif option == "3":
            update.update_note()
        elif option == "4":
            delete.delete_note()
        elif option == "5":
            read.search_and_filter_notes()
        elif option == "6":
            read.export_notes()
        elif option == "7":
            read.import_notes()
        elif option == "8":
            print("Adiós!")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
