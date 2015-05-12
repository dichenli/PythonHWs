# Classes and methods for a simple library program
# Authors: Dave Matuszek and <FILL IN YOR NAMES HERE>
#--------------------------------------------------------------

class Calendar(object):
    """Keeps track of the current date (as an integer)."""

    def __init__(self, date):
        """Creates the initial calendar."""
        self.date = date

    def get_date(self):
        """Returns (as a positive integer) the current date."""
        return self.date

    def advance(self):
        """Advances this calendar to the next date."""
        self.date = self.date + 1

#--------------------------------------------------------------

class Book(object):
    """Represents one copy of a book. There may be many copies
       of a book with the same title and author.
       Each book has:
         * An id (a unique integer)
         * A title
         * An author (one string, even if many authors)
         * A due date (or None if the book is not checked out.)."""

    def __init__(self, title, author, book_id):
        """Creates a book, not checked out to anyone."""
        self.title = title
        self.author = author
        self.due_date = None
        self.book_id = book_id

    def get_title(self):
        """Returns the title of this book."""
        return self.title

    def get_author(self):
        """Returns the author(s) of this book, as a single string."""
        return self.author

    def get_due_date(self):
        """If this book is checked out, returns the date on
           which it is due, else returns None."""
        return due_date

    # Added by Alifia
    def get_book_id(self):
        return self.book_id
        
    def check_out(self, due_date):
        """Sets the due date for this book."""
        self.due_date = due_date

    def check_in(self):
        """Clears the due date for this book (sets it to None)."""
        self.due_date = None

    def __str__(self):
        """Returns a string representation of this book,
        of the form: title, by author"""
        return (self.title + ", by " + self.author)

    def __eq__(self, other):
        """Tests if this book equals the given parameter. Not
        required by assignment, but fairly important."""
        return self.title == other.title and self.author == other.author

#--------------------------------------------------------------

class Patron(object):
    """Represents a patron of the library. A patron has:
         * A name
         * A set of books checked out"""

    def __init__(self, name):
        """Constructs a new patron, with no books checked out yet."""
        self.name = name
        self.books = []

    def get_name(self):
        """Returns this patron's name."""
        return self.name

    def get_books(self):
        """Returns the set of books checked out to this patron."""
        return self.books

    def take(self, book):
        """Adds a book to the set of books checked out to this patron."""
        self.books.append(book)

    def give_back(self, book):
        """Removes a book from the set of books checked out to this patron."""
        self.books.remove(book)

    def __str__(self):
        """Returns the name of this patron."""
        return self.name

#--------------------------------------------------------------
    
class OverdueNotice(object):
    """Represents a message that will be sent to a patron."""

    def __init__(self, set_of_books):
        """Takes note of all the books checked out to some patron."""
        self.set_of_books = set_of_books

    def __str__(self):
        """From a set of books, returns a multi-line string giving
           the dates on which the books were or will be due.
           This should only be called when at least one of the books
           is overdue, but ALL the patron's books are listed, with
           their due dates, and the overdue ones specially marked."""
        global calendar
        current_date = calendar.get_date()
        message = ''
        book = Book(object)
        for book in set_of_books:
            due_date = book.get_due_date()
            if due_date > current_date:
                message = message + "*" + book.get_title + " by " + book.get_author + " with Book ID " + book.get_book_id + " is overdue with due date " + book.due_date + "/n"
            else:
                message = message + book.get_title + " by " + book.get_author + " with Book ID " + book.get_book_id + " is due on " + book.due_date + "/n"
#--------------------------------------------------------------

class Library(object):
    """Provides operations available to the librarian."""
    
    def __init__(self):
        """Constructs a library, which involves reading in a
           list of books that are in this library's collection."""
        
        # Create a global calendar, to be used by many classes
        global calendar
        calendar = Calendar()
        
        # Initialize some instance variables for _this_ library
        self.is_open = False            # Is library open?
        self.collection = []            # List of all Books
        self.patrons = {}               # Set of all Patrons
        self.patron_being_served = None # Current patron
        self.response = ''              # Accumulated messages to print
        
        # Read in the book collection
        file = open('collection.txt')
        for line in file:
            if len(line) > 1:
                tuple = eval(line.strip())
                self.collection.append(Book(tuple[0], tuple[1]))
        file.close()

    def open(self):
        """Opens this library for business at the start of a new day."""
        pass

    def list_overdue_books(self):
        """Checks records and prints overdue notices to all
           delinquent patrons who have an overdue book."""
        
        global calendar
        current_date = calendar.get_date()
        for patron in self.patrons:
            p = Patron()
            for book in p.get_books():
                b = Book()
                if current_date > b.get_due_date():
                    print OverdueNotice()
                
    def issue_card(self, name_of_patron):
        """Allows the named person the use of this library. For
           convenience, immediately begins serving the new patron."""
        # additional code goes here
        self.serve(name_of_patron)

    def serve(self, name_of_patron):
        """Saves the given patron in an instance variable. Subsequent
           check_in and check_out operations will refer to this patron,
           so that the patron's name need not be entered many times."""
        pass
		
    def check_in(self, *book_numbers):
        """Accepts books being returned by the patron being served,
           and puts them back "on the shelf"."""
        p = Patron()
        for book in book_numbers:
            p.give_back(book)
            self.collection.remove(book)
        

    def search(self, string):
        """Looks for books with the given string in either the
           title or the author's name, and creates a globally
           available numbered list in self.found_books."""
        

    def create_numbered_list(self, items):
        """Creates and returns a numbered list of the given items,
           as a multiline string. Returns "Nothing found." if the
           list of items is empty."""
        pass

    def check_out(self, *book_numbers):
        """Checks books out to the patron currently being served.
           Books will be due seven days from "today".
           Patron must have a library card, and may have not more
           than three books checked out at a time."""
        for patron in book_numbers:
            if patron in self.patrons:
                p = Patron()
                if len(p.get_books())< 3:
                    for book in book_numbers:
                        p.take_book(book)
        
    def close(self):
        """Closes the library for the day."""
        pass

    def quit(self):
        pass

    def help(self):
        self.talk("""
help()
     Repeat this list of commands.
open()
     Opens the library for business; do this once each morning.
     
list_overdue_books()
     Prints out information about books due yesterday.
     
issue_card("name_of_patron")
     Allows the named person the use of the library.
     
serve("name_of_patron")
     Sets this patron to be the current patron being served.
     
search("string")
     Searches for any book or author containing this string
     and displays a numbered list of results.
     
check_out(books...)
     Checks out books (by number) to the current patron.
     
check_in(books...)
     Accepts returned books (by number) from the current patron.
     
close()
     Closes the library at the end of the day.

quit()
     Closes the library for good. Hope you never have to use this!""")

    # ----- Assorted helper methods (of Library) -----

    def talk(self, message):
        """Accumulates messages for later printing. A newline is
           appended after each message."""
        self.response += message + '\n'

    # Feel free to add any more helper methods you would like

#--------------------------------------------------------------

def main():
    library = Library()
    print len(library.collection), 'books in collection.'
    print "Ready for input. Type 'help()' for a list of commands.\n"
    command = '\0'
    while command != 'quit()':
        try:
            command = raw_input('Library command: ').strip()
            if len(command) == 0:
                print "What? Speak up!\n"
            else:
                eval('library.' + command)
                print library.response
                library.response = ''
        except AttributeError, e:
            print "Sorry, I didn't understand:", command
            print "Type 'help()' for a list of the things I do understand.\n"
        except Exception, e:
            print "Unexpected error:", e            
    
if __name__ == '__main__':
    main()
