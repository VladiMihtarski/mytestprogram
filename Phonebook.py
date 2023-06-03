contacts = {}
 
while True:
    menu = input("Menu:\n1: Update contact\n2: Add contact\n3: Search contact\n4: Show all contacts\n5: Delete contact\nEnter your choice (1-5): ")
 
    if menu == "1":
        name = input("Enter the name to update: ")
        phone = input("Enter the new phone number: ")
        contacts[name] = phone
        print("Contact updated.")
 
    elif menu == "2":
        name = input("Enter the name: ")
        phone = input("Enter the phone number: ")
        contacts[name] = phone
        print("Contact added.")
 
    elif menu == "3":
        name = input("Enter the first three letters of the name to search: ")
        search_results = [contact for contact in contacts.keys() if contact.lower().startswith(name.lower())]
        if search_results:
            print("Search results:")
            for result in search_results:
                print(result)
        else:
            print("No contacts found.")
 
    elif menu == "4":
        if contacts:
            print("All contacts:")
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
        else:
            print("No contacts available.")
 
    elif menu == "5":
        name = input("Enter the name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")
 
    else:
        print("Invalid input. Please enter a valid menu option.")
