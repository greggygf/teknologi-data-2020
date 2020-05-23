from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

# Menentukan link yang akan diambil datanya
html = urlopen('http://yunhasnawa.com/sdrepo-kmeans/')
bsObj = BeautifulSoup(html, 'html.parser')

# Mengambil data table
table = bsObj.findAll(class_="divTable")[0]
rows = table.findAll(class_="divTableRow")

csvFile = open("resource/hasil_nyolong.csv", 'w+')
writer = csv.writer(csvFile)

try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(class_="divTableCell"):
            csvRow.append(cell.get_text())
            writer.writerow(csvRow)
finally:
    csvFile.close()
