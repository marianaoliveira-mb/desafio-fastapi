
import os

from sqlalchemy import (Column, Integer, String, Boolean, DateTime, Table, create_engine, MetaData)
from dotenv import load_dotenv
from databases import Database
from datetime import datetime as dt

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:secret@localhost:5432/postgres")

engine = create_engine(DATABASE_URL)
metadata = MetaData()
notes = Table(
    "notes",
    metadata,
    Column("id", Integer, primary_key = True),
    Column("title", String(50)),
    Column("description", String(50)),
    Column("completed", Boolean, default="False"),
    Column("created_date", DateTime, default=dt.now())
)

database = Database(DATABASE_URL)
