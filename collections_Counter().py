from collections import Counter
total_money = 0
sh_size_list = []
cu_price = []
sh_num = int(raw_input())
sh_size_list = Counter(str(raw_input()).split(' '))
cu_num = int(raw_input())
for i in range(cu_num):
    cu_price.append(raw_input().split(' '))
for i in range(len(cu_price)):
    for key, value in sh_size_list.items():
            if cu_price[i][0] == key and value > 0:
                total_money += int(cu_price[i][1])
                sh_size_list[key] = value - 1

print(total_money)
