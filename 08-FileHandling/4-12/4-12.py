import csv
with open('books.csv') as file:
    reader = csv.reader(file)
    header = next(reader)  # read header row
        # find indices of relevant columns (assumes header names contain these)
    gen = []
    for row in reader:
        if row[header.index("Genre")] in gen:
            continue
        else:
            gen.append(row[header.index("Genre")])

for el in gen:
    with open('books.csv') as file:
        reader = csv.reader(file)
        header = next(reader) 
        with open (f'{el}.txt', 'w') as file:
            for row in reader:
                if str(row[header.index("Genre")]) == str(el):
                    line = f'{row[header.index("Title")]},{row[header.index("Author")]},{row[header.index("Year")]} \n'
                    file.write(line)