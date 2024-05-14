from models import AddressBook
from commands import add_record, edit_record, delete_record, find_record, list_records
from utils import parse_command
from storage import AddressBookStorage

def main():
    storage = AddressBookStorage()
    book = storage.load()
    parse_command().print_help()

    while True:
        command = input("Enter command: ").strip()
        
        if command.lower() in ["close", "exit"]:
            storage.save(book)
            print("Exiting program.")
            break

        try:
            args = parse_command().parse_args(command.split())
            if args.command == 'add':
                add_record(book, args.name, args.phone[0])

            elif args.command == 'edit':
                edit_record(book, args.name, args.old_phone, args.new_phone)

            elif args.command == 'delete':
                delete_record(book, args.name)

            elif args.command == 'find':
                find_record(book, args.name)

            elif args.command == 'list':
                list_records(book)

            else:
                print("Unknown command. Please try again.")

        except SystemExit:
            continue

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting program.")
