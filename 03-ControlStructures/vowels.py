###
# Counts vowels in the text
#
text = "This is a sample text."
vowels = "aeiouAEIOU"
vowel_count = 0
i = 0 
ii = 0

# Count vowels in the text
#for char in text:
    #if char in vowels:
       # vowel_count += 1

while i != 22:
    while True:
        if text[i] == vowels[ii]:
            vowel_count += 1
            i +=1
            continue
        else:
            ii+=1
    continue

    

print(f"The number of vowels in the text is: {vowel_count}")
