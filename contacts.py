class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}\nPhone Number: {self.phone_number}\nEmail: {self.email}\nAddress: {self.address}\n"


class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone_number, email, address):
        contact = Contact(name, phone_number, email, address)
        self.contacts.append(contact)
        print("Contact added successfully")

    def view_contact_list(self):
        if not self.contacts:
            print("No contacts found")
        else:
            for i, contact in enumerate(self.contacts, start=1):
                print(f"\nContact {i}:\n{contact}")

    def search_contact(self, keyword):
        found_contacts = []
        for contact in self.contacts:
            if (
                keyword.lower() in contact.name.lower()
                or keyword in contact.phone_number
            ):
                found_contacts.append(contact)
        if not found_contacts:
            print("No matching contacts found.")
        else:
            print("\nMatching Contacts:")
            for i, contact in enumerate(found_contacts, start=1):
                print(f"\nContact {i}:\n{contact}")

    def update_contact(self, index, name, phone_number, email, address):
        if 1 <= index <= len(self.contacts):
            contact = self.contacts[index - 1]
            contact.name = name
            contact.phone_number = phone_number
            contact.email = email
            contact.address = address
            print("Contact updated successfully")
        else:
            print("Invalid contact index")

    def delete_contact(self, index):
        if 1 <= index <= len(self.contacts):
            del self.contacts[index - 1]
            print("Contact deleted successfully.")
        else:
            print("Invalid contact index.")


def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Manager Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone_number, email, address)
        elif choice == "2":
            contact_book.view_contact_list()
        elif choice == "3":
            keyword = input("Enter name or phone number to search: ")
            contact_book.search_contact(keyword)
        elif choice == "4":
            index = int(input("Enter the contact index to update: "))
            name = input("Enter updated name: ")
            phone_number = input("Enter updated phone number: ")
            email = input("Enter updated email: ")
            address = input("Enter updated address: ")
            contact_book.update_contact(index, name, phone_number, email, address)
        elif choice == "5":
            index = int(input("Enter the contact index to delete: "))
            contact_book.delete_contact(index)
        elif choice == "6":
            print("Exiting the Contact Book application")
            break
        else:
            print("Invalid choice. Please try again")

if __name__ == "__main__":
    main()