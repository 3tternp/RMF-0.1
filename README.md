# RMF-0.1

A secure, containerized Django-based Risk Register application with JWT authentication and RBAC support.

## 🚀 Features Implemented
- Django 5 with Django REST Framework
- JWT-based Authentication (`djangorestframework-simplejwt`)
- Custom User Model with Roles: Admin, Manager, Auditor, Viewer
- Role-Based Access Control
- Risk Register API (CRUD)
- Dockerized with PostgreSQL backend

## 📦 Setup Instructions

```bash
git clone https://github.com/yourusername/RMF-0.1.git
cd RMF-0.1
cp backend/.env.example backend/.env
docker-compose up --build
