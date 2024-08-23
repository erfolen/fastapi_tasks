from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

async_engine = (
    "sqlite+aiosqlite:///database.sql"
)

new_session = async_sessionmaker(async_engine, expire_on_commit=False)


class Base(DeclarativeBase):
    ...
