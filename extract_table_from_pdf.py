import camelot

tables = camelot.read_pdf('table.pdf', pages='1')

print(tables)  # print all the tables found in the PDF

tables.export('table.csv', f='csv', compress=True)  # export table to a CSV
tables[0].to_csv('table.csv')