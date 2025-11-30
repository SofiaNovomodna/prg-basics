
import csv
with open('it_company.csv') as file:
    reader = csv.reader(file)
    header = next(reader)  # read header row
        # find indices of relevant columns (assumes header names contain these)
    for row in reader:
        if row[header.index("Job Title")] == "Graphic Designer":
            first = row[header.index("First Name")]
            last = row[header.index("Last Name")]
            email = row[header.index("Email")]
            print(f"{first} {last},{email}")