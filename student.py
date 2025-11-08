
## 💻 **Extended Python Code (student_records.py)**
python
import mysql.connector
from mysql.connector import Error
from colorama import Fore, Style, init

# Initialize colorama for colored text
init(autoreset=True)

# ---------- Database Connection Setup ----------
def connect_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",          # 🔹 Change this
            password="password",  # 🔹 Change this
            database="student_db"
        )
        return conn
    except Error as err:
        print(Fore.RED + f"❌ Database Connection Error: {err}")
        return None

# ---------- CRUD FUNCTIONS ----------
def add_student(name, roll_no, course, marks):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO students (name, roll_no, course, marks) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (name, roll_no, course, marks))
            conn.commit()
            print(Fore.GREEN + "✅ Student added successfully!")
        except mysql.connector.IntegrityError:
            print(Fore.YELLOW + "⚠️ Roll number already exists. Try another.")
        except Error as err:
            print(Fore.RED + f"❌ Error: {err}")
        finally:
            cursor.close()
            conn.close()

def view_students():
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        results = cursor.fetchall()

        print(Fore.CYAN + "\n--- Student Records ---")
        print(Fore.MAGENTA + f"{'ID':<5}{'Name':<20}{'Roll No':<15}{'Course':<20}{'Marks':<10}")
        print("-" * 70)

        if results:
            for row in results:
                print(f"{row[0]:<5}{row[1]:<20}{row[2]:<15}{row[3]:<20}{row[4]:<10}")
        else:
            print(Fore.YELLOW + "⚠️ No records found.")
        cursor.close()
        conn.close()

def search_student(roll_no):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        query = "SELECT * FROM students WHERE roll_no = %s"
        cursor.execute(query, (roll_no,))
        result = cursor.fetchone()
        if result:
            print(Fore.CYAN + "\n--- Student Details ---")
            print(f"ID: {result[0]}")
            print(f"Name: {result[1]}")
            print(f"Roll No: {result[2]}")
            print(f"Course: {result[3]}")
            print(f"Marks: {result[4]}")
        else:
            print(Fore.YELLOW + "⚠️ Student not found!")
        cursor.close()
        conn.close()

def update_marks(roll_no, marks):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        query = "UPDATE students SET marks = %s WHERE roll_no = %s"
        cursor.execute(query, (marks, roll_no))
        conn.commit()
        if cursor.rowcount > 0:
            print(Fore.GREEN + "✅ Marks updated successfully!")
        else:
            print(Fore.YELLOW + "⚠️ Roll number not found.")
        cursor.close()
        conn.close()

def delete_student(roll_no):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        query = "DELETE FROM students WHERE roll_no = %s"
        cursor.execute(query, (roll_no,))
        conn.commit()
        if cursor.rowcount > 0:
            print(Fore.GREEN + "🗑️ Student deleted successfully!")
        else:
            print(Fore.YELLOW + "⚠️ Roll number not found.")
        cursor.close()
        conn.close()

# ---------- MENU SYSTEM ----------
def main_menu():
    while True:
        print(Fore.BLUE + "\n===== Student Records Management =====")
        print(Fore.CYAN + "1️⃣ Add Student")
        print("2️⃣ View All Students")
        print("3️⃣ Search Student by Roll No")
        print("4️⃣ Update Marks")
        print("5️⃣ Delete Student")
        print("6️⃣ Exit")

        choice = input(Fore.WHITE + "\nEnter your choice (1-6): ")

        if choice == '1':
            name = input("Enter Name: ").strip()
            roll_no = input("Enter Roll No: ").strip()
            course = input("Enter Course: ").strip()
            try:
                marks = int(input("Enter Marks: "))
                add_student(name, roll_no, course, marks)
            except ValueError:
                print(Fore.RED + "❌ Invalid marks. Please enter an integer.")

        elif choice == '2':
            view_students()

        elif choice == '3':
            roll_no = input("Enter Roll No: ").strip()
            search_student(roll_no)

        elif choice == '4':
            roll_no = input("Enter Roll No: ").strip()
            try:
                marks = int(input("Enter New Marks: "))
                update_marks(roll_no, marks)
            except ValueError:
                print(Fore.RED + "❌ Invalid marks. Please enter an integer.")

        elif choice == '5':
            roll_no = input("Enter Roll No: ").strip()
            delete_student(roll_no)

        elif choice == '6':
            print(Fore.GREEN + "👋 Exiting the program. Goodbye!")
            break
        else:
            print(Fore.RED + "⚠️ Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
