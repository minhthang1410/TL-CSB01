# initialize lists
names = ['BĐ', 'BTL', 'CG', 'ĐĐ', 'HBT']
pops = [247100, 333300, 266800, 420900, 318000]

# find indices of min & max population
# min_pos = 0  # initialize the first element to be min & max
# max_pos = 0
# for i, el in enumerate(pops[1:]):  # loop over population list
#   if el < pops[min_pos]:  # if found element smaller than min => update min
#     min_pos = i
#   if el > pops[max_pos]:  # if found element larger than max => update max
#     max_pos = i

max_pos = 0
min_pos = 0
for i in range(len(pops)):
    if pops[i] > pops[max_pos]:
        max_pos = i
    if pops[i] < pops[min_pos]:
        min_pos = i

# print result
print('Indices of:')
print('- Most populated dist.:', names[max_pos])
print('- Least populated dist.:', names[min_pos])
