bottles = [508,500,512,499,492,511,503,476,501,509]

correct = list(filter(lambda value: 490 <= value <= 510, bottles))
print('Bottle capacity:    500ml')
print('Filling tolerance:  2%')
print('Filled bottles:    ', *bottles)
print(f'Incorrectly filled: {100-(len(correct)/len(bottles)*100)}%')