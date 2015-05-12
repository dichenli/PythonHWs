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

    def __init__(self, title, author):
        """Creates a book, not checked out to anyone."""
        self.title = title
        self.author = author
        self.due_date = None

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

    #Dichen Modified
    def __eq__(self, other):
        """Tests if this book equals the given parameter. Not
        required by assignment, but fairly important."""
        return type(self) == type(other) and self.author == other.author and self.title == other.title

#--------------------------------------------------------------

class Patron(object):
    """Represents a patron of the library. A patron has:
         * A name
         * A set of books checked out"""
    #Dichen Modified
    global calendar
    def __init__(self, name):
        """Constructs a new patron, with no books checked out yet."""
        self.name = name
        self.books = {} #Assumption here: Each patron can only take one copy of the same book!

    def get_name(self):
        """Returns this patron's name."""
        return self.name

    def get_books(self):
        """Returns the set of books checked out to this patron."""
        return self.books
    
    #Doesn't check whether patron has more than 3 books or whether the book is available or not!
    def take(self, book):
        """Adds a book to the set of books checked out to this patron."""
        self.books.add(book)
        book.set_due_date(calendar.get_date() + 7)


    #Dichen Modified
    def give_back(self, book):
        """Removes a book from the set of books checked out to this patron."""
        for self_book in self.books:
            if self_book == book:
                book.check_in()
                self.books.remove(self_book)


    def __str__(self):
        """Returns the name of this patron."""
        return self.name
    
    #Dichen Li. Not default!
    def __eq__(self, other):
        """Test if the given patron has the same name as the other patron, return true"""
        return self.get_name() == other.get_name()
        
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
        book = Book()
        for book in set_of_books:
            due_date = book.get_due_date()
            if due_date > current_date:
                message = message + "OVERDUE: " + book.get_title + ", by " + book.get_author + " (" + " was due on day " + str(book.due_date) + ")/n"
            elif due_date == current_date:
                message = message + "DUE: " + book.get_title + ", by " + book.get_author + " (due today)/n"
            else:
                message = message + "DUE: " + book.get_title + ", by " + book.get_author + " (" + " is due on day " + str(book.due_date) + ")/n"
        return message

#--------------------------------------------------------------

class Library(object):
    """Provides operations available to the librarian."""

    #Dichen Modified
    def __init__(self):
        """Constructs a library, which involves reading in a
           list of books that are in this library's collection."""
        
        # Create a global calendar, to be used by many classes
        global calendar
        calendar = Calendar(1)
        
        # Initialize some instance variables for _this_ library
        self.is_open = False            # Is library open?
        self.collection = []            # List of all Books
        self.patrons = {}               # Set of all Patrons
        self.patron_being_served = None # Current patron
        self.response = ''              # Accumulated messages to print
        self.found_books = {}
        
        # Read in the book collection
        file = open('collection.txt')
        number = 1
        for line in file:
            if len(line) > 1:
                tuple = eval(line.strip())
                self.collection.append(Book(tuple[0], tuple[1], number))
                number += 1
        file.close()

    #Dichen Li
    def open(self):
        """Opens this library for business at the start of a new day."""
        if self.is_open:
            self.talk("Invalid requirement, the library was already open!")
        else:
            self.is_open = True
            self.talk("Today is day %d ." % calendar.get_date())
            
    def list_overdue_for_patron(self, patron):
        """Returns overdue books notice for a single patron."""
        if not self.is_open:
            self.talk("The library is closed now. Please wait for openning before any operation.")
            return
        global calendar
        has_overdue = False
        for book in patron.get_books():
            if book.get_due_date() > calendar.get_date():
                has_overdue = True
        if has_overdue:
            message = "Dear " + patron.get_name() + ",\n" + "You have the following books: \n"
            message += str(OverdueNotice(patron.get_books()))
            return message
        else:
            return ''

    def list_overdue_books(self):
        """Checks records and prints overdue notices to all
           delinquent patrons who have an overdue book."""
        if not self.is_open:
            self.talk("The library is closed now. Please wait for openning before any operation.")
            return 
        message = ''
        for patron in self.patrons:
            message += list_overdue_for_patron(patron)
        self.talk(message)
            
            
    #Dichen Li  
    def issue_card(self, name_of_patron):
        """Allows the named person the use of this library. For
           convenience, immediately begins serving the new patron."""
        if not self.is_open:
            self.talk("The library is closed now. Please wait for openning before any operation.")
            return 
        new_patron = Patron(name_of_patron)
        for patron in self.patrons:
            if new_patron == patron:
                self.talk("%s was already issued a card!" % name_of_patron)
                self.serve(name_of_patron)
                return None
        self.patrons.add(new_patron)
        self.talk("%s has been issued a new card!" % name_of_patron)
        self.serve(name_of_patron)

    #Dichen Li
    def serve(self, name_of_patron):
        """Saves the given patron in an instance variable. Subsequent
           check_in and check_out operations will refer to this patron,
           so that the patron's name need not be entered many times."""
        if not self.is_open:
            self.talk("The library is closed now. Please wait for openning before any operation.")
            return 
        for patron in self.patrons:
            if patron.get_name() == name_of_patron:
                self.patron_being_served = patron
                self.talk("Now helping %s.\n%s has these books:\n" % name_of_patron)
                talk(create_numbered_list(self.patron_being_served.get_books()))
                return
        self.talk("The patron was not found! This person is not in patrons list")

