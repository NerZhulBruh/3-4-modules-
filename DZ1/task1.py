import csv
with open('data.txt', 'r') as file:
    data = [line.strip().split(': ') for line in file]
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(['name', 'grade'])
    for row in data:
        writer.writerow(row)