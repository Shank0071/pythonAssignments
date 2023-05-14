contacts = {}

def add_contact():
    name = input("Enter the name of the contact: ")
    phone = input("Enter the phone number of the contact: ")
    email = input("Enter the email address of the contact: ")
    contacts[name] = {'phone': phone, 'email': email}
    print("Contact added successfully.")

def search_contact():
    name = input("Enter the name of the contact: ")
    if name in contacts:
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")
    else:
        print("Contact not found.")

def view_contacts():
    if contacts:
        for name in contacts:
            print(f"{name} - Phone: {contacts[name]['phone']}, Email: {contacts[name]['email']}")
    else:
        print("No contacts found.")

def delete_contact():
    name = input("Enter the name of the contact: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

while True:
    print("\n---- Contact Book Menu ----")
    print("1. Add contact")
    print("2. Search contact")
    print("3. View all contacts")
    print("4. Delete contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        search_contact()
    elif choice == '3':
        view_contacts()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")
