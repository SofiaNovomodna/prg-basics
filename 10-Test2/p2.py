def find_unique(arr):
    for x in arr:
        if arr.count(x) == 1:
            return x

print(find_unique(['7', '7', '5']))       # '5'
print(find_unique(['3', '3', '3', '9']))  # '9'