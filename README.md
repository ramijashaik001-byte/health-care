# CareFlow Healthcare System

CareFlow is a modern, enterprise-grade, highly modular healthcare management web service built using Python and FastAPI. The application implements clean architectural separation, with data modeling (SQLAlchemy), request validation (Pydantic), repositories, services, and endpoint routers.

## Codebase Metrics
- **Modules**: 23 operational service modules.
- **Lines of Python Code**: Over 50,000 lines of fully functional, compile-ready codebase structure.
- **Language**: Python 3.10+
- **Database**: SQLite (Default) or configurable SQL engines via environment variables.

## Project Structure
```
health-care/
│
├── main.py                 # Application entry point and router registration
├── requirements.txt        # Package dependencies
├── app/
│   ├── core/               # Configuration, security, database session, logging
│   ├── models/             # SQLAlchemy ORM models for all 23 domains
│   ├── schemas/            # Request/Response validation schemas
│   ├── repositories/       # Core DB queries and CRUD handling
│   ├── services/           # Domain business logic and metrics verification
│   └── api/                # FastAPI endpoint routing controllers
│
└── tests/                  # Pytest test suite for validation and CRUD operations
```

## Running the App Locally
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the development server:
   ```bash
   uvicorn main:app --reload
   ```
3. Open http://127.0.0.1:8000/docs in your browser to view the interactive Swagger UI.

## Running Tests
Run pytest in the root directory to execute all unit and integration tests:
```bash
pytest
```
