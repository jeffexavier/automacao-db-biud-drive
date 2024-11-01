
from dotenv import load_dotenv

import psycopg2
import os

load_dotenv()

def db_query(select: str = ""):
  conn = psycopg2.connect(
    database = os.environ["db_database"],
    host = os.environ["db_host"],
    port = os.environ["db_port"],
    user = os.environ["db_user"],
    password = os.environ["db_password"]
  )

  cursor = conn.cursor()
  cursor.execute(select)

  collums = [collumn.name for collumn in cursor.description]
  rows = cursor.fetchall()
  conn.close()

  return collums, rows
