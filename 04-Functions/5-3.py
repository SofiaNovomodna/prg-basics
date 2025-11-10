###
# Allows to enter and print employee data. Due to personal
# data protection, you can determine whether information about
# the employee's salary will be printed
#
import mykeyboard # your own defined module

# Reads employee's data from keyboard
first_name = mykeyboard.input_string('Enter name: ')
last_name = mykeyboard.input_string('Enter last name: ')
age = mykeyboard.input_integer('Enter age: ')
salary = mykeyboard.input_real('Enter salary: ')
is_salary_hidden = mykeyboard.input_boolean('Hide salary? (y/n)')

# Prints employee's record
print('DATA RECORD')
print('===========')
print('Name:', first_name)
print('last name:', last_name)
print('age:', age)
if is_salary_hidden==True:
    print('Salary', salary)
