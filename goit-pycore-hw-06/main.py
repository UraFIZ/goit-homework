from models import AddressBook
from commands import add_record, edit_record, delete_record, find_record
from utils import display_menu, parse_command, list_records

def main():
    book = AddressBook()
    display_menu()

    while True:
        command = input("Enter command: ").strip()
        
        if command.lower() in ["close", "exit"]:
            print("Exiting program.")
            break

        try:
            args = parse_command(command)
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
            display_menu()
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting program.")
