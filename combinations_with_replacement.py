from __future__ import print_function
from itertools import permutations
from itertools import combinations_with_replacement
#input_1 = raw_input().split(' ')
input_1 = 'HACKER 3'.split(' ')
letter_list = []
for i in input_1[0]:
     letter_list.append(i)
letter_list.sort()
al_list = list(combinations_with_replacement(letter_list,int(input_1[1])))
al_list.sort()
for al in al_list:
    for j in al:
        print(j,end = '')
    print()
