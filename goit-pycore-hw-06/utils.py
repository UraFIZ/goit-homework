import argparse


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



def parse_command():
    parser = argparse.ArgumentParser(prog='', description='Manage your address book. Have fun!')
    subparsers = parser.add_subparsers(dest='command')

    add_parser = subparsers.add_parser('add', help='add [name] [phone1] - Add a new record. Example: "add John 1234567890"')
    add_parser.add_argument('name', type=str, help='Name of the contact. It should contain only letters and spaces.')
    add_parser.add_argument('phone', type=str, nargs='+', help='Phone numbers of the contact. It should contain only digits and be 10 digits long.')

    edit_parser = subparsers.add_parser('edit', help='edit [name] [old_phone] [new_phone] - Edit an existing phone number. Example: "edit John 1234567890 0987654321"')
    edit_parser.add_argument('name', type=str, help='Name of the contact')
    edit_parser.add_argument('old_phone', type=str, help='Old phone number')
    edit_parser.add_argument('new_phone', type=str, help='New phone number. Must be 10 digits long.')

    delete_parser = subparsers.add_parser('delete', help='delete [name] - Delete a record by the name. Example: "delete John"')
    delete_parser.add_argument('name', type=str, help='Name of the contact')

    find_parser = subparsers.add_parser('find', help='find [name] - Find a record by the name. Example: "find John"')
    find_parser.add_argument('name', type=str, help='Name of the contact')

    subparsers.add_parser('list', help='List of all records. Example: "list"')
    subparsers.add_parser('close', help='Close the app and save the data. Example: "close"')
    subparsers.add_parser('exit', help='Close the app and save the data. Example: "exit"')
    subparsers.add_parser('help', help='Show the current menu. Example: "-h" or "--help')
    subparsers.add_parser('command help', help='Show the help for a specific command. Example: "add -h"')


    subparsers.add_parser('piatachok', help='Show the beautiful piatachok. Example: "piatachok"')



    return parser
