grades = [3.0,5.0,2.0,3.5,4.0,4.0,3.5,2.0,4.0,2,0]

positive = list(filter(lambda grade: grade >2.0, grades))
print(round(sum(positive)/len(positive),2))