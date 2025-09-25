dictionary = {}

while True:
    print("\nDictionary Management System")
    print("1. Add a Word")
    print("2. Search for Meaning")
    print("3. Display All Words")
    print("4. Update Meaning")
    print("5. Delete Word")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        word = input("Enter the word: ").lower()
        meaning = input("Enter the meaning: ")
        dictionary[word] = meaning
        print("Word added successfully!")

    elif choice == '2':
        word = input("Enter the word to search: ").lower()
        if word in dictionary:
            print("Meaning:", dictionary[word])
        else:
            print("Word not found in the dictionary.")

    elif choice == '3':
        if dictionary:
            print("Words and their meanings:")
            for word, meaning in dictionary.items():
                print(f"{word}: {meaning}")
        else:
            print("Dictionary is empty.")

    elif choice == '4':
        word = input("Enter the word to update meaning: ").lower()
        if word in dictionary:
            new_meaning = input("Enter the new meaning: ")
            dictionary[word] = new_meaning
            print("Meaning updated successfully!")
            print("Updated Meaning:", dictionary[word])
        else:
            print("Word not found in the dictionary.")

    elif choice == '5':
        word = input("Enter the word to delete: ").lower()
        if word in dictionary:
            del dictionary[word]
            print("Word deleted successfully!")
        else:
            print("Word not found in the dictionary.")

    elif choice == '6':
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please enter a valid option.")



