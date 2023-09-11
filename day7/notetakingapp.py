notes = {}

while True:
    print("Choose an action:")
    print("1 - Add note")
    print("2 - View notes")
    print("3 - Edit note")
    print("4 - Delete note")
    print("5 - Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        note_title = input("Enter a title for the note: ")
        note_content = input("Enter the note content: ")
        notes[note_title] = note_content
        print("Note added.")
    elif choice == '2':
        if not notes:
            print("No notes available.")
        else:
            print("Notes:")
            for title, content in notes.items():
                print(f"Title: {title}")
                print(f"Content: {content}")
    elif choice == '3':
        if not notes:
            print("No notes available.")
        else:
            note_title = input("Enter the title of the note to edit: ")
            if note_title in notes:
                new_content = input("Enter the new content: ")
                notes[note_title] = new_content
                print("Note edited.")
            else:
                print("Note not found.")
    elif choice == '4':
        if not notes:
            print("No notes available.")
        else:
            note_title = input("Enter the title of the note to delete: ")
            if note_title in notes:
                del notes[note_title]
                print("Note deleted.")
            else:
                print("Note not found.")
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please choose a valid option.")
