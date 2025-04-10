from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel

# Define la URL de la base de datos (SQLite en este caso)
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# Crea el motor de la base de datos
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# Crea una sesión para interactuar con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()