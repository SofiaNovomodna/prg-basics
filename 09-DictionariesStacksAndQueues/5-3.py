translations = {
   'computer': 'komputer',
   'mouse': 'myszka',
   'keyboard': 'klawiatura',
   'printer': 'drukarka'
}

eng = input('Enter word in English: ')
if eng in translations.keys():
    print('In Polidsh:', translations[eng])
else:
    print ('No traslation')