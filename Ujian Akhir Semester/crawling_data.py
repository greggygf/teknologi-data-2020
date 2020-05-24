from bs4 import BeautifulSoup # Untuk Mengambil data dari file HTML
from urllib.request import urlopen # Untuk Menghandle URL
import csv # Untuk bekerja dengan file CSV

# Menentukan link yang akan diambil datanya
html = urlopen('http://yunhasnawa.com/sdrepo-kmeans/')
bsObj = BeautifulSoup(html, 'html.parser')

# Mengambil table, menggunakan indeks ke-0 karena table yang ingin diambil datanya adalah data tabel yang pertama / indeks ke-0
table = bsObj.findAll(class_="divTable")[0]
# Mengambil data di dalam baris tabel
rows = table.findAll(class_="divTableRow")

# Untuk menentukan tempat kita menyimpan data hasil crawling dengan metode w+ untuk menulis data ke dalam file csv
csvFile = open("resource/data_nasabah_asuransi_crawling.csv", 'w+')
writer = csv.writer(csvFile)

# Cara mengambil data menggunakan perulangan
try:
    for row in rows:
        csvRow = [] # ["ID Nasabah", "Jenis Kelamin", ...],[1, Pria, 19, 225000000, 58500000], ...
        for cell in row.findAll(class_="divTableCell"):
            csvRow.append(cell.get_text()) # Mengekstrak data satu persatu di dalam divTableCell atau tag <td>

        writer.writerow(csvRow)
finally:
    csvFile.close()
