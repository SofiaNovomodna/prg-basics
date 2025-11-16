arr = [[-38, 19], [5,40],[-7,11],[29,16]]

min = 0
row = 0
col = 0
for rows in arr:
    for i in rows:
        if i < min:
            min = i
            min_row = row+1
            min_col = col+1
        col+=1
    row+=1
print('Min value: ', min,'Row: ',  min_row,'Col: ',  min_col)


max = 0
row = 0
col = 0
for rows in arr:
    for i in rows:
        if i > max:
            max = i
            max_row = row+1
            max_col = col+1
        col+=1
    col = 0
    row+=1
print('Max value: ', max,'Row: ',  max_row,'Col: ',  max_col)