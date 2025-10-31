import cli
import sys
import pickle
from addressbook import AddressBook


DEF_ADDRESSBOOK_FILENAME = "def_addressbook.pkl"


def save_addressbook(book, filename=DEF_ADDRESSBOOK_FILENAME):
    """ Saves the address book to a file.
    Parameters:
        book (AddressBook): The address book instance.
        filename (str): The name of the file to save the address book to."""
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_addressbook(filename=DEF_ADDRESSBOOK_FILENAME):
    """ Loads the address book from a file.
    Parameters:
        filename (str): The name of the file to load the address book from.
    """
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()


def main():

    filename = sys.argv[1] if len(sys.argv) > 1 else DEF_ADDRESSBOOK_FILENAME
    book = load_addressbook(filename)

    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = cli.parse_input(user_input)

        if command in ["close", "exit"]:
            save_addressbook(book, filename)
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(cli.add_contact(args, book))

        elif command == "change":
            print(cli.change_contact(args, book))

        elif command == "phone":
            print(cli.phone_contact(args, book))

        elif command == "all":
            print(cli.all_contacts(book))

        elif command == "add-birthday":
            print(cli.add_birthday(args, book))

        elif command == "show-birthday":
            print(cli.show_birthday(args, book))

        elif command == "birthdays":
            print(cli.birthdays(book))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
