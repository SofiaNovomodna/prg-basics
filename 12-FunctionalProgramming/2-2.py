names = [
   'James',
   'Emily',
   'William',
   'Olivia',
   'Benjamin',
   'Sophia',
   'Henry']

names = sorted (names, key = lambda name: len(name))

for i in names:
    print(i)