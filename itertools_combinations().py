from __future__ import print_function
from itertools import permutations
from itertools import combinations
input_1 = raw_input().split(' ')
letter_list = []
for i in input_1[0]:
     letter_list.append(i)
letter_list.sort()
for letter in letter_list:
    print (letter)
for i in range(1,int(input_1[1])):
    al_list = list(combinations(letter_list,i+1))
    al_list.sort()
    for al in al_list:
        for j in al:
            print(j,end = '')
        print()
