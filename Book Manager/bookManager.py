import datetime

class Book:
    def __init__(self, title, author, publication_year):
        self._title = title
        self._author = author
        self._publication_year = publication_year

    def get_title(self):
        return self._title

    def get_author(self):
        return self._author

    def get_publication_year(self):
        return self._publication_year


class BookManager:
    def __init__(self):
        self._book_list = []

    def add_book(self, book):
        self._book_list.append(book)

    def show_books(self):
        if not self._book_list:
            print("No books in the list.")
        else:
            print("List of Books:")
            for book in self._book_list:
                print(f"Title: {book.get_title()}, Author: {book.get_author()}, Publication Year: {book.get_publication_year()}")

    def search_book(self, title):
        found_books = [book for book in self._book_list if book.get_title().lower() == title.lower()]
        if found_books:
            print("Search Results:")
            for book in found_books:
                print(f"Title: {book.get_title()}, Author: {book.get_author()}, Publication Year: {book.get_publication_year()}")
        else:
            print("No matching book found.")


class UserInterface:
    @staticmethod
    def get_input(prompt):
        return input(prompt)

    @staticmethod
    def add_book(manager):
        while True:
            title = UserInterface.get_input("Enter book title: ").strip()
            if not title:
                print("Title cannot be empty. Please enter a title.")
            else:
                break
        
        while True:
            author = UserInterface.get_input("Enter author name: ").strip()
            if not author:
                print("Author name cannot be empty. Please enter an author.")
            elif author.isdigit():
                print("Invalid input. Author name cannot be a number.")
            else:
                break
        
        while True:
            year = UserInterface.get_input("Enter publication year: ")
            if not year.isdigit():
                print("Invalid input. Please enter a valid year.")
            elif int(year) > datetime.datetime.now().year:
                print("Invalid input. Publication year cannot be in the future.")
            else:
                break
                
        manager.add_book(Book(title, author, int(year)))

    @staticmethod
    def view_books(manager):
        manager.show_books()

    @staticmethod
    def search_books(manager):
        title = UserInterface.get_input("Enter book title to search: ")
        manager.search_book(title)


def main():
    book_manager = BookManager()
    while True:
        print("\nMenu:")
        print("1. Add a new book")
        print("2. View all books")
        print("3. Search for a book")
        print("4. Exit")
        choice = UserInterface.get_input("Enter your choice: ")
        if choice == '1':
            UserInterface.add_book(book_manager)
        elif choice == '2':
            UserInterface.view_books(book_manager)
        elif choice == '3':
            UserInterface.search_books(book_manager)
        elif choice == '4':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please choose again.")


if __name__ == "__main__":
    main()
