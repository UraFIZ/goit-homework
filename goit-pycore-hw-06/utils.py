import argparse

from models import AddressBook


def format_table(headers, rows):
    # Determine column widths
    col_widths = [max(len(str(item)) for item in col) for col in zip(*[headers] + rows)]
    
    # Create format string
    format_str = " | ".join([f"{{:<{width}}}" for width in col_widths])
    
    # Create table
    table = []
    table.append(format_str.format(*headers))
    table.append("-+-".join(['-' * width for width in col_widths]))
    for row in rows:
        table.append(format_str.format(*row))
    
    return "\n".join(table)


def display_menu():
    menu = """
    Please choose an action:
    1. add [name] [phone1] ... - Add a new record
    2. edit [name] [old_phone] [new_phone] - Edit an existing phone number
    3. delete [name] - Delete a record
    4. find [name] - Find a record
    5. list - List all records
    6. close or exit - Exit the program
    """
    print(menu)

def parse_command(command):
    parser = argparse.ArgumentParser(prog='', description='Manage your address book.')
    subparsers = parser.add_subparsers(dest='command')

    add_parser = subparsers.add_parser('add', help='Add a new record')
    add_parser.add_argument('name', type=str, help='Name of the contact')
    add_parser.add_argument('phone', type=str, nargs='+', help='Phone numbers of the contact')

    edit_parser = subparsers.add_parser('edit', help='Edit an existing phone number')
    edit_parser.add_argument('name', type=str, help='Name of the contact')
    edit_parser.add_argument('old_phone', type=str, help='Old phone number')
    edit_parser.add_argument('new_phone', type=str, help='New phone number')

    delete_parser = subparsers.add_parser('delete', help='Delete a record')
    delete_parser.add_argument('name', type=str, help='Name of the contact')

    find_parser = subparsers.add_parser('find', help='Find a record')
    find_parser.add_argument('name', type=str, help='Name of the contact')

    list_parser = subparsers.add_parser('list', help='List all records')

    return parser.parse_args(command.split())
