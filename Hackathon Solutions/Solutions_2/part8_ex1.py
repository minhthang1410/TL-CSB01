# initialize list
scores = [78, 56, 67]
print(scores)
# get user input
print('Input new score: ', end='')
scores.append(int(input()))
print(scores)

# sort list - selection sort
for i in range(len(scores)-1):
    max_pos = i
    for j in range(i+1, len(scores)):
        if scores[j] > scores[max_pos]:
            max_pos = j
    # swap to current position
    scores[i], scores[max_pos] = scores[max_pos], scores[i]
    print("Sort:" + str(scores))

# # print list
# print('High scores:')
# for i, score in enumerate(scores):
#     print(f'{i+1}. {score}')
