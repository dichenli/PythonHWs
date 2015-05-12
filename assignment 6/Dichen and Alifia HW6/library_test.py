# Authors: Dave Matuszek and <Dichen Li and Alifia Haidry>
#--------------------------------------------------------------


import unittest
from library import *

lib = Library()
lib.open()

import library

class CalendarTest(unittest.TestCase):

    def test_calendar(self):
        cal = Calendar(0)
        self.assertEqual(0, cal.get_date())
        cal.advance()
        self.assertEqual(1, cal.get_date())
        cal.advance()
        cal.advance()
        self.assertEqual(3, cal.get_date())

class BookTest(unittest.TestCase):

    def setUp(self):
        global book
        global second_book
        global third_book
        book = Book("Contact", "Carl Sagan")
        second_book = Book("20,000 Leagues Under the Seas", "Jules Verne")
        third_book = Book("A Quiet Belief in Angels","R. J. Ellory")
        self.assertTrue(type(book) is Book)
        self.assertTrue(type(second_book) is Book)
        self.assertTrue(type(third_book) is Book)        

    def test_get_title(self):
        self.assertEqual("Contact", book.get_title())
        self.assertEqual("20,000 Leagues Under the Seas", second_book.get_title())
        self.assertEqual("A Quiet Belief in Angels", third_book.get_title())
        
    def test_get_author(self):
        self.assertEqual("Carl Sagan", book.get_author())
        self.assertEqual("Jules Verne", second_book.get_author())
        self.assertEqual("R. J. Ellory", third_book.get_author())

    def test_get_due_date(self):
        self.assertEqual(None, book.get_due_date())
        self.assertEqual(None, book.get_due_date())
        self.assertEqual(None, book.get_due_date())

    def test_book_check_out_and_check_in(self):
        book = Book("Contact", "Carl Sagan")
        second_book = Book("20,000 Leagues Under the Seas", "Jules Verne")
        third_book = Book("A Quiet Belief in Angels","R. J. Ellory")
        self.assertEqual(None, book.get_due_date())
        lib.serve("Amy Gutmann")
        book.check_out(17)
        self.assertEqual(17, book.get_due_date())
        book.check_in()
        self.assertEqual(None, book.get_due_date())
        self.assertEqual(None, second_book.get_due_date())
        lib.serve("Voldemort")
        second_book.check_out(9)
        self.assertEqual(9, second_book.get_due_date())
        second_book.check_in()
        self.assertEqual(None, second_book.get_due_date())
        self.assertEqual(None, third_book.get_due_date())
        lib.serve("Dumbledore")
        third_book.check_out(32)
        self.assertEqual(32, third_book.get_due_date())
        third_book.check_in()
        self.assertEqual(None, third_book.get_due_date())

class PatronTest(unittest.TestCase):

    def setUp(self):
        global lib
        lib = Library()
        lib.open()

    def test_patron(self):
        patron = Patron("Amy Gutmann")
        self.assertEquals("Amy Gutmann", patron.get_name())
        self.assertEquals(set([]), patron.get_books())
        lib.issue_card("Voldemort")
        lib.patron_being_served
        self.assertEquals("Voldemort", lib.patron_being_served.get_name())
        lib.search("thomas")
        book = lib.found_books[3]
        lib.check_out(3)
        self.assertEquals(set([book]), lib.patron_being_served.get_books())
        
    def test_take(self):
        book = Book("Contact", "Carl Sagan")
        lib.issue_card("Amy Gutmann")
        lib.patron_being_served
        lib.search("thomas")
        books_checked_out = lib.found_books[3]
        lib.check_out(3)
        self.assertEquals(set([books_checked_out]),lib.patron_being_served.get_books())
        lib.patron_being_served.take(book)
        book.check_out(11)
        self.assertEquals(11, book.get_due_date())
        
    def test_give_back(self):
        book = Book("A Lost Lady","Willa Cather")
        lib.issue_card("Alifia")
        lib.patron_being_served
        lib.search("the")
        books = lib.found_books[8]
        lib.check_out(8)
        lib.patron_being_served.give_back(books)
        lib.check_in(8)
        self.assertEquals(set([]),lib.patron_being_served.get_books())



