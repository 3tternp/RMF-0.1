# RMF-0.1

A secure, containerized Django-based Risk Register application with JWT authentication and RBAC support.

## 🔧 Features Implemented

### ✅ Step 1: Secure Django Setup
- Django 5 + Django REST Framework (DRF)
- PostgreSQL with Docker Compose
- JWT Authentication (`djangorestframework-simplejwt`)
- Custom User Model with Roles: `Admin`, `Manager`, `Auditor`, `Viewer`
- Role-Based Access Control (RBAC)

### 🗂️ Step 2: Risk Register API
- CRUD API for risk entries
- Fields: title, description, owner, severity, likelihood, impact, mitigation, etc.
- Access control: Create/Edit by Admin/Manager, View by all

### 📊 Step 3: Dashboards & Risk Heatmap
- `GET /api/core/dashboard/metrics/`: Risk counts by status, severity, owner, recency
- `GET /api/core/dashboard/heatmap/`: 5x4 matrix for likelihood × severity
- Role-based read access to dashboards

---

## 🚀 Quick Start (Local with Docker)

```bash
docker-compose up --build
