n = input()
s = set(map(int, raw_input().split()))
num = int(raw_input())
sum_num = 0
for i in range(num):
    comm = raw_input()
    if comm[0] == 'p':
        s.pop()
    elif comm[0] == 'd':
        s.discard(int(comm[8:]))
    elif comm[0] == 'r':
        s.remove(int(comm[7:]))
for i in range(len(s)):
    sum_num += int(s.pop())
print(sum_num)    
