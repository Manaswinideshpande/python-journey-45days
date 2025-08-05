def show_menu():
    print("\nDictionary Menu:")
    print("1. Add a Word")
    print("2. Search for Meaning")
    print("3. Display All Words")
    print("4. Update Meaning")
    print("5. Delete Word")
    print("6. Exit")

dictionary = {}

while True:
    show_menu()
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        word = input("Enter the word: ").strip()
        if word in dictionary:
            print("Word already exists.")
        else:
            meaning = input("Enter the meaning: ").strip()
            dictionary[word] = meaning
            print(f"Word '{word}' added successfully.")

    elif choice == '2':
        word = input("Enter the word to search: ").strip()
        meaning = dictionary.get(word)
        if meaning:
            print(f"The meaning of '{word}' is: {meaning}")
        else:
            print("Word not found in dictionary.")

    elif choice == '3':
        if not dictionary:
            print("Dictionary is empty.")
        else:
            print("\nWords in Dictionary:")
            for word, meaning in dictionary.items():
                print(f"{word}: {meaning}")

    elif choice == '4':
        word = input("Enter the word to update: ").strip()
        if word in dictionary:
            new_meaning = input("Enter the new meaning: ").strip()
            dictionary[word] = new_meaning
            print(f"Updated meaning of '{word}': {new_meaning}")
        else:
            print("Word not found in dictionary.")

    elif choice == '5':
        word = input("Enter the word to delete: ").strip()
        if word in dictionary:
            confirm = input(f"Are you sure you want to delete '{word}'? (y/n): ").lower()
            if confirm == 'y':
                del dictionary[word]
                print(f"Word '{word}' deleted.")
            else:
                print("Deletion canceled.")
        else:
            print("Word not found in dictionary.")

    elif choice == '6':
        print("Exiting dictionary program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")

