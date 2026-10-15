class Publication:
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def set_title(self, title):
        self.title = title
    
    def set_author(self,author):
        self.author = author
    
    def display_info(self):
        print(f"Publication Information \nTitle: {self.title} \nAuthor: {self.author}")
        
class Book:
    
    def __init__(self, title, author, number_of_pages):
        super().__init__(title, author)
        self.number_of_pages = number_of_pages
    
    def title(self):
        print("Title: ")
        return self.title
    
    def author(self):
        print("Author: ")
        return self.author
        
    def number_of_pages(self, val):
        if val == int == False:
            print("Number of pages must be an integer.")
            
        if val <= 0:
            print("Must be a positive integer.")
        self.number_of_pages = val
        
    def set_no_pgs(self, np):
        self.number_of_pages = np
        
    def get_no_pgs(self):
        return self.number_of_pages
        
    def display_info(self):
        print(f"Book Information \nTitle: {self.title} \nAuthor: {self.author}")
        
class Magazine:
    
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
    
    def title(self):
        print("Title: ")
        return self.title
        
    def author(self):
        print("Author: ")
        return self.author
        
    def issue_number(self, val):
        if val == int == False:
            print("Number of pages must be an integer.")
            
        if val <= 0:
            print("Must be a positive integer.")
        self.issue_number = val
        
    def set_in(self, isn):
        self.issue_number = isn
        
    def get_in(self):
        return self.issue_number
        
    def display_info(self):
        print(f"Magazine Information \nTitle: {self.title} \nAuthor: {self.author}")
        
        
pub1 = Publication("Poop", "Pee poop")
book1 = Book("yay", "Pee RR poop", 76)
mag1 = Magazine("Pee", "Pooga", 8)
