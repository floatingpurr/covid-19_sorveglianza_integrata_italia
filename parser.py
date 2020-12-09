from datetime import date
from openpyxl import load_workbook
import csv

data_path = 'data/latest'
today = date.today()
current_date = today.strftime('%d-%m-%Y')

wb = load_workbook(f'{data_path}/data.xlsx', read_only=True)


for sheet in wb.worksheets:
    with open(f'{data_path}/{sheet.title}.csv', 'w', newline="") as f:
        c = csv.writer(f)
        for r in sheet.rows:
            c.writerow([cell.value for cell in r])