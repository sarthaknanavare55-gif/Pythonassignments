class Library:
    def __init__(self,book_name,author,availability_status=True):
        self.book_name=book_name
        self.author=author
        self.availability_status=availability_status
    def check_out(self):
        if self.availability_status:
            self.availability_status=False
            print(f"Book '{self.book_name}' by {self.author} has been checked out.")
        else:
            print(f"Sorry, {self.book_name} is currently not available. ")

    def return_book(self):
        if not self.availability_status:
            self.availability_status=True
            print(f"Book '{self.book_name}' has been returned and is now available. ")
        else:
            print(f" Book '{self.book_name}' was not checked out.")

    def display_book_info(self):
        status="Available" if self.availability_status else "Checked out "
        print(f"Book:{self.book_name}, Author: {self.author}, Status:{status}")

book1=Library("Rich Dad Poor Dad"," Robert Kiyosaki")
book2=Library("Clean Code", "Robert C. Martin")  
book3=Library("The Pragmatic Programmer","Andrew Hunt")      

book1.display_book_info()
book2.display_book_info()
book3.display_book_info()

print("\n Checking out Books...")
book1.check_out()
book2.check_out()
book3.check_out()

print("\n Returning Books...")
book1.return_book()
book2.return_book()

print("\n Final Book Statuse.")
book1.display_book_info()
book2.display_book_info()
book3.display_book_info()