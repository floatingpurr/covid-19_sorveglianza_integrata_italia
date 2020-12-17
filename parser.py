from openpyxl import load_workbook
import csv

data_path = 'data/latest'

wb = load_workbook(f'{data_path}/data.xlsx', read_only=True)
# get report date
report_date = wb['casi_regioni']['A2'].value.replace('/','-')

# Write date to file
with open(f'{data_path}/date', 'w') as f:
    f.write(report_date)

# Write data to file
for sheet in wb.worksheets:
    with open(f'{data_path}/{sheet.title}.csv', 'w', newline="") as f:
        c = csv.writer(f)
        for r in sheet.rows:
            c.writerow([cell.value for cell in r])