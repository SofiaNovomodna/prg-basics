
def check(arr1, arr2):
    for i in arr1:
        if i not in arr2:
            return False
    return True

print(check([1,2,3], [1,2,3,4,5,6]))
print(check([1,2,3], [4,5,6]))