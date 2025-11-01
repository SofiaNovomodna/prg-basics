
age = int (input('Enter age: '))
age_group = ''

if 0<= age <13:
    age_group = 'Child'
elif 13<= age <=19:
    age_group = 'Teen'
elif 20<= age <=64:
    age_group = 'Adult'
elif 65<= age:
    age_group = 'Senior'

print(f'Your age group: {age_group}')