# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Calculates expenses
# Use loop statements
Food = 0
for Week in monthly_expenses:
    Food += Week[0]
Transport = 0
for Week in monthly_expenses:
    Transport += Week[1]
Utilities = 0
for Week in monthly_expenses:
    Utilities += Week[2]

Week1=0
for item in monthly_expenses[0]:
    Week1 += item
Week2=0
for item in monthly_expenses[1]:
    Week2 += item
Week3=0
for item in monthly_expenses[2]:
    Week3 += item
Week4=0
for item in monthly_expenses[3]:
    Week4 += item

TOTAL = 0
for Week in monthly_expenses:
    for item in Week:
        TOTAL += item
# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:',Food)
print('Transport:',Transport)
print('Utilities:',Utilities)
print('Week 1:',Week1)
print('Week 2:',Week2)
print('Week 3:',Week3)
print('Week 4:',Week4)
print('---------------')
print('TOTAL:',TOTAL)