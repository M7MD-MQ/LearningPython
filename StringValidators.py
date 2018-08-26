if __name__ == '__main__':
    s = raw_input()

    check_list = [False,False,False,False,False]
for i in s:
        if i.isalnum():
            check_list[0]=True
        if i.isalpha():
            check_list[1]=True
        if i.isdigit():
            check_list[2]=True
        if i.islower():
            check_list[3]=True
        if i.isupper():
            check_list[4]=True

for c in check_list:
    print(c)

    
