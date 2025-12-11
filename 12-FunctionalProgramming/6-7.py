scores = [(17,15,16,17,15),
 (16,18,19,17,19),
 (19,15,15,19,18),
 (18,17,19,15,16)]

n_scores = list(map(lambda i: sum(i)-min(i)-max(i), scores))

print(n_scores)