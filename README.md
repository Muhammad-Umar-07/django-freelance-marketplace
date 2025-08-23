# 🛠️ Django Freelance Marketplace  

![Django](https://img.shields.io/badge/Django-5.0.7-green)  
![Python](https://img.shields.io/badge/Python-3.x-blue)  
![License](https://img.shields.io/badge/License-MIT-lightgrey)  

---

## 📖 Project Overview  

**A full-featured freelance marketplace web application built with Django 5.0.**  

This project is designed as a **two-sided platform** where clients and freelancers can interact in a structured and role-based way.  

- **Clients** can create and publish jobs, manage proposals submitted by freelancers, update the status of their projects, and track progress through a dedicated dashboard.  
- **Freelancers** can register, build detailed profiles with skills, experience, and portfolio links, apply to jobs with personalized proposals, and monitor their applications.  

The platform includes:  

✔ **Secure authentication**  
✔ **Role-aware profiles** (client/freelancer)  
✔ **Job posting & management** with status updates  
✔ **Proposals with bid amounts & cover letters**  
✔ **Dashboards** for both clients and freelancers  
✔ **Global search** across jobs and freelancer profiles  

Styled with **Bootstrap-ready templates** and **crispy-forms**, the UI is clean, responsive, and ready to extend. SQLite is used by default for simplicity, but the database can easily be switched to PostgreSQL/MySQL in production. **Django Admin** is fully enabled for managing users, jobs, proposals, and profiles.  

This project is perfect as a **foundation for building a professional freelance marketplace, job board, or multi-role platform**. It demonstrates real-world Django concepts including:  

- Role-based permissions  
- One-to-one and foreign key relationships  
- Pagination and global search  
- Modular app design (accounts, jobs, proposals, reviews)  

Whether you’re learning Django, prototyping, or planning to extend into a production-ready service, this project provides a **solid and practical starting point**.  

---

## 🚀 Features  

- 🔑 Authentication (Signup, Login, Logout)  
- 👤 Role-based Profiles (Client / Freelancer)  
- 📄 Jobs Management (create, list, detail, delete, update status)  
- 💼 Proposals System (apply, withdraw, bid amounts)  
- 📊 Role-aware Dashboards  
- 🔍 Global Search (jobs + freelancers)  
- 🖥️ Django Admin Panel  
- 🎨 Bootstrap + Crispy Forms UI  

---

## 🧩 Tech Stack  

- **Backend:** Django 5.0, Python 3.x  
- **Database:** SQLite (default), PostgreSQL/MySQL supported  
- **Frontend:** Bootstrap 5 + crispy-bootstrap5  
- **Other:** Django Admin, role-based permissions  

---

## ⚙️ Setup & Installation  

```bash
# Clone the repo
git clone https://github.com/yourusername/django-freelance-marketplace.git
cd django-freelance-marketplace

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate   # on Windows
source .venv/bin/activate # on Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser

# Start server
python manage.py runserver
