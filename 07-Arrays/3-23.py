text = 'An apple a day keeps the doctor away'
arr = []
add= ''
ii=0
for i in text:
    if i==' ':
        arr.append(add)
        add = ''
    elif ii == len(text)-1:
        add += i
        arr.append(add)
        add = ''
    else:
        add += i
    ii+=1
print (arr)

print('Text: ', text)
print('Number of words: ', len(arr))
print('Words from the longest: ', end ='')

ex=[]
for ii in range(0, len(arr)-1):
    max = 0
    max_word = ''
    for i in arr:
        if i in ex:
            continue
        if len(i)> max:
            max = len(i)
            max_word = i
    print(max_word, end=' ')
    ex.append(max_word)
print()
arr.sort()
print('Words ordered alphabetically: ', arr)