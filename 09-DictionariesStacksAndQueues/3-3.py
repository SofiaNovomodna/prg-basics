import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct

def brackets_ok(expression):
    result = True
    brackets = queue.LifoQueue()
    for i in expression:
        if i in ['[' , '{' , '(']:
            brackets.put(i)
        elif i in [']' , '}' , ')']:
            if brackets.empty():
                return False
            compare = brackets.get()
            if i == ']' and compare != '[':
                return False
            elif i == '}' and compare != '{':
                return False
            elif i == ')' and compare != '(':
                return False
    if not brackets.empty():
        return False
    return result #True if brackets in expression are ok of False otherwise

if brackets_ok(expression1) == True:
   print('ok')
else:
   print('no')

if brackets_ok(expression2) == True:
   print('ok')
else:
   print('no')

if brackets_ok(expression3) == True:
   print('ok')
else:
   print('no')