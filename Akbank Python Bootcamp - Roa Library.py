class Library:
    def __init__(self, bookname, author, year, page):
        self.roa_lib = open("books.txt", "a+")
        
    def Quit(self):
        self.roa_lib.seek(0)
        self.roa_lib.close()
        del self.roa_lib
    
    def List_Books(self):
        self.roa_lib.seek(0)
        books = [line.strip().split(", ") for line in self.roa_lib.readlines()]
        booknames = []
        authors = []
        for i in range(len(books)):
            bookname = books[i][0]
            author = books[i][1]
            booknames.append(bookname)
            authors.append(author)
            print(f"Title: {bookname}, Author: {author}")
        self.roa_lib.close()
    
    def Add_Book(self):
        n = input("Which book do you want to add? \nWrite book name: ")
        a = input("Write book author: ")
        y = input("Write release year: ")
        p = input("Write number of pages: ")
        try:
            self.roa_lib.write(f"{n}, {a}, {y}, {p}\n")
            print(f"{n}, {a} added successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            self.roa_lib.close()
            
    def Remove_Book(self):
        self.roa_lib.seek(0)
        books = self.roa_lib.readlines()
        remove = input("Which book do you want to remove?")
        updated_books = [book for book in books if not book.startswith(remove)]
        self.roa_lib.seek(0)
        self.roa_lib.truncate()
        self.roa_lib.writelines(updated_books)
        print(f"{remove} deleted successfully.")
        self.roa_lib.close()
        while True:
            break
        
    def Search_Book(self):
        self.roa_lib.seek(0)
        books = self.roa_lib.readlines()
        search = input("Which book are you searching for?")
        for line in books:
            if search in line:
               print(line.strip())
               print("Book found.")
               return
            print("Book not found.")
        self.roa_lib.close()

while True:
    print("Welcome to the Roa Library \n1-List Books\n2-Add Book\n3-Remove Book\n4-Search Book\nq-Quit")
    option = input("Choose an option: \n").lower()
    
    lib = Library("bookname", "author", "year", "page")

    if option == "1":
        lib.List_Books()
    if option == "2":
        lib.Add_Book()
    if option == "3":
        lib.Remove_Book()
    if option == "4":
        lib.Search_Book()
    if option == "q":
        lib.Quit()
        break

