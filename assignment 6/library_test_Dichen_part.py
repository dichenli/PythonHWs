import unittest
from library import *

lib = Library()
lib.open()

import library


class LibraryTest(unittest.TestCase):

    def setUp(self):
        global lib
##        global calendar
        lib = Library()
#Question: initialize library every time? How to avoid that but still make the tests working
        lib.open()
        lib.issue_card("Amy")
##        lib = Library()
##Question: Why local initialization (if no global lib defined) doesn't apply to the other tests methods?

    def test_init(self):
        print "\ntest_init"
        self.assertEquals(library.calendar.get_date(), 1)       
##Question!! Why doesn't work?
        self.assertEquals(lib.collection[0].get_author(), "Jules Verne")
        self.assertEquals(lib.collection[0].get_title(), "20,000 Leagues Under the Seas")

    def test_serve(self):
        print "\ntest_serve"
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
        print "\ntest_open"
        lib.close()
        lib.open()
        self.assertTrue(lib.is_open)
        lib.response = ''
        lib.open()
        self.assertEquals(lib.response, "Invalid requirement, the library was already open!\n")
        #assertEqual()
        
            
    def test_list_overdue_for_patron(self):
        print "\ntest_list_overdue_for_patron"
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
#Question: How to solve problems like random iteration order in set?


    def test_list_overdue_books(self):
        print "\ntest_list_overdue_books"
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
        print "\ntest_issue_card"
        lib.response = ''
        lib.issue_card("Bilibili")
        self.assertEquals(lib.response, "Bilibili has been issued a new card!\nNow helping Bilibili.\nBilibili has these books:\n\tNo book was found!\n")
        self.assertEquals(str(lib.patron_being_served), "Bilibili")

        lib.response = ''
        lib.issue_card("Bilibili")
        self.assertEquals(lib.response, 'Bilibili was already issued a card!\nNow helping Bilibili.\nBilibili has these books:\n\tNo book was found!\n')
        
        
        
    def test_check_in(self):
        print "\ntest_check_in"
        lib.serve("Amy")
        lib.search("Thomas")
        lib.check_out(1)
        lib.close()
        lib.open()
        lib.serve("Amy")
        lib.check_in(1)
        self.assertEqual(lib.patron_being_served.books ,set({}))
        
    def test_search(self):
        print "\ntest_search"
        lib.response = ''
        lib.search("52 Pick-up")
        self.assertEqual(lib.response, '\t1. 52 Pick-up, by Elmore Leonard\n\n')
       
    def test_create_numbered_list(self):
        print "\ntest_create_numbered_list"
        lib.create_numbered_list([lib.collection[0], lib.collection[3]])
        self.assertEqual("20,000 Leagues Under the Seas", lib.found_books[1].get_title())        
        self.assertEqual("52 Pick-up", lib.found_books[2].get_title())
        self.assertEqual(2, len(lib.found_books))        

        lib.create_numbered_list([])
        self.assertEqual(0, len(lib.found_books))   
       
    def test_check_out(self):
        print "\ntest_check_out"
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
        print "\ntest_close"
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
        print "\ntest_quit"
        lib.response = ''
        lib.quit()
        self.assertEquals(lib.response, "The library is closed and you are fired! Hope you find the next job soon...\n")

unittest.main()
