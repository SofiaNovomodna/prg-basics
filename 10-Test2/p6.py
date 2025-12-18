def f(years, course, average_grade):
    import json
    with open('data.json', 'r') as file:
        context = json.load(file)
    
    count = 0
    for student in context:
        if student['age'] < years:
            continue
        elif student['courses'][course] < average_grade:
            continue
        count +=1

    return count



print(f(21, "statistics", 4) )