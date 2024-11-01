
from db_connection import db_query
from create_csv_file import create_csv
from select_queries import select_queries

for select in select_queries():
  collumns, rows = db_query(select.query)
  create_csv(collumns, rows, select.file_name)
