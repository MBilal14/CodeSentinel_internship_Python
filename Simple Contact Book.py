# Task 2
# Simple Contact Book (File Handling)
# Build a simple console app that: Lets the user add a name and phone
# number Saves contacts to a contacts.txt file Allows viewing saved contacts
# 🛠 Concepts: File I/O (open, read, write), while loops,dictionaries
# 🎯 Goal: Learn how to store and retrieve persistent datausing files.


while True:
    # Menu
    print("\n--- Contact Book ---")
    print("1.Add a new contact")
    print("2.View all contacts")
    print("3.Exit")
    choice = input("Enter the number according to your choice: ")
    if choice == "1":
        # Add a new contact
        name = input("Please Enter Your Name: ")
        number = input("Please Enter Your Number: ")
        # Save as dictionary
        contact = {name: number}

        print("Contact saved successfully!")

        with open("contacts.txt", "a") as file:
            file.write(f"{name}:{number} \n")
    elif choice == "2":
        # View all contacts
        print("\n--- Saved Contacts ---")
        try:
            with open("contacts.txt", "r") as file:
                contacts = file.read()
                if contacts:
                    print(contacts)
                else:
                    print("No contacts found.")
        except FileNotFoundError:
            print("No contacts file found yet.")
    elif choice == "3":
        break
    else:
        print("Invalid choice, please try again.")
