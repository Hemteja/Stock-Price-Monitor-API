import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL environment variable is not set. Check your .env file.")

# echo=True prints all SQL queries — helpful during development
engine = create_async_engine(DATABASE_URL, echo=True)

# expire_on_commit=False → keeps data accessible after commit
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# All models (tables) will inherit from this
Base = declarative_base()

# Ensures proper open/close per request
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

