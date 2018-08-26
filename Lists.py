if __name__ == '__main__':
    N = int(raw_input())
    lst = []
    for i in range(N):
        u_input = raw_input()
        if 'insert'  in u_input:
            lst.insert(int(u_input[7]),int(u_input[9:]))
        elif 'print' in u_input:
            print(lst)
        elif 'remove' in u_input:
            lst.remove(int(u_input[7:]))
        elif 'append' in u_input:
            lst.append(int(u_input[7:]))
        elif 'sort' in u_input:
            lst.sort()
        elif 'pop' in u_input:
            lst.pop()
        elif 'reverse' in u_input:
            lst.reverse()