##    def create_dictionary(self, books):
##        """Given a set of books, it returns a numbered dictionary"""
##        books_dic = {}
##        index = 1
##        for book in books:
##            books_dic[index] = book
##            index += 1
##        return books_dic

    #Dichen Modified
    def check_in(self, *book_numbers):
        """Accepts books being returned by the patron being served,
           and puts them back "on the shelf"."""
        if not self.is_open:
            self.talk("The library is closed now. Please wait for openning before any operation.\n")
            return 
        for number in book_numbers:
            if self.found_books[number]:
                self.patron_being_served.give_back(self.found_books[number])
                self.talk("%s returned to shelves.\n" % self.found_books[number].get_title())
            else:
                self.talk("Book already returned or was not checked out\n")
                


    #Dichen Modified
    def search(self, string):
        """Looks for books with the given string in either the
           title or the author's name, and creates a globally
           available numbered list in self.found_books."""
        if not self.is_open:
            self.talk("The library is closed now. Please wait for openning before any operation.\n")
            return 
        found_books = []
        for book in self.collection:
            if (book.get_title().lower()).find(string) >= 0 or (book.get_author().lower()).find(string) >= 0:
                found_books.append(book)
        if len(self.found_books) == 0:
            self.talk("Sorry, no book was found!")
        self.talk(create_numbered_list(found_books))


    #Dichen Li
    def create_numbered_list(self, items):
        """Creates and returns a numbered list of the given items,
           as a multiline string. Returns "Nothing found." if the
           list of items is empty."""
        if not self.is_open:
            self.talk("The library is closed now. Please wait for openning before any operation.")
            return 
        number = 1
        num_list = ""
        self.found_books = {}
        for item in items:
            num_list = num_list + "\t" + str(number) + ". " + str(item) + "\n"
            self.found_books[number] = item
            number += 1
        return num_list



    def check_out(self, *book_numbers):
        """Checks books out to the patron currently being served.
           Books will be due seven days from "today".
           Patron must have a library card, and may have not more
           than three books checked out at a time."""
        if not self.is_open:
            self.talk("The library is closed now. Please wait for openning before any operation.\n")
            return 
        if self.patron_being_served == None:
            self.talk("Error: There is no patron being served right now!\n")
            return
        elif len(self.patron_being_served.get_books()) + len(book_numbers) > 3:
            self.talk("Sorry, %s already has %d books checked out.\n" % (self.patron_being_served.get_name(), len(self.patron_being_served.get_books())))
            return
        for number in book_numbers:
            if self.found_books[number]:
                for patron_book in self.patron_being_served.get_books():
                    if self.found_books[number] != patron_book:
                        self.patron_being_served.take(self.found_books[number])
                        self.talk("%s, checked out to %s. \n" % (self.found_books[number].get_title(), self.patron_being_served.get_name()))
                    else:
                        self.talk("%s has already checked out a same book!\n" % self.patron_being_served.get_name())
            else:
                self.talk("Book unavailable!\n")


    #Dichen Li
    def close(self):
        """Closes the library for the day."""
        if self.is_open:
            self.is_open = False
            self.talk("The library is closed now!")
            calendar.advance()
        else:
            self.talk("The library was already closed!")

    #Dichen Li: It seems we need to write nothing here!
    def quit(self):
        self.talk("The library is closed and you are fired! Hope you find the next job soon...")

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
