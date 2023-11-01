class Notebook:
    def __init__(self):
        self.notes = {}

    def add_note(self, title, content):
        self.notes[title] = content
        print(f"Note added: {title}")

    def update_note(self, title, new_content):
        if title in self.notes:
            self.notes[title] = new_content
            print(f"Note updated: {title}")
        else:
            print("Note not found.")

    def delete_note(self, title):
        if title in self.notes:
            del self.notes[title]
            print(f"Note deleted: {title}")
        else:
            print("Note not found.")

    def list_notes(self):
        for title, content in self.notes.items():
            print(f"{title}: {content}")

if __name__ == "__main__":
    notebook = Notebook()

    while True:
        print("\nAvailable actions:")
        print("1. Add Note")
        print("2. Update Note")
        print("3. Delete Note")
        print("4. List Notes")
        print("5. Exit")

        choice = input("Please select an action (1/2/3/4/5): ")

        if choice == "1":
            title = input("Enter the note title: ")
            content = input("Enter the note content: ")
            notebook.add_note(title, content)

        elif choice == "2":
            title = input("Enter the title of the note to update: ")
            new_content = input("Enter the new content: ")
            notebook.update_note(title, new_content)

        elif choice == "3":
            title = input("Enter the title of the note to delete: ")
            notebook.delete_note(title)

        elif choice == "4":
            print("Your notes:")
            notebook.list_notes()

        elif choice == "5":
            print("Notebook application is closing.")
            break

        else:
            print("Invalid choice. Please try again.")
