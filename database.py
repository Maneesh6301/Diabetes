from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,DeclarativeBase

DATABASE_URL="mysql+pymysql://root:123@localhost:3306/Diabetes_db"

engine=create_engine(DATABASE_URL,pool_pre_ping=True)

SessionLocal=sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

class Base(DeclarativeBase):
    pass

def get_db():
    db=SessionLocal()
    try:
        yield db
    except:
        db.close()
