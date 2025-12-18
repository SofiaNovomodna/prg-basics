def f(value):
    import csv
    count =0
    with open('data.csv', 'r') as file:
        context = csv.reader(file)
        headings = next(context)
        for i in context:
            if int(i[headings.index('salary')]) >= value:
                count +=1
    return count


print(f(5000))