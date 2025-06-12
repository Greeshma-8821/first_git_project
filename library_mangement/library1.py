class Book:
    def __init__(self,isbn,title,author,genre,copies,book_type):
        self.isbn=isbn
        self.title=title
        self.author=author
        self.genre=genre
        self.copies=copies
        self.book_type=book_type
        self.waitlist=[]
        
class LibraryBranch:
    def __init__(self,branch_id,location,operating_hours):
        self.branch_id=branch_id
        self.location=location
        self.operating_hours=operating_hours

class Member:
    def __init__(self,name,member_id,membership_type,books_issued,overdue,fine,total_books_borrowed,avg_reading_time,reading_challenges,reading_history):
        self.name=name
        self.member_id=member_id
        self.membership_type=membership_type
        self.books_issued=books_issued
        self.overdue=overdue
        self.fine=fine
        self.total_books_borrowed=total_books_borrowed
        self.avg_reading_time=avg_reading_time
        self.reading_challenges=reading_challenges
        self.reading_history=reading_history
    def calculate_fine(self, rate_per_day=5):
        self.fine = self.overdue * rate_per_day
        return self.fine
    

class Library:
    def __init__(self,books,branch,member):
        self.books=books
        self.branch=branch 
        self.member=member   

    def get_member_by_id(self,member_id):
        for m in self.member:
            if m.member_id==member_id:
                return m
        return None
    def register_member(self, name, member_id, membership_type): 
        new_member = Member(
            name=name,
            member_id=member_id,
            membership_type=membership_type,
            books_issued=0,
            overdue=0,
            fine=0,
            total_books_borrowed=0,
            avg_reading_time="N/A",
            reading_challenges=0,
            reading_history="None"
        )
        self.member.append(new_member)
        return new_member
    def recommend_books(self, membership_type):
        recommendations = []
        if membership_type == "Premium":
            recommendations.extend([
            "1. The Palace of Illusions by Chitra Banerjee Divakaruni (Mythology)",
            "2. The Psychology of Money by Morgan Housel (Science Fiction)",
            "3. Shutter Island by Dennis Lehane (Mystery)",
            "4. Steve Jobs by Walter Isaacson (Biography)"
        ])
        elif membership_type == "Gold":
            recommendations.extend([
            "1. Harry Potter and the Philosopher's Stone by J.K Rowling (Science Fiction)",
            "2. The Immortals of Meluha by Amish Tripathi (Mythology)",
            "3. The Adventures of Sherlock Holmes by Arthur Conan Doyle (Mystery)",
            "4. Make, Think, Imagine by John Browne (Biography)"
        ])
        else:
           recommendations.append("No recommendations available for this membership type.")
        return recommendations
    def borrow_book(self, member_id, isbn):
        member = self.get_member_by_id(member_id)
        if not member:
          return "Member not found."

        if member.books_issued >= 5:
          return "Limit reached! You can't issue more than 5 books."

        for book in self.books:
          if book.isbn == isbn:
            if book.copies > 0:
                book.copies -= 1
                member.books_issued += 1
                member.total_books_borrowed += 1
                # Optional: update reading history or genre tracking
                return f"Book '{book.title}' issued successfully to {member.name}."
            else:
                book.waitlist.append(member_id)
                return f"'{book.title}' is currently unavailable. You've been added to the waitlist."
    
        return "Book not found."

book1=Book(101,"Norse mythology","NeilGaiman","prose",20,"Mythology")
book2=Book(102,"My Gita","Devdutt Patanaik","poetry",50,"Mythology")
book3=Book(103,"The Rise of Hastinapur","Sharath Komarraju","drama",30,"Mythology")
book4=Book(104,"The Palace of Illusions","chitra Banerjee Divakaruni","prose",25,"Mythology")
book5=Book(105,"The Immortals of Meluha","Amish Tripathi","prose",35,"Mythology")
book6=Book(106,"The Psychology of Money","Morgan Housel","prose",40,"Science Fiction")
book7=Book(107,"Thinking,Fast and Slow","Daniel Kahneman","prose",45,"Science Fiction")
book8=Book(108,"The Courage to Be Disliked","Fumitake Koga","prose",20,"Science Fiction")
book9=Book(109,"Harry Potter and the Philosopher's Stone","J.K Rowling","prose",60,"Science Fiction")
book10=Book(110,"The Lord of the Rings","J.R.R Tolkien","prose",30,"Science Fiction")


