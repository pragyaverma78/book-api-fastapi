# Mini Book API

Small beginner FastAPI project.

## Run
```bash
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000/docs` for Swagger.

## Endpoints
- GET `/`
- GET `/books`
- POST `/books`
