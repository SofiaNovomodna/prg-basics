def f(number):
    number = str(number)
    result = 0
    checked = set()  # to avoid counting same digit multiple times

    for com in number:
        if com not in checked:
            count = number.count(com)
            if count > 1:
                result += int(com) * count
            checked.add(com)

    return result

if __name__ == "__main__":
    print(f(1027))
    print(f(230335))
    print(f(513553007))
