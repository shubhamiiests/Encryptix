import csv

class ContactBook:
    def __init__(self, csv_file):
        self.contacts = {}  # Dictionary to store contacts
        self.csv_file = csv_file  # CSV file to save contacts

    def add_contact(self, name, phone, email, address):
        """Add a new contact."""
        if name not in self.contacts:
            self.contacts[name] = {'phone': phone, 'email': email, 'address': address}
            self.save_to_csv()
            print(f"Contact '{name}' added successfully!")
        else:
            print(f"Contact '{name}' already exists!")

    def view_contacts(self):
        """View all contacts."""
        if self.contacts:
            print("\nContact List:")
            for name, info in self.contacts.items():
                print(f"Name: {name}")
                print(f"Phone: {info['phone']}")
                print(f"Email: {info['email']}")
                print(f"Address: {info['address']}")
                print("--------------------")
        else:
            print("Contact book is empty.")

    def search_contact(self, keyword):
        """Search contacts by name or phone number."""
        found = False
        for name, info in self.contacts.items():
            if keyword.lower() in name.lower() or keyword in info['phone']:
                print(f"Name: {name}")
                print(f"Phone: {info['phone']}")
                print(f"Email: {info['email']}")
                print(f"Address: {info['address']}")
                print("--------------------")
                found = True
        if not found:
            print(f"No contacts found with '{keyword}'.")

    def update_contact(self, name, phone=None, email=None, address=None):
        """Update contact details."""
        if name in self.contacts:
            if phone:
                self.contacts[name]['phone'] = phone
            if email:
                self.contacts[name]['email'] = email
            if address:
                self.contacts[name]['address'] = address
            self.save_to_csv()
            print(f"Contact '{name}' updated successfully!")
        else:
            print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        """Delete a contact."""
        if name in self.contacts:
            del self.contacts[name]
            self.save_to_csv()
            print(f"Contact '{name}' deleted successfully!")
        else:
            print(f"Contact '{name}' not found.")
    
    def save_to_csv(self):
        """Save contacts to CSV file."""
        with open(self.csv_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Phone', 'Email', 'Address'])
            for name, info in self.contacts.items():
                writer.writerow([name, info['phone'], info['email'], info['address']])
    
    def load_from_csv(self):
        """Load contacts from CSV file."""
        try:
            with open(self.csv_file, 'r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header row
                for row in reader:
                    name, phone, email, address = row
                    self.contacts[name] = {'phone': phone, 'email': email, 'address': address}
        except FileNotFoundError:
            print("CSV file not found. Starting with an empty contact book.")

def main():
    csv_file = 'contacts.csv'  # CSV file to store contacts
    contact_book = ContactBook(csv_file)
    contact_book.load_from_csv()  # Load contacts from CSV file if it exists
    
    while True:
        print("\nWelcome to Contact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone, email, address)
        
        elif choice == '2':
            contact_book.view_contacts()
        
        elif choice == '3':
            keyword = input("Enter name or phone number to search: ")
            contact_book.search_contact(keyword)
        
        elif choice == '4':
            name = input("Enter name of contact to update: ")
            phone = input("Enter new phone number (leave blank to keep existing): ")
            email = input("Enter new email address (leave blank to keep existing): ")
            address = input("Enter new address (leave blank to keep existing): ")
            contact_book.update_contact(name, phone, email, address)
        
        elif choice == '5':
            name = input("Enter name of contact to delete: ")
            contact_book.delete_contact(name)
        
        elif choice == '6':
            print("Saving contacts and exiting Contact Book. Goodbye!")
            contact_book.save_to_csv()  # Save contacts before exiting
            break
        
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()

# class ContactBook:
#     def __init__(self):
#         self.contacts = {}  # Dictionary to store contacts

#     def add_contact(self, name, phone, email, address):
#         """Add a new contact."""
#         if name not in self.contacts:
#             self.contacts[name] = {'phone': phone, 'email': email, 'address': address}
#             print(f"Contact '{name}' added successfully!")
#         else:
#             print(f"Contact '{name}' already exists!")

#     def view_contacts(self):
#         """View all contacts."""
#         if self.contacts:
#             print("\nContact List:")
#             for name, info in self.contacts.items():
#                 print(f"Name: {name}")
#                 print(f"Phone: {info['phone']}")
#                 print(f"Email: {info['email']}")
#                 print(f"Address: {info['address']}")
#                 print("--------------------")
#         else:
#             print("Contact book is empty.")

#     def search_contact(self, keyword):
#         """Search contacts by name or phone number."""
#         found = False
#         for name, info in self.contacts.items():
#             if keyword.lower() in name.lower() or keyword in info['phone']:
#                 print(f"Name: {name}")
#                 print(f"Phone: {info['phone']}")
#                 print(f"Email: {info['email']}")
#                 print(f"Address: {info['address']}")
#                 print("--------------------")
#                 found = True
#         if not found:
#             print(f"No contacts found with '{keyword}'.")

#     def update_contact(self, name, phone=None, email=None, address=None):
#         """Update contact details."""
#         if name in self.contacts:
#             if phone:
#                 self.contacts[name]['phone'] = phone
#             if email:
#                 self.contacts[name]['email'] = email
#             if address:
#                 self.contacts[name]['address'] = address
#             print(f"Contact '{name}' updated successfully!")
#         else:
#             print(f"Contact '{name}' not found.")

#     def delete_contact(self, name):
#         """Delete a contact."""
#         if name in self.contacts:
#             del self.contacts[name]
#             print(f"Contact '{name}' deleted successfully!")
#         else:
#             print(f"Contact '{name}' not found.")

# def main():
#     contact_book = ContactBook()
    
#     while True:
#         print("\nWelcome to Contact Book")
#         print("1. Add Contact")
#         print("2. View Contacts")
#         print("3. Search Contact")
#         print("4. Update Contact")
#         print("5. Delete Contact")
#         print("6. Exit")
        
#         choice = input("Enter your choice (1-6): ")
        
#         if choice == '1':
#             name = input("Enter name: ")
#             phone = input("Enter phone number: ")
#             email = input("Enter email address: ")
#             address = input("Enter address: ")
#             contact_book.add_contact(name, phone, email, address)
        
#         elif choice == '2':
#             contact_book.view_contacts()
        
#         elif choice == '3':
#             keyword = input("Enter name or phone number to search: ")
#             contact_book.search_contact(keyword)
        
#         elif choice == '4':
#             name = input("Enter name of contact to update: ")
#             phone = input("Enter new phone number (leave blank to keep existing): ")
#             email = input("Enter new email address (leave blank to keep existing): ")
#             address = input("Enter new address (leave blank to keep existing): ")
#             contact_book.update_contact(name, phone, email, address)
        
#         elif choice == '5':
#             name = input("Enter name of contact to delete: ")
#             contact_book.delete_contact(name)
        
#         elif choice == '6':
#             print("Exiting Contact Book. Goodbye!")
#             break
        
#         else:
#             print("Invalid choice. Please enter a number from 1 to 6.")

# if __name__ == "__main__":
#     main()
