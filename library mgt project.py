class Library:
    def __init__(self,list_of_books ):
        self.list_of_books = list_of_books
        self.issue_data = {}
        for books in self.list_of_books:
            self.issue_data[books] = None

    def display_books(self):
        for index,books in enumerate (self.list_of_books):
           print (f"({index}){books}")

    def issue_books(self,person,book):
        if book in self.list_of_books:
            if self.issue_data[book] is None:
                self.issue_data[book] = person
                print("Book Issued successfully!")
            else:
                print("Sorry!! this book is issued to", self.issue_data[book])
        else:
            print("Wrong Input!! please select from the listed Books")

    def return_books(self,person,book):
        if book in self.list_of_books:
            if self.issue_data[book] is not None:
                self.issue_data.pop(book)
            else:
                print(" Alert!! this book is not issued ")
        else:
            print("Invalid Book Name !!")

    def donate_books(self,book):
        self.list_of_books.add(book)
        self.issue_data[book] = None

    def delete_books(self,book):
        self.list_of_books.remove(book)
        self.issue_data.pop(book)





print(" ---------------------------------------------")
print("|     Welcome to  VIPS Library (BCA)          |")
print(" ---------------------------------------------")
pin = 1236
list_of_books = {"Data Structures in C","Database Management System","Introductin to C language","Mathematics II","POM"}
jatin = Library(list_of_books)
a = 1
while a > 0 :
    print("           ................              ")
    print("               Main Menu                 ")
    print("           ................              ")
    print("\t1 : Display all Books")
    print("\t2 : Issue a Book")
    print("\t3 : Return a Book")
    print("\t4 : Donate a Book")
    print("\t5 : Delete a Book")
    opt = int(input("Enter your choice : "))
    if opt == 1:
        jatin.display_books()
    if opt == 2:
        _input1=input("Enter Your Name : ")
        _input2=input("Enter Book Name : ")

        jatin.issue_books(_input1,_input2)
    if opt == 3:
        _input3 = input("Enter Your Name : ")
        _input4 = input("Enter Book Name : ")
        jatin.return_books(_input3,_input4)
    if opt == 4:
        _input5 = input("Enter Book Name : ")
        jatin.donate_books(_input5)
        print("Thank you for donating books to VIPS library")
    if opt == 5:
        _input6=int(input("Enter Pin to delete : "))
        if _input6 == pin:
             _input7=input("Enter Book Name : ")
             jatin.delete_books(_input7)
             print("Deletion Successfull ... !!")
        else:
            print("Invalid Pin !! Deletion is unsuccessfull")



