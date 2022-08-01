from openpyxl import load_workbook
import csv

data_path = 'data/latest'

wb = load_workbook(f'{data_path}/data.xlsx', read_only=True)

# get the report date
date_list = wb['casi_regioni']['C2'].value.split('/')
report_date = f'{date_list[2]}-{date_list[1]}-{date_list[0]}'

# Write date to file
with open(f'{data_path}/date', 'w') as f:
    f.write(report_date)

# Write data to file
for sheet in wb.worksheets:
    # fix bad file format in read_only mode
    sheet.reset_dimensions()
    with open(f'{data_path}/{sheet.title}.csv', 'w', newline="") as f:
        c = csv.writer(f)
        for r in sheet.rows:
            c.writerow([cell.value for cell in r])