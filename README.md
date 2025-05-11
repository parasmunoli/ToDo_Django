# ToDo Django App

This is a basic Django project developed for practicing core concepts of Django web development. It implements a simple ToDo list application where users can manage their daily tasks — add, update, mark complete, and delete them.

## Purpose

This project serves as a foundational exercise to understand:
- Django models, views, and templates (MVT architecture)
- URL routing and rendering logic
- Working with Django admin and database migrations
- User interface integration with backend logic

---

## Features

- Add Tasks
- View All Tasks
- Update Task Details
- Delete Tasks
- Mark Tasks as Completed
- Simple UI integrated with Django Templates

---

## Installation & Setup

Follow these steps to run the project on your local machine:

### 1. Clone the Repository
```bash
git clone https://github.com/parasmunoli/ToDo_Django.git
cd ToDo_Django
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the Development Server
```bash
python manage.py runserver
```

### 6. Open in Browser
Visit:
```
http://127.0.0.1:8000/signup/
```

---

## Project Structure

```
ToDo_Django/
├── ToDoList/               
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── ToDo/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   └── ...
├── db.sqlite3
├── manage.py
└── README.md
```

---