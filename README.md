# Library-Management-System
User first asked if they're subs of Library
If user selects Yes, they move ahead without adding their name to Subscribers.txt. If they select No, their name is added to Subscribers.txt

Further User has four Options to choose from. List all the books, Donate a book, Borrow a Book, Return Borrowed Book.

Show all Books: 
    >> Creates an empty List 
    >> Appends texts form books.txt to the Empty list through 'for loop' 
    >> prints all elements from List through another 'for loop'

Donate a Book:
    >> Asks for name of the book 
    >> Append name of the book in books.txt 
    >> Says thanks to Donor.

Borrow a Book: 
    >> Starting 9 line are as same as 'Show all Books' method for displaying the available books (when printing, enumerate is used in for loop) 
    >> User asked to enter Serial Number of book (Index of element in List) {errors are not handled here. For example if user enters any other character than 0 to last        index it will give error}
    >> User enters a number from 0 to last index >> Element (Book Name) is saved in variable 'selectedBookName' 
    >> Name of Borrower is asked  
    >> Selected element is removed from List 
    >> Books.txt is opened in write mode 
    >> All elements are written in books.txt through for loop 
    >> lended_books.txt is open in append mode
    >> File is appended with current datetime, borrower name and Borrowed Book Name with '-' in between

Return a Book:
    >> lended_books.txt is opened
    >> Empty List is made
    >> Each line from lended_book.txt is appended in list
    >> Also each line is split by '-' and saved in new list 'splitBook'
    >> Book name is stored in new variable 'splitbookname' (book name is last element in splitBook)
    >> Elements from list is printed with index number through for loop & enumerate
    >> User asked to serial number of book they wants to return
    >> Selected element is removed from list
    >> books.txt is opend as append mode
    >> value of splitbookname which containes name of the book retured by user is appended in books.txt
