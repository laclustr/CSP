import csv

addresses = []
with open("21wedFeb12_csv.csv", "r") as f:
	#reader = csv.reader(f)
	#labels = next(reader)
	#for row in reader:
	#	print(row)
	reader = csv.DictReader(f)
	for row in reader:
		addresses.append(row)


with open("21wedFeb12_csv_new.csv", "w") as f:
	writer = csv.DictWriter(f, addresses[0].keys())

	writer.writeheader()

	for g in addresses:
		writer.writerow(g)
