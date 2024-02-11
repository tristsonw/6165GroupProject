import glob
import csv
from dateutil import parser

path = r'Data/*.csv'
files = glob.glob(path)

zones = [f.replace('.csv', '').replace('Data/', '') for f in files]

with open('processed.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['year', 'quarter', 'month', 'day_of_year', 'loss'])
    for f in files:
        with open(f) as data_csv:
            csv_reader = csv.reader(data_csv)
            for row in csv_reader:
                date_str = row[0]
                location = row[1]
                energy = row[2]
                congestion = row[3]
                loss = row[4]