# Digittence - Digital Attendance Management System

## Overview

Digittence is a web-based Digital Attendance Management System designed to simplify attendance tracking and academic record management for educational institutions. It enables faculty to manage classes, subjects, students, and attendance through a secure and user-friendly interface.

## Features

- Secure user authentication (Register/Login)
- Faculty dashboard
- Create and manage classes
- Add and manage subjects
- Student enrollment
- Record daily attendance
- View attendance records
- Attendance percentage calculation
- Role-based access control
- MySQL database integration
- Responsive web interface

## Tech Stack

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python
- Flask

### Database
- MySQL

### Tools
- Visual Studio Code
- Git
- GitHub

---

## Project Structure

```
Digittence/
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── classes.html
│   ├── subjects.html
│   └── attendance.html
│
├── digi.py
├── requirements.txt
├── database.sql
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Digittence.git
```

### 2. Navigate to the project

```bash
cd Digittence
```

### 3. Create a virtual environment (Optional)

```bash
python -m venv venv
```

Activate it:

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure MySQL

- Create a MySQL database.
- Import the `database.sql` file.
- Update the database credentials in `app.py`.

Example:

```python
host="localhost"
user="root"
password="your_password"
database="digittence"
```

### 6. Run the application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000/
```

---

## Database Modules

- Users
- Classes
- Subjects
- Students
- Attendance

---

## Authentication

- User Registration
- Secure Login
- Session Management
- Logout

---

## Screenshots

Add screenshots here.

Example:

- Login Page
- Dashboard
- Class Management
- Subject Management
- Attendance Page

---

## Future Enhancements

- Student login portal
- QR Code attendance
- Face Recognition attendance
- Attendance analytics
- Email notifications
- Mobile application
- Export attendance to Excel/PDF
- Admin dashboard

---

## Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

---

## License

This project is developed for educational purposes.

---

## Author

**Golla Sai Teja**

B.Tech Computer Science and Engineering

JNTUH College of Engineering Sultanpur

GitHub: https://github.com/your-username
