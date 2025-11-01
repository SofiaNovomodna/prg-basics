
print ('SURVEY')
science = input('Are you interested in computer science? (y/n): ')
games = input('Do you like playing computer games? (y/n): ')
account = input('Do you have an Instagram account? (y/n):')

print ('SURVEY RESULTS')
if science == 'y':
    print ('Interested in computer science: Yes')
elif science == 'n':
    print ('Interested in computer science: No')
else:
    print('incorrect')

if games == 'y':
    print ('Playing computer games: Yes')
elif games == 'n':
    print ('Playing computer games: No')
else:
    print('incorrect')

if account == 'y':
    print ('Has an Instagram account: Yes')
elif account == 'n':
    print ('Has an Instagram account: No')
else:
    print('incorrect')