
import csv
with open('clothing.csv ') as file:
    reader = csv.reader(file)
    header = next(reader)  # read header row
        # find indices of relevant columns (assumes header names contain these)
    for row in reader:
        if float(row[header.index("Price")]) < 60.0 and float(row[header.index("Stock_Quantity")]) < 40.0:
            print(row[header.index("Product_Name")])
