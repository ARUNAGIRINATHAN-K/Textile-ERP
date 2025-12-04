<p align="center">
  <img src="https://img.icons8.com/color/96/fabric-roll.png" alt="Textile ERP Logo" width="80"/>
</p>

<h1 align="center">🏭 Textile ERP</h1>

<p align="center">
  <strong>Enterprise Resource Planning for Textile Manufacturing</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/FastAPI-0.104-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI"/>
  <img src="https://img.shields.io/badge/SQLite-Local-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite"/>
  <img src="https://img.shields.io/badge/PostgreSQL-14+-336791?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white" alt="HTML5"/>
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white" alt="CSS3"/>
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black" alt="JavaScript"/>
  <img src="https://img.shields.io/badge/Chart.js-FF6384?style=flat-square&logo=chartdotjs&logoColor=white" alt="Chart.js"/>
  <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker"/>
  <img src="https://img.shields.io/badge/Nginx-009639?style=flat-square&logo=nginx&logoColor=white" alt="Nginx"/>
</p>

<p align="center">
  <a href="#-features">Features</a> •
  <a href="#-quick-start">Quick Start</a> •
  <a href="#️-tech-stack">Tech Stack</a> •
  <a href="#-api-endpoints">API</a> •
  <a href="#-license">License</a>
</p>

---

## ✨ Features

| Module | Description |
|--------|-------------|
| 🔐 **Authentication** | JWT-based login with role-based access control |
| 📦 **Procurement** | Supplier management, purchase orders, delivery tracking |
| 🏬 **Inventory** | Stock levels, movements, reorder alerts |
| ⚙️ **Production** | Work orders, machine allocation, production logs |
| ✅ **Quality Control** | QC inspections, defect tracking, batch approvals |
| 💼 **Sales** | Customer management, sales orders, dispatch notes |
| 📊 **Reports** | Dashboard KPIs, analytics, trend charts |

---

## 🚀 Quick Start

### Option 1: Docker (Recommended)

```bash
docker-compose up -d
```

### Option 2: Manual Setup

```bash
# Backend
cd backend
pip install -r requirements-local.txt
python create_db.py
python scripts/seed_data.py
python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload

# Frontend (new terminal)
cd frontend
python -m http.server 80
```

### 🌐 Access

| Service | URL |
|---------|-----|
| Web App | http://localhost |
| API Docs | http://localhost:8000/docs |

### 🔑 Default Credentials

| Role | Username | Password |
|------|----------|----------|
| Admin | `admin` | `admin123` |
| Manager | `manager1` | `manager123` |
| Operator | `operator1` | `operator123` |

---

## 🛠️ Tech Stack

<table>
<tr>
<td align="center" width="150"><b>Backend</b></td>
<td align="center" width="150"><b>Frontend</b></td>
<td align="center" width="150"><b>Database</b></td>
<td align="center" width="150"><b>DevOps</b></td>
</tr>
<tr>
<td align="center">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="40"/><br/>Python<br/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/fastapi/fastapi-original.svg" width="40"/><br/>FastAPI
</td>
<td align="center">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" width="40"/><br/>HTML5<br/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" width="40"/><br/>JavaScript
</td>
<td align="center">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg" width="40"/><br/>PostgreSQL<br/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlite/sqlite-original.svg" width="40"/><br/>SQLite
</td>
<td align="center">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" width="40"/><br/>Docker<br/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nginx/nginx-original.svg" width="40"/><br/>Nginx
</td>
</tr>
</table>

---

## 📁 Project Structure

```
Textile-ERP/
├── backend/
│   ├── app/
│   │   ├── api/routes/      # API endpoints
│   │   ├── core/            # Config, DB, security
│   │   └── models/          # SQLAlchemy models
│   ├── scripts/             # Seed data
│   └── main.py              # FastAPI app
├── frontend/
│   ├── index.html           # Landing page
│   ├── dashboard.html       # Main dashboard
│   ├── inventory/           # Inventory pages
│   ├── procurement/         # Procurement pages
│   ├── production/          # Production pages
│   ├── quality/             # QC pages
│   ├── sales/               # Sales pages
│   └── reports/             # Report pages
├── docker-compose.yml
└── nginx.conf
```

---

## 📡 API Endpoints

| Module | Endpoints | Description |
|--------|-----------|-------------|
| `/api/auth` | 4 | Login, register, profile |
| `/api/procurement` | 10 | Suppliers, POs |
| `/api/inventory` | 11 | Materials, stock |
| `/api/production` | 12 | Work orders, logs |
| `/api/quality` | 10 | Inspections, defects |
| `/api/sales` | 11 | Customers, orders |
| `/api/reports` | 9 | Analytics, KPIs |

> 📖 Full API documentation at **http://localhost:8000/docs**

---

<p align="center">
  <sub>Built with ❤️ for the textile industry</sub>
</p>
