from datetime import datetime, timedelta

# In-memory data structures
books = []
members = []
borrowed_books = []
waitlists = {}

# Add a book
def add_book(isbn, title, author, genre, copies, book_type):
    for book in books:
        if book["isbn"] == isbn:
            book["copies"] += copies
            return
    books.append({
        "isbn": isbn,
        "title": title,
        "author": author,
        "genre": genre,
        "copies": copies,
        "type": book_type
    })

# Register member
def register_member(member_id, name, contact, membership_type):
    for member in members:
        if member["id"] == member_id:
            return  # already registered
    members.append({
        "id": member_id,
        "name": name,
        "contact": contact,
        "type": membership_type
    })

# Issue a book
def issue_book(member_id, isbn, branch_id):
    for book in books:
        if book["isbn"] == isbn:
            if book["copies"] > 0:
                # Check if member has overdue
                for record in borrowed_books:
                    if record["member_id"] == member_id:
                        due_date = datetime.strptime(record["due_date"], "%d-%m-%Y")
                        if datetime.now() > due_date:
                            print("Cannot issue: Member has overdue books.")
                            return False
                # Issue book
                due_date = (datetime.now() + timedelta(days=14)).strftime("%d-%m-%Y")
                borrowed_books.append({
                    "member_id": member_id,
                    "isbn": isbn,
                    "due_date": due_date,
                    "branch_id": branch_id
                })
                book["copies"] -= 1
                print(f"Book issued to {member_id} till {due_date}")
                return True
            else:
                print("Book not available, adding to waitlist.")
                add_to_waitlist(member_id, isbn)
                return False
    print("Book not found.")
    return False

# Return book and check fine
def return_book(member_id, isbn, return_date_str, condition):
    for i in range(len(borrowed_books)):
        record = borrowed_books[i]
        if record["member_id"] == member_id and record["isbn"] == isbn:
            due_date = datetime.strptime(record["due_date"], "%d-%m-%Y")
            return_date = datetime.strptime(return_date_str, "%d-%m-%Y")
            fine = calculate_fine(return_date, due_date, condition)
            borrowed_books.pop(i)
            for book in books:
                if book["isbn"] == isbn:
                    if condition.lower() == "good":
                        book["copies"] += 1
                    break
            print(f"Book returned. Fine: rs{fine:.2f}")
            notify_waitlist(isbn)
            return fine
    print("Record not found.")
    return 0.0

# Fine logic
def calculate_fine(return_date, due_date, condition):
    if condition.lower() == "lost":
        return 50.0  # fixed penalty
    elif condition.lower() == "damaged":
        return 20.0
    elif return_date > due_date:
        days_late = (return_date - due_date).days
        return 1.0 * days_late  # 5rs per day
    return 0.0

# Waitlist logic
def add_to_waitlist(member_id, isbn):
    if isbn not in waitlists:
        waitlists[isbn] = []
    waitlists[isbn].append(member_id)

def notify_waitlist(isbn):
    if isbn in waitlists and waitlists[isbn]:
        next_member = waitlists[isbn].pop(0)
        print(f"Book {isbn} is now available. Notifying member {next_member}.")
while True:
        print("\nOptions:\n1.add_book\n2.Register Member\n3.issue Book\n4.Return Book\n5.Exit")
        choice=input("Enter your choice:")
        if choice=="1":
            isbn=input("enter ISBN")
            title=input("Enter Title:")
            author=input("Enter Author")
            genre=input("Enter Genre:")
            copies=int(input("Enter number of copies: "))
            book_type=input("enter book type (physical/ebook): ")
            add_book(isbn,title,author,genre,copies,book_type)
        elif choice=="2":
            member_id=input("Enter member ID: ")
            name=input("Enter name:")
            email=input("Enter Email:")
            contact=int(input("enter contact: "))
            membership_type=input("Enter membership type: ")
            register_member(member_id,name,{"email":email},contact,membership_type)
        elif choice=="3":
            member_id=input("Enter member ID: ")
            isbn=input("Enter ISBN: ")
            branch_id=input("Enter Branch ID: ")
            issue_book(member_id,isbn,branch_id)
        elif choice=="4":
            member_id=input("Enter member ID: ")
            isbn=input("Enter ISBN: ")
            return_date_str=input("Enter Return date (DD-MM-YYYY): ")
            condition=input("Enter Book condition(good/damaged/lost): ")
            return_book(member_id,isbn,return_date_str,condition)
        elif choice=="5":
            print("Goodbye!")
        
            break
        else:
            print("Invalid option, Try again.")


