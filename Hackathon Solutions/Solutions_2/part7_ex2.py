# initialize list
scores = [78, 56, 67]


# print list
print('High scores:')
# for i, score in enumerate(scores):
#   print(f'{i+1}. {score}')
for i in range(len(scores)):
    print(f"{i + 1}. {scores[i]}")
