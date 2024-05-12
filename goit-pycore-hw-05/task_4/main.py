
import sys
import os
import json
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from utils.decorators.log_errors import log_errors
from collections import defaultdict

def save_contacts(contacts, filename='contacts.json'):
    with open(filename, 'w') as file:
        json.dump(contacts, file)
        
def load_contacts(filename='contacts.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def parse_input(user_input: str):
    parts = user_input.strip().split()
    command = parts[0].lower()
    args = parts[1:]
    return command, args

def add_contact(args, contacts):
    if len(args) != 2:
        return "Error: Please provide a name and a phone number."
    name, phone = args
    contacts[name.lower()] = phone
    return "Contact added."

def change_contact(args, contacts):
    if len(args) != 2:
        return "Error: Please provide a name and a new phone number."
    name, new_phone = args
    if name.lower() in contacts:
        contacts[name.lower()] = new_phone
        return "Contact updated."
    else:
        return "Error: Contact not found."

def show_phone(args, contacts):
    if len(args) != 1:
        return "Error: Please provide a name."
    name = args[0].lower()
    if name in contacts:
        return f"{name.capitalize()}'s phone number is {contacts[name]}"
    else:
        return "Error: Contact not found."

def show_all(contacts):
    if contacts:
        return "\n".join(f"{name.capitalize()}: {phone}" for name, phone in contacts.items())
    else:
        return "No contacts saved."

@log_errors
def main():
    try:
        contacts = {}
        print("Welcome to the assistant bot!")
        while True:
            user_input = input("Enter a command: ")
            command, args = parse_input(user_input)

            if command in ["close", "exit"]:
                print("Good bye!")
                break
            elif command == "hello":
                print("How can I help you?")
            elif command == "add":
                print(add_contact(args, contacts))
            elif command == "change":
                print(change_contact(args, contacts))
            elif command == "phone":
                print(show_phone(args, contacts))
            elif command == "all":
                print(show_all(contacts))
            else:
                print("Invalid command.")
                
    except KeyboardInterrupt:
        print("\nДопобачення!")

if __name__ == "__main__":
    main()
