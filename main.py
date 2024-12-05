from contact_operations import (
    add_contact,
    remove_contact,
    search_contact,
    view_contacts,
)
from file_operations import load_contacts, save_contacts

# Load contacts from file
contacts = load_contacts()


def display_menu():
    print("\n--- Contact Book Management ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Remove Contact")
    print("5. Exit")


while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact(contacts)
    elif choice == "2":
        view_contacts(contacts)
    elif choice == "3":
        search_contact(contacts)
    elif choice == "4":
        remove_contact(contacts)
    elif choice == "5":
        save_contacts(contacts)
        print("Contacts saved. Exiting...")
        break
    else:
        print("Invalid choice. Please select a valid option.")
