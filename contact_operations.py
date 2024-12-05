def add_contact(contacts):
    print("\n--- Add New Contact ---")
    name = input("Enter Name: ").strip()
    email = input("Enter Email: ").strip()
    phone = input("Enter Phone Number: ").strip()
    address = input("Enter Address: ").strip()

    # Validation
    if not name.isalpha():
        print("Error: Name must only contain letters.")
        return
    if not phone.isdigit():
        print("Error: Phone number must be numeric.")
        return
    if phone in [contact["Phone"] for contact in contacts]:
        print("Error: Phone number already exists.")
        return

    contacts.append({"Name": name, "Email": email, "Phone": phone, "Address": address})
    print("Contact added successfully!")


def view_contacts(contacts):
    print("\n--- Contact List ---")
    if not contacts:
        print("No contacts found.")
        return
    for i, contact in enumerate(contacts, 1):
        print(
            f"{i}. Name: {contact['Name']}, Email: {contact['Email']}, Phone: {contact['Phone']}, Address: {contact['Address']}"
        )


def search_contact(contacts):
    print("\n--- Search Contact ---")
    query = input("Enter Name, Email, or Phone Number to search: ").strip()
    results = [contact for contact in contacts if query in contact.values()]
    if not results:
        print("No matching contacts found.")
        return
    for contact in results:
        print(
            f"Name: {contact['Name']}, Email: {contact['Email']}, Phone: {contact['Phone']}, Address: {contact['Address']}"
        )


def remove_contact(contacts):
    print("\n--- Remove Contact ---")
    phone = input("Enter the Phone Number of the contact to remove: ").strip()
    for contact in contacts:
        if contact["Phone"] == phone:
            contacts.remove(contact)
            print("Contact removed successfully.")
            return
    print("No contact found with that phone number.")
