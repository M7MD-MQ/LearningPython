m_num = int(raw_input())
m_set  = set(map(int, raw_input().split(' ')))
n_num = int(raw_input())
n_set = set(map(int, raw_input().split(' ')))
def_l = list(m_set.difference(n_set))+list(n_set.difference(m_set))
def_l.sort()

for i in range(len(def_l)):
    print(def_l[i])