class LibraryTest(unittest.TestCase):

    def setUp(self):
        global lib
        lib = Library()
        lib.open()
        lib.issue_card("Amy")

    def test_init(self):
        self.assertEquals(library.calendar.get_date(), 1)       
        self.assertEquals(lib.collection[0].get_author(), "Jules Verne")
        self.assertEquals(lib.collection[0].get_title(), "20,000 Leagues Under the Seas")

    def test_serve(self):
        lib.response = ''
        lib.serve("Amy")
        self.assertEquals(lib.response, "Now helping Amy.\nAmy has these books:\n\tNo book was found!\n")
        self.assertEquals(str(lib.patron_being_served), "Amy")
        
        lib.response = ''
        lib.serve("Bilibili")
        self.assertEquals(lib.response, "The patron was not found! This person is not in patrons list\n")
        
        lib.close()
        lib.response = ''
        lib.serve("Amy")
        self.assertEquals(lib.response, "The library is closed now. Please wait for openning before any operation.\n")
        
        
    def test_open(self):
        lib.close()
        lib.open()
        self.assertTrue(lib.is_open)
        lib.response = ''
        lib.open()
        self.assertEquals(lib.response, "Invalid requirement, the library was already open!\n")

            
    def test_list_overdue_for_patron(self):
        lib.serve("Amy")
        lib.search("Thomas")
        lib.check_out(1, 2) #check out two books to Amy
        
        lib.response = ''
        self.assertEquals(lib.list_overdue_for_patron(lib.patron_being_served), '')
        
        for i in range(1, 10): #forward day by 10
            lib.close()
            lib.open()
        lib.serve("Amy")
        lib.response = ''
        answer1 = 'Dear Amy,\nYou have the following books: \nOVERDUE: Buddenbrooks, by Thomas Mann ( was due on day 8)\nOVERDUE: Black Sunday, by Thomas Harris ( was due on day 8)\n\n'
        answer2 = 'Dear Amy,\nYou have the following books: \nOVERDUE: Black Sunday, by Thomas Harris ( was due on day 8)\nOVERDUE: Buddenbrooks, by Thomas Mann ( was due on day 8)\n\n'
        response = lib.list_overdue_for_patron(lib.patron_being_served)
        self.assertTrue(response == answer1 or response == answer2)


    def test_list_overdue_books(self):
        lib.serve("Amy")
        lib.search("Thomas")
        lib.check_out(1) #check out two books to Amy
        lib.issue_card("Bilibili")
        lib.search("Thomas")
        lib.check_out(1) #check out two books to Bilibili
        lib.issue_card("Canned Soda") #Add person, no book checked out

        lib.response = ''
        lib.list_overdue_books()
        self.assertEquals(lib.response, 'No overdue book was found!\n')

        for i in range(1, 10):
            lib.close()
            lib.open()
        lib.serve("Amy")
        lib.response = ''
        lib.list_overdue_books()
        answer1 = 'Dear Amy,\nYou have the following books: \nOVERDUE: Black Sunday, by Thomas Harris ( was due on day 8)\n\nDear Bilibili,\nYou have the following books: \nOVERDUE: Buddenbrooks, by Thomas Mann ( was due on day 8)\n\n\n'
        answer2 = 'Dear Bilibili,\nYou have the following books: \nOVERDUE: Buddenbrooks, by Thomas Mann ( was due on day 8)\n\nDear Amy,\nYou have the following books: \nOVERDUE: Black Sunday, by Thomas Harris ( was due on day 8)\n\n\n'
        self.assertTrue(lib.response == answer1 or lib.response == answer2)

                

    def test_issue_card(self):
        lib.response = ''
        lib.issue_card("Bilibili")
        self.assertEquals(lib.response, "Bilibili has been issued a new card!\nNow helping Bilibili.\nBilibili has these books:\n\tNo book was found!\n")
        self.assertEquals(str(lib.patron_being_served), "Bilibili")

        lib.response = ''
        lib.issue_card("Bilibili")
        self.assertEquals(lib.response, 'Bilibili was already issued a card!\nNow helping Bilibili.\nBilibili has these books:\n\tNo book was found!\n')
        
        
        
    def test_check_in(self):
        lib.serve("Amy")
        lib.search("Thomas")
        lib.check_out(1)
        lib.close()
        lib.open()
        lib.serve("Amy")
        lib.check_in(1)
        self.assertEqual(lib.patron_being_served.books ,set({}))
        
    def test_search(self):
        lib.response = ''
        lib.search("52 Pick-up")
        self.assertEqual(lib.response, '\t1. 52 Pick-up, by Elmore Leonard\n\n')
       
    def test_create_numbered_list(self):
        lib.create_numbered_list([lib.collection[0], lib.collection[3]])
        self.assertEqual("20,000 Leagues Under the Seas", lib.found_books[1].get_title())        
        self.assertEqual("52 Pick-up", lib.found_books[2].get_title())
        self.assertEqual(2, len(lib.found_books))        

        lib.create_numbered_list([])
        self.assertEqual(0, len(lib.found_books))   
       
    def test_check_out(self):
        lib.serve("Amy")
        lib.search("20,000 Leagues Under the Seas")
        lib.response = ''
        lib.check_out(1)
        self.assertEquals(lib.patron_being_served.books, {lib.collection[0]})
        self.assertEquals(lib.response, "20,000 Leagues Under the Seas, checked out to Amy. \n\n")

        lib.close()
        lib.response = ''
        lib.check_out(1)
        self.assertEquals(lib.response, "The library is closed now. Please wait for openning before any operations.\n\n")

        lib.open()
        lib.search("20,000 Leagues Under the Seas")
        lib.response = ''
        lib.check_out(1)
        self.assertEquals(lib.response, "Error: There is no patron being served right now!\n\n")

      
    def test_close(self):
        lib.response = ''
        lib.close()
        self.assertEquals(lib.response, "The library is closed now!\n")

        lib.response = ''
        lib.close()
        self.assertEquals(lib.response, "The library was already closed!\n")

        lib.response = ''
        lib.open()
        self.assertEquals(lib.response, "Today is day 2.\n")
        
    def test_quit(self):
        lib.response = ''
        lib.quit()
        self.assertEquals(lib.response, "The library is closed and you are fired! Hope you find the next job soon...\n")

unittest.main()


