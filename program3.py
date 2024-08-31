import json

# Function to load contacts from a file
def load_contacts(filename="contacts.json"):
    try:
        with open(filename, "r") as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = []
    return contacts

# Function to save contacts to a file
def save_contacts(contacts, filename="contacts.json"):
    with open(filename, "w") as file:
        json.dump(contacts, file, indent=4)

# Function to add a new contact
def add_contact(contacts):
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email address: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    print("Contact added successfully!")

# Function to view all contacts
def view_contacts(contacts):
    if contacts:
        for idx, contact in enumerate(contacts, 1):
            print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    else:
        print("No contacts found.")

# Function to edit an existing contact
def edit_contact(contacts):
    view_contacts(contacts)
    contact_index = int(input("Enter the number of the contact you want to edit: ")) - 1
    
    if 0 <= contact_index < len(contacts):
        print("Leave blank if you don't want to change a field.")
        name = input(f"Enter the new name (current: {contacts[contact_index]['name']}): ")
        phone = input(f"Enter the new phone number (current: {contacts[contact_index]['phone']}): ")
        email = input(f"Enter the new email address (current: {contacts[contact_index]['email']}): ")
        
        if name:
            contacts[contact_index]['name'] = name
        if phone:
            contacts[contact_index]['phone'] = phone
        if email:
            contacts[contact_index]['email'] = email
        
        print("Contact updated successfully!")
    else:
        print("Invalid contact number.")

# Function to delete a contact
def delete_contact(contacts):
    view_contacts(contacts)
    contact_index = int(input("Enter the number of the contact you want to delete: ")) - 1
    
    if 0 <= contact_index < len(contacts):
        contacts.pop(contact_index)
        print("Contact deleted successfully!")
    else:
        print("Invalid contact number.")

# Main function to run the contact management system
def main():
    contacts = load_contacts()
    
    while True:
        print("\nContact Management System")
        print("1. Add a new contact")
        print("2. View contacts")
        print("3. Edit a contact")
        print("4. Delete a contact")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_contact(contacts)
            save_contacts(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            edit_contact(contacts)
            save_contacts(contacts)
        elif choice == "4":
            delete_contact(contacts)
            save_contacts(contacts)
        elif choice == "5":
            print("Exiting the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
