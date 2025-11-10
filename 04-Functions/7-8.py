def f(amount_to_pay):
    result = amount_to_pay//5 + (amount_to_pay%5)//2 + (amount_to_pay%5)%2
    return result

print(f(23))
print(f(8))
print(f(2))
print(f(0))