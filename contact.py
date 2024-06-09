def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")    
    address = input("Enter address: ")
    
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    print("Contact added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found!")
    else:
        for contact in contacts:
            print(f"Name: {contact['name']}, \nPhone: {contact['phone']}, \nEmail: {contact['email']}, \nAddress: {contact['address']}")

def search_contacts(contacts):
    search_term = input("Enter name or phone number to search: ")
    found = False
    for contact in contacts:
        if search_term in contact["name"] or search_term in contact["phone"]:
            print(f"Name: {contact['name']}, \nPhone: {contact['phone']}, \nEmail: {contact['email']}, \nAddress: {contact['address']}")
            found = True
    if not found:
        print("Contact not found!")

def update_contact(contacts):
    search_term = input("Enter name or phone number of the contact to update: ")
    for contact in contacts:
        if search_term in contact["name"] or search_term in contact["phone"]:
            contact["name"] = input(f"Enter new name (current: {contact['name']}): ") or contact["name"]
            contact["phone"] = input(f"Enter new phone number (current: {contact['phone']}): ") or contact["phone"]
            contact["email"] = input(f"Enter new email (current: {contact['email']}): ") or contact["email"]
            contact["address"] = input(f"Enter new address (current: {contact['address']}): ") or contact["address"]
            print("Contact updated successfully!")
            return
    print("Contact not found!")

def delete_contact(contacts):
    search_term = input("Enter name or phone number of the contact to delete: ")
    for contact in contacts:
        if search_term in contact["name"] or search_term in contact["phone"]:
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return
    print("Contact not found!")


contacts = []

while True:
    print("\nContact Manager")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_contact(contacts)
    elif choice == "2":
        view_contacts(contacts)
    elif choice == "3":
        search_contacts(contacts)
    elif choice == "4":
        update_contact(contacts)
    elif choice == "5":
        delete_contact(contacts)
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice! Please try again.")


# Contact Manager
# 1. Add Contact
# 2. View Contacts
# 3. Search Contact
# 4. Update Contact
# 5. Delete Contact
# 6. Exit
# Enter your choice: 1
# Enter name: Afra
# Enter phone number: 9876543215 
# Enter email: afra@gmail.com
# Enter address: Theni
# Contact added successfully!

# Contact Manager
# 1. Add Contact
# 2. View Contacts
# 3. Search Contact
# 4. Update Contact
# 5. Delete Contact
# 6. Exit
# Enter your choice: 2
# Name: Afra,
# Phone: 9876543215,
# Email: afra@gmail.com,
# Address: Theni

# Contact Manager
# 1. Add Contact
# 2. View Contacts
# 3. Search Contact
# 4. Update Contact
# 5. Delete Contact
# 6. Exit
# Enter your choice: 3
# Enter name or phone number to search: Afra
# Name: Afra,
# Phone: 9876543215,
# Email: afra@gmail.com,
# Address: Theni

# Contact Manager
# 1. Add Contact
# 2. View Contacts
# 3. Search Contact
# 4. Update Contact
# 5. Delete Contact
# 6. Exit
# Enter your choice: 4
# Enter name or phone number of the contact to update: Afrafathima
# Contact not found!

# Contact Manager
# 1. Add Contact
# 2. View Contacts
# 3. Search Contact
# 4. Update Contact
# 5. Delete Contact
# 6. Exit
# Enter your choice: 4
# Enter name or phone number of the contact to update: Afra
# Enter new name (current: Afra): Afrafathima
# Enter new phone number (current: 9876543215): 123457895
# Enter new email (current: afra@gmail.com): afrafathima@gmail.com
# Enter new address (current: Theni): Theni
# Contact updated successfully!

# Contact Manager
# 1. Add Contact
# 2. View Contacts
# 3. Search Contact
# 4. Update Contact
# 5. Delete Contact
# 6. Exit
# Enter your choice: 5
# Enter name or phone number of the contact to delete: Afrafathima
# Contact deleted successfully!

# Contact Manager
# 1. Add Contact
# 2. View Contacts
# 3. Search Contact
# 4. Update Contact
# 5. Delete Contact
# 6. Exit
# Enter your choice: 6
# Exiting...
