from datetime import datetime
class FiveDegreeLibrary:
    wlcm = "Welcome to the Library"
    print(wlcm)

    def userSignUp(self):
        partOfLib = input("Are you a subscriber of the Library? [Y]Yes / [N]No: ").upper()
        if partOfLib == "N":
            subname = input("Enter your name: ").upper()
            todaydate = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
            with open("subscribers.txt","a") as subs:
                    subs.write("\n["+todaydate+"] "+ subname)
            print(subname, "has subscribed to 5D Library.")
        elif partOfLib == "Y":
            subname = input("Enter your Name: ").upper()
            print("Welcome back",subname)
        else:
            print("Invalid Input")
            self.userSignUp()

    def userActions(self):
        while True:
            userAc = input("\n[S]Show books\n[D]Donate a book\n"
                  "[B]Borrow a book\n[R]Return a book\n[E]Exit Library\n>>>").lower()
            if userAc == "s": self.showBooks()
            elif userAc == "d": self.donateBooks()
            elif userAc == "b": self.borrowBook()
            elif userAc == "r": self.returnBook()
            elif userAc == "e": break

    def showBooks(self):
        print("\n_____List of Books______")
        booksArr = []
        with open("books.txt") as book:
            count = 0
            # Strips the newline character
            for line in book:
                count += 1
                booksArr.append("{}: {}".format(count, line.strip()))
            for i in booksArr:
                print(i)

    def donateBooks(self):
        bookname = input("Name of book: ").capitalize()
        with open("books.txt", "a") as book:
            book.write("\n"+bookname)
        print("Thanks")

    def borrowBook(self):
        print("\n_____List of Available Books______")
        booksArr = []
        with open("books.txt") as book:
            count = 0
            for line in book:
                count += 1
                booksArr.append(line.strip())
            for i,j in enumerate(booksArr):
                print(f'[{i}]',j)

        selectedBook = int(input("Enter Serial No. of the book you want:\n>>>"))
        selectedBookName = booksArr[selectedBook]
        borrowerName = input("Enter your name again: ").capitalize()
        booksArr.pop(selectedBook)
        with open("books.txt","w") as bookUp:
            for y in booksArr:
                bookUp.write(y+"\n")
        with open("lended_books.txt", "a") as lendedBooks:
            todaydate = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
            lendedBooks.write("["+todaydate+"] - "+ borrowerName + " - " + selectedBookName )

        print("Book borrowed by you successfully! \n Return it as soon as possible.")

    def returnBook(self):
        with open("lended_books.txt") as lendedBooks:
            booklist = []
            count = 0
            for line in lendedBooks:
                count += 1
                splitBook = line.split("-")
                splitbookname = splitBook[len(splitBook)-1]
                booklist.append(line.strip())
            for i,j in enumerate (booklist): print(f'[{i}] {j}')
            selection = int(input("Enter serial number of the book you wanna return: \n >>>"))
            booklist.pop(selection)
            with open("lended_books.txt", "w") as lendedbookUp:
                for y in booklist:
                    booklist.write(y + "\n")

            with open("books.txt", "a") as bookUp:
                bookUp.write(splitbookname)



person1 = FiveDegreeLibrary()
person1.userSignUp()
person1.userActions()