branch1=LibraryBranch("lb001","Hanumakonda",8)
branch2=LibraryBranch("lb002","Borabanda",8)
branch3=LibraryBranch("lb003","Secendrabad",10)
branch4=LibraryBranch("lb004","Koti",12)
branch5=LibraryBranch("lb005","shamshabad",8) 




m1=Member("John Smith","LM001","Premium",2,0,0,25,"8.5 days per book",25,"Mythology(20%),Science Fiction(28%),Mystery(34%),Biograpy(21%)")
m2=Member("Vedasri","LM002","Premium",3,6,30,47,"9 days per book",47,"Mythology(25%),Science Fiction(25%),Mystery(33%),Biograpy(27%)")
m3=Member("Mythri","LM003","Premium",3,0,0,40,"7 days per book",40,"Mythology(28%),Science Fiction(29%),Mystery(34%),Biograpy(11%)")
m4=Member("Nikethan","LM004","Premium",2,10,50,29,"10 days per book",29,"Mythology(20%),Science Fiction(28%),Mystery(34%),Biograpy(10%)")
m5=Member("Gopal","LM005","Premium",2,0,0,26,"9 days per book",26,"Mythology(23%),Science Fiction(42%),Mystery(23%),Biograpy(11%)")
m6=Member("Padmavathi","LM006","Gold",3,0,0,35,"8 days per book",35,"Mythology(20%),Science Fiction(28%),Mystery(34%),Biograpy(21%)")
m7=Member("Shiva","LM007","Gold",1,3,15,30,"11 days per book",30,"Mythology(20%),Science Fiction(28%),Mystery(34%),Biograpy(21%)")
m8=Member("Rajamouli","LM008","Gold",2,4,20,46,"9 days per book",46,"Mythology(25%),Science Fiction(17%),Mystery(39%),Biograpy(22%)")
m9=Member("vikram","LM009","Gold",3,5,25,37,"7.7 days per book",37,"Mythology(22%),Science Fiction(88%),Mystery(34%),Biograpy(11%)")
m10=Member("Vishwanath","LM010","Gold",1,0,0,33,"7 days per book",30,"Mythology(20%),Science Fiction(28%),Mystery(34%),Biograpy(21%)")
library=Library([book1,book2,book3,book4,book5,book6,book7,book8,book9,book10],[branch1,branch2,branch3,branch4,branch5],[m1,m2,m3,m4,m5,m6,m7,m8,m9,m10])



choice=int(input("If you already a member press 1\nDo you want to join as a member press 2\n:"))


if choice==1:
    member_id_input=input("Enter Member ID:")
    member=library.get_member_by_id(member_id_input)
    if member:
        print("1.View Profile\n2.Borrow a Book\n:")
        action=int(input("Choose an action:"))
        if action==1:
            fine=member.calculate_fine()
            print(f"""
            Member:{member.name}
            Membership:{member.membership_type}
            Books Borrowed This Year:{member.total_books_borrowed}
            Favorite Genres:{member.reading_history}
            Average Reading Time:{member.avg_reading_time}
            Current Status:
            -Books Issued:{member.books_issued}/5
            -Overdue Books:{member.overdue}
            -Pending Fines:Rs.{member.fine}
            Reading Challenge Progress:
           "50 Books Challenge 2025":{member.reading_challenges}/50
            """)
            print("\n=======RECOMMENDATIONS FOR YOU=========")
            recs=library.recommend_books(member.membership_type)
            for book in recs:
               print(book)
        elif action==2:
          isbn=int(input("enter the ISBN of the book to borrow:"))
          message=library.borrow_book(member_id_input,isbn)
          print(message)
elif choice==2:
    name = input("Enter your name: ")
    member_id = input("Enter new Member ID (e.g., LM011): ")
    membership_type = input("Enter membership type (Premium/Gold): ")
    new_member = library.register_member(name, member_id, membership_type)
    print("New member registered successfully:")
    print(f"Name: {new_member.name}")
    print(f"Member ID: {new_member.member_id}")
    print(f"Membership Type: {new_member.membership_type}")
    print(f"Books Issued: {new_member.books_issued}")
    print(f"Fine: Rs.{new_member.fine}")
    print(f"Reading History: {new_member.reading_history}")
    print("\nWelcome! Based on your membership type, here are some book recommendations:")
    recs=library.recommend_books(new_member.membership_type)
    for book in recs:
        print(book)
else:
    print("member not found")
