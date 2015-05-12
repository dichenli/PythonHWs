
class aaa(object):
    def __init__(self, st):
        self.a = st
        global b
        b = bbb()

    def __str__(self):
        return self.a

    def __eq__(self, other):
        return self.a == other.a

    def change(self, st):
        self.a = st
        b.change()

    def test_method(self):
        print "test_method\n"
        return
    
    def give_str (self):
        return "abcdefg"

class bbb(object):
    def __int__(self):
        self.b = "no change"
    def change(self):
        self.b = "changed"
    def puts(self):
        print self.b

class ccc(object):
    def __init__(self, st):
        self.c = st
        global b
    def change(self):
        b.change()

    def puts(self):
        b.puts()

testa = aaa("aaa")
testc = ccc("ccc")
testa.change("aa")
testc.puts()

        
        
    
##test = aaa("aa")
####test.test_method()
##test2 = aaa("aaa")
##test3 = aaa("aaaa")
##testlist = {aaa("aa"), aaa("aaa"), aaa("aaaa")}
##
##for testa in testlist:
##    testobj = testa
##    testobj.change("bb")
##    print str(testobj)
##    print str(testa)
##
##print len({})
####print str(test)
####print test == test2
####print test == test3
####
####def test_star(*book_numbers):
####    print type(book_numbers)
####    for book in book_numbers:
####        print book
####
####test_star(1, 2, 3)
####
#####print str(nil) == nil
####
####print type("%d. dsf" % 1)
####
####print type(test)
####
####if 0 == None:
####    print "0"
##
####testb = bbb()
####testb.add(test)
####testb.add(test2)
####testb.add(test3)
####testb.puts()
##
##str1 = "ABCDEFG"
##str2 = "g"
##print str1.lower().find(str2)
##
####
####
####print test.give_str()
####
####
####set1 = {1, 2, 3}
####set1.add(4)
####set1.remove(2)
####print set1
##
##
##a = {test, test2, test3}
##test4 = aaa("aa")
##for tests in a:
##    if test4 == tests:
##        print "True"
##if test4 in a:
##    print "True"
##
##def foo():
##    return
##f = foo()
##print f
##
a = {1: "a1", 2: "a2", 3: "a3"}
##print a[1]
##print len(a)

if 4 in a:
    print "4"
