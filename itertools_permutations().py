# Enter your code here. Read input from STDIN. Print output to STDOUT
from __future__ import print_function
from itertools import permutations
from itertools import combinations
#input_1 = raw_input().split(' ')
input_1 = 'HACK 2'.split(' ')
letter_list = []
al_list = list(permutations(input_1[0],int(input_1[1])))
al_list.sort()
for al in al_list:
    for j in al:
        print(j,end = '')
    print() 
