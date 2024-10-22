import json
import os

def load_contacts():
    if os.path.exists('contacts.json'):
        with open('contacts.json', 'r') as file:
            return json.load(file)
    return {}


def save_contacts(contacts):
    with open('contacts.json', 'w') as file:
        json.dump(contacts, file)


def add_contact(contacts):
    name = input("Enter contact name: ")
    if name in contacts:
        print("Contact already exists!")
        return
    phone = input("Enter contact phone number: ")
    contacts[name] = {"phone": phone}
    print(f"Contact {name} added successfully.")


def edit_contact(contacts):
    name = input("Enter the name of the contact to edit: ")
    if name not in contacts:
        print("Contact not found!")
        return
    phone = input(f"Enter new phone number for {name}: ")
    contacts[name]["phone"] = phone
    print(f"Contact {name} updated successfully.")


def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print("Contact not found!")


def search_contact(contacts):
    query = input("Enter name or phone number to search: ")
    for name, details in contacts.items():
        if query.lower() in name.lower() or query == details["phone"]:
            print(f"Found contact - Name: {name}, Phone: {details['phone']}")
            return
    print("Contact not found!")


def main():
    contacts = load_contacts()

    while True:
        print("\n=== Contact Book ===")
        print("1. Add Contact")
        print("2. Edit Contact")
        print("3. Delete Contact")
        print("4. Search Contact")
        print("5. View All Contacts")
        print("6. Quit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            edit_contact(contacts)
        elif choice == '3':
            delete_contact(contacts)
        elif choice == '4':
            search_contact(contacts)
        elif choice == '5':
            if contacts:
                for name, details in contacts.items():
                    print(f"Name: {name}, Phone: {details['phone']}")
            else:
                print("No contacts found.")
        elif choice == '6':
            save_contacts(contacts)
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()