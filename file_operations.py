FILE_NAME = "contacts.txt"


def load_contacts():
    contacts = []
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                name, email, phone, address = line.strip().split("|")
                contacts.append(
                    {"Name": name, "Email": email, "Phone": phone, "Address": address}
                )
    except FileNotFoundError:
        print("No existing contact file found. Starting fresh.")
    return contacts


def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        for contact in contacts:
            file.write(
                f"{contact['Name']}|{contact['Email']}|{contact['Phone']}|{contact['Address']}\n"
            )
