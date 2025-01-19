import json

class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, address):
        if phone in self.contacts:
            print(f"Contact with phone number {phone} already exists.")
            return
        self.contacts[phone] = {
            "name": name,
            "email": email,
            "address": address
        }
        print(f"Contact {name} added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts to display.")
            return
        print("\nSaved Contacts:")
        print("{:<20} {:<15}".format("Name", "Phone"))
        print("-" * 35)
        for phone, details in self.contacts.items():
            print("{:<20} {:<15}".format(details['name'], phone))

    def search_contact(self, query):
        results = []
        for phone, details in self.contacts.items():
            if query.lower() in details['name'].lower() or query in phone:
                results.append((details['name'], phone, details['email'], details['address']))
        if results:
            print("\nSearch Results:")
            print("{:<20} {:<15} {:<25} {:<30}".format("Name", "Phone", "Email", "Address"))
            print("-" * 90)
            for result in results:
                print("{:<20} {:<15} {:<25} {:<30}".format(*result))
        else:
            print("No contacts found matching the query.")

    def update_contact(self, phone):
        if phone not in self.contacts:
            print(f"No contact found with phone number {phone}.")
            return
        print("\nUpdating Contact:")
        name = input("Enter new name (leave blank to keep current): ") or self.contacts[phone]["name"]
        email = input("Enter new email (leave blank to keep current): ") or self.contacts[phone]["email"]
        address = input("Enter new address (leave blank to keep current): ") or self.contacts[phone]["address"]
        self.contacts[phone] = {"name": name, "email": email, "address": address}
        print("Contact updated successfully.")

    def delete_contact(self, phone):
        if phone not in self.contacts:
            print(f"No contact found with phone number {phone}.")
            return
        del self.contacts[phone]
        print("Contact deleted successfully.")

    def menu(self):
        while True:
            print("\nContact Management System")
            print("1. Add New Contact")
            print("2. View Contacts")
            print("3. Search Contacts")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Exit")
            choice = input("Enter your choice (1-6): ")

            if choice == "1":
                name = input("Enter name: ")
                phone = input("Enter phone number: ")
                email = input("Enter email: ")
                address = input("Enter address: ")
                self.add_contact(name, phone, email, address)
            elif choice == "2":
                self.view_contacts()
            elif choice == "3":
                query = input("Enter name or phone number to search: ")
                self.search_contact(query)
            elif choice == "4":
                phone = input("Enter phone number of contact to update: ")
                self.update_contact(phone)
            elif choice == "5":
                phone = input("Enter phone number of contact to delete: ")
                self.delete_contact(phone)
            elif choice == "6":
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    manager = ContactManager()
    manager.menu()
