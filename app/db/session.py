from sqlalchemy import create_engine

from ..config import Config

database_url = Config.sql

engine = create_engine(database_url,echo=True)
