categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]

max_expenses = max(expenses)
count =0 
for i in expenses:
    if max_expenses == i:
        break
    count +=1

print('max expenses are in category', categories[count])