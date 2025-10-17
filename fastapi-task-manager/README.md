# 🚀 Task Manager REST API

REST API with FastAPI and JWT authentication.

## Features
- JWT authentication
- CRUD operations
- Swagger documentation
- Task statistics

## Usage
```bash
pip install -r requirements.txt
python main.py
```

Visit: http://localhost:8000/docs

## Technologies
FastAPI • JWT • Pydantic • Uvicorn
```

---

### 📄 **FICHIER 7/11 : fastapi-task-manager/requirements.txt**
```
fastapi==0.109.0
uvicorn[standard]==0.27.0
pydantic[email]==2.5.3
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
