__author__ = 'dhs'
x = 0
phonebook = {}
while x == 0:
    command = input("Input your command! Search/Insert/Update/Delete/Display/Quit: ")
    if command == "Search":
        entry = input("Input an entry to search for: ")
        if entry in d:
            print("Entry is found!")
        else:
            print("Entry not found!")
    elif command == "Insert":
        name = input("What is the name? ")
        if name not in phonebook:
            number = input("What is the phone number? ")
            phonebook[name] = number
        else:
            print("The name is already in the phonebook!")
    elif command == "Update":
        name = input("What is the name? ")
        if name in phonebook:
            number = input("What is the phone number? ")
            phonebook[name] = number
        else:
            print("The name is not in the phonebook!")
    elif command == "Delete":
        name = input("What is the name? ")
        if name in phonebook:
            number = input("What is the phone number? ")
            del phonebook[name]
        else:
            print("The name is not in the phonebook!")
    elif command == "Display":
        print(phonebook)
    elif command == "Quit":
        print("Thank you for using Lim Ah Seng Phonebook!")
        x = 1
    else:
        print("Please input a valid command! With Capital letters! Search/Insert/Update/Delete/Display/Quit: ")