import sys
from operations import create, read, update, delete

def print_usage():
    print("Uso:")
    print("  python main.py [create|read|update|delete]")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)
    
    operation = sys.argv[1].lower()

    if operation == "create":
        create.create_note()
    elif operation == "read":
        read.show_notes()
    elif operation == "update":
        update.update_note()
    elif operation == "delete":
        delete.delete_note()
    else:
        print_usage()
        sys.exit(1)
