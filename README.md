# 🎓 Student Records Management System (Python & MySQL)

## 📌 Overview
This project demonstrates how to connect **Python** with **MySQL** to perform **CRUD (Create, Read, Update, Delete)** operations.  
It’s a great beginner-friendly project for anyone learning **database handling and Python scripting**.

---

## ⚙️ Features
- Add new student records  
- View all records in a clean table format  
- Search by roll number  
- Update marks easily  
- Delete records  
- Handles input errors gracefully  
- Beautiful **colored console output**  

---

## 🧰 Technologies Used
- **Python 3**
- **MySQL Server**
- **mysql-connector-python**
- **colorama** (for colorful console text)

---

## 🗂️ Database Setup
1. Open MySQL and create a database and table:
   ```sql
   CREATE DATABASE student_db;
   USE student_db;

   CREATE TABLE students (
       id INT AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(100) NOT NULL,
       roll_no VARCHAR(50) UNIQUE NOT NULL,
       course VARCHAR(100),
       marks INT
   );
