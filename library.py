from datetime import datetime, timedelta

class Library:
    def __init__(self):
        # Book database (dictionary)
        self.books = {
            101: {"title": "Python Basics", "available": True},
            102: {"title": "Data Structures", "available": True},
            103: {"title": "Operating Systems", "available": True},
            104: {"title": "Computer Networks", "available": True},
        }

        # Issued books record
        self.issued_books = {}

    # -----------------------------
    def display_books(self):
        print("\n📚 Available Books:")
        print("-" * 40)
        for book_id, info in self.books.items():
            status = "Available" if info["available"] else "Issued"
            print(f"ID: {book_id} | {info['title']} | {status}")
        print("-" * 40)

    # -----------------------------
    def issue_book(self):
        self.display_books()
        try:
            book_id = int(input("\nEnter Book ID to issue: "))
            
            if book_id not in self.books:
                print("❌ Invalid Book ID!")
                return

            if not self.books[book_id]["available"]:
                print("❌ Book already issued!")
                return

            student = input("Enter Student Name: ")
            duration = int(input("Enter duration (in days): "))

            issue_date = datetime.now()
            return_date = issue_date + timedelta(days=duration)

            # Store issued record
            self.issued_books[book_id] = {
                "student": student,
                "issue_date": issue_date,
                "return_date": return_date
            }

            self.books[book_id]["available"] = False

            print("\n✅ Book Issued Successfully!")
            print(f"📅 Return by: {return_date.strftime('%d-%m-%Y')}")

        except ValueError:
            print("❌ Invalid input!")

    # -----------------------------
    def return_book(self):
        try:
            book_id = int(input("\nEnter Book ID to return: "))

            if book_id not in self.issued_books:
                print("❌ This book was not issued!")
                return

            record = self.issued_books[book_id]
            today = datetime.now()
            due_date = record["return_date"]

            fine = self.calculate_fine(today, due_date)

            print("\n📖 Book Returned!")
            print(f"👤 Student: {record['student']}")
            print(f"📅 Due Date: {due_date.strftime('%d-%m-%Y')}")

            if fine > 0:
                print(f"💰 Late Fine: ₹{fine}")
            else:
                print("✅ No Fine!")

            # Reset book
            self.books[book_id]["available"] = True
            del self.issued_books[book_id]

        except ValueError:
            print("❌ Invalid input!")

    # -----------------------------
    def calculate_fine(self, today, due_date):
        if today <= due_date:
            return 0

        late_days = (today - due_date).days
        weeks = late_days // 7 + 1

        fine = 0
        for i in range(weeks):
            fine += (i + 1) * 10  # Progressive fine: 10, 20, 30...

        return fine

    # -----------------------------
    def view_issued_books(self):
        print("\n📋 Issued Books:")
        print("-" * 40)

        if not self.issued_books:
            print("No books issued.")
            return

        for book_id, record in self.issued_books.items():
            print(f"ID: {book_id}")
            print(f"📖 Title: {self.books[book_id]['title']}")
            print(f"👤 Student: {record['student']}")
            print(f"📅 Due: {record['return_date'].strftime('%d-%m-%Y')}")
            print("-" * 40)


# =====================================
# MAIN MENU SYSTEM
# =====================================

def main():
    lib = Library()

    while True:
        print("\n====== 📚 LIBRARY MENU ======")
        print("1. Display Books")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View Issued Books")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            lib.display_books()
        elif choice == "2":
            lib.issue_book()
        elif choice == "3":
            lib.return_book()
        elif choice == "4":
            lib.view_issued_books()
        elif choice == "5":
            print("👋 Exiting... Thank you!")
            break
        else:
            print("❌ Invalid choice!")


# Run program
if __name__ == "__main__":
    main()