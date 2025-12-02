paragraph = "cat dog mouse cat rat cat mouse"

paragraph = paragraph.split()
words = set()
for i in paragraph:
    words.add(i)
for i in words:
    print(i, paragraph.count(i))