# How to Run Textile ERP Application

## Prerequisites
- Python 3.7 or higher
- Pip package manager

## Setup Instructions

### 1. Install Dependencies
Navigate to the backend directory and install the required packages:
```bash
cd backend
pip install -r requirements-local.txt
```

### 2. Create Database
Create the SQLite database with all required tables:
```bash
python create_db.py
```

### 3. Seed Initial Data
Populate the database with sample data:
```bash
python scripts/seed_data.py
```

### 4. Start Backend Server
Run the FastAPI backend server:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### 5. Start Frontend Server
In a new terminal, navigate to the frontend directory and start the HTTP server:
```bash
cd frontend
python -m http.server 80
```

## Access the Application

### Web Interface
Open your browser and go to:
- **Login Page**: http://localhost
- **API Documentation**: http://localhost:8000/docs

### Default Login Credentials
- **Administrator**: admin / admin123
- **Manager**: manager1 / manager123
- **Operator**: operator1 / operator123

## Troubleshooting

### Port Conflicts
If port 80 or 8000 is already in use, you can change them:
- For frontend: `python -m http.server [PORT_NUMBER]`
- For backend: `uvicorn main:app --host 0.0.0.0 --port [PORT_NUMBER] --reload`

### Database Issues
To reset the database:
1. Delete the `test.db` file in the backend directory
2. Run `python create_db.py` again
3. Run `python scripts/seed_data.py` again

## API Endpoints
The backend API is available at `http://localhost:8000/api/` with the following modules:
- Authentication: `/api/auth/`
- Procurement: `/api/procurement/`
- Inventory: `/api/inventory/`
- Production: `/api/production/`
- Quality: `/api/quality/`
- Sales: `/api/sales/`
- Reports: `/api/reports/`

For detailed API documentation, visit http://localhost:8000/docs