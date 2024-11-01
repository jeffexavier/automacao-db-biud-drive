
from datetime import datetime

import os
import csv

def create_csv(collumns: list, rows: list, file_name: str):
  today = datetime.today().strftime('%d-%m-%Y')
  base_path = r'H:\\Meu Drive\\GESTÃO\\Produto\\HubSpot\\Extrações\\'
  folder_path = os.path.join(base_path, today)

  if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    print(f"Pasta criada: {folder_path}")
  else:
    print(f"A pasta já existe: {folder_path}")

  csv_file_path = os.path.join(folder_path, file_name)

  with open(csv_file_path, mode='w', newline='', encoding='utf-8',) as file:
    writer = csv.writer(file, delimiter=";")

    writer.writerow(collumns)
    writer.writerows(rows)

  print(f'Arquivo CSV criado/atualizado com sucesso em {csv_file_path}')
