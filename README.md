# 🎓 College Department Management System

A Flask + MySQL–based web application designed to efficiently manage departmental, faculty, and student data through structured database operations and backend automation.  

---

## 📘 Overview

The **College Department Management System** streamlines core academic operations by automating administrative tasks such as managing departments, faculty, students, attendance, complaints, and fee structures.  
It focuses on **structured data handling and relational database design**, providing a clear and efficient backend for educational institutions.

---

## Key Features

### Admin
- Add, edit, or delete departments  
- View all faculty and students by department  
- Manage fee structures and scholarships  
- Review complaints, feedback, and leave requests  

### Department
- Manage faculty and student details  
- Assign subjects and maintain attendance records  
- Enter and update student results  
- Approve or reject faculty/student leave requests  

### Faculty
- Apply for leave  
- View assigned subjects  
- Submit complaints  

### Student
- Apply for leave and scholarships  
- Send complaints and feedback  
- View attendance, results, faculty list, and fee details  

---

## 🧰 Tech Stack

| Layer | Technology |
|-------|-------------|
| **Frontend** | HTML, CSS, Bootstrap |
| **Backend** | Python (Flask Framework) |
| **Database** | MySQL |
| **IDE/Tools** | VS Code, MySQL Workbench, GitHub Desktop |

---

## 🗂️ Database Design

The system uses a **relational database** built on MySQL.  
Major tables include:

- `login` – Stores user credentials and roles  
- `department` – Department records and contact info  
- `faculty` – Faculty details, linked to departments  
- `student` – Student details and department mapping  
- `attendance` – Student attendance records  
- `complaint` – Complaints and admin replies  
- `leave` – Leave applications and approval status  
- `result` – Student performance data  
- `fee` – Department fee information  
- `scholarship` – Scholarship records  

All tables are linked through **foreign key relationships** ensuring data consistency and integrity.
