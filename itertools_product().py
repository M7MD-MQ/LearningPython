from itertools import product
list_1 = []
list_2 = []
input_1 = (raw_input())
input_2 = (raw_input())
list_1 = input_1.split(' ')
list_2 = input_2.split(' ')
for i in range(len(list_1)):
    list_1[i] = int(list_1[i])
for i in range(len(list_2)):
    list_2[i] = int(list_2[i])
A = [list_1,list_2]
mult_list = str(list(product(*A)))
mult_list = mult_list.replace('[','')
mult_list = mult_list.replace(']','')
mult_list = mult_list.replace('),',')')
print mult_list
