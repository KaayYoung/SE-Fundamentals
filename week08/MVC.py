import sqlite3

"""
Precondition of running this program: Run Library.py for once
The MVC architecture which allows the user to query the library by book's name and also author's name
"""

class Controller(object):

    def __init__(self):
        pass

    def search_book(self, title):
        model = LibraryModel()
        view = LibraryView()
        book = model.search_book(title)
        return view.print_book(book, title)

    def search_author(self, author):
        model = LibraryModel()
        view = LibraryView()
        book_list = model.search_author(author)
        return view.print_author(book_list, author)


class LibraryModel(object):

    def search_author(self, author):
        query = "SELECT title, year, genre  from BOOK where author = ?"
        payload = (author,)
        book_list = self._dbselect(query, payload)
        return book_list

    def search_book(self, title):
        query = "SELECT title, author, year, genre  from BOOK where title = ?"
        payload = (title,)
        book = self._dbselect(query, payload)
        return book

    def _dbselect(self, query, payload):

        # Logic to connect to the database.  Students will be               
        # introduced to this in the lectures this week
        connection = sqlite3.connect('library.db')
        cursorObj = connection.cursor()

        # execute the query
        rows = cursorObj.execute(query, payload)
        connection.commit()
        results = []
        for row in rows:
            results.append(row)
        cursorObj.close()
        return results


class LibraryView(object):

    def print_author(self, book_list, author):
        print("%s's books:"%author)
        for book in book_list:
            print(book)
        print()

    def print_book(self, book, title):
        print("Book with title: %s"%title)
        print(book)
        print()


controller = Controller()
controller.search_author("Aarthi")
controller.search_author("Tom")
controller.search_book("Agile Design Principles")
controller.search_book("The Lord of the Rings")
controller.search_book("Pride and Prejudice")
controller.search_book("The Great Gatsby")
controller.search_book("Introduction to Cooking")
controller.search_book("Software Engineering Fundamentals")
