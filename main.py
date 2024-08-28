import os

# Defines the filename to store diary entries
DIARY_FILE = "diary_entries.txt"


def display_menu():
    print("\nPersonal Diary App")
    print("1. Add a new entry")
    print("2. View all entries")
    print("3. Delete an entry")
    print("4. Exit")


def add_entry():
    with open(DIARY_FILE, "a") as file:
        entry = input("Write your entry: ")
        file.write(entry + "\n")
        print("⋆｡°✩Entry added successfully!✩°｡⋆")


def view_entries():
    if not os.path.exists(DIARY_FILE):
        print("No entries found.")
        return

    with open(DIARY_FILE, "r") as file:
        entries = file.readlines()
        if not entries:
            print("No entries found.")
        else:
            print("\nYour Diary Entries:")
            for idx, entry in enumerate(entries, start=1):
                print(f"{idx}. {entry.strip()}")


def delete_entry():
    if not os.path.exists(DIARY_FILE):
        print("No entries found.")
        return

    with open(DIARY_FILE, "r") as file:
        entries = file.readlines()

    if not entries:
        print("No entries found.")
        return

    print("\nYour Diary Entries:")
    for idx, entry in enumerate(entries, start=1):
        print(f"{idx}. {entry.strip()}")

    try:
        entry_num = int(input("Enter the entry number to delete: "))
        if 1 <= entry_num <= len(entries):
            del entries[entry_num - 1]
            with open(DIARY_FILE, "w") as file:
                file.writelines(entries)
            print("Entry deleted successfully!")
        else:
            print("Invalid entry number.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def main():
    while True:
        display_menu()
        choice = input("\nChoose an option (1-4): ")

        if choice == "1":
            add_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            delete_entry()
        elif choice == "4":
            print("Exiting the diary app. ByeBye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
