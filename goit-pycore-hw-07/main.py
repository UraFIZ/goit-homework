from commands import add_record, edit_record, delete_record, find_record, list_records, add_birthday, show_birthday, get_upcoming_birthdays
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
            elif args.command == 'change':
                edit_record(book, args.name, args.old_phone, args.new_phone)
            elif args.command == 'delete':
                delete_record(book, args.name)
            elif args.command == 'phone':
                find_record(book, args.name)
            elif args.command == 'all':
                list_records(book)
            elif args.command == 'hello':
                print("💝🐽🐽🐽 '' 🐷 '' 🐽🐽🐽💝")
            elif args.command == 'add-birthday':
                add_birthday(book, args.name, args.birthday)
            elif args.command == 'show-birthday':
                show_birthday(book, args.name)
            elif args.command == 'birthdays':
                get_upcoming_birthdays(book)
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
