def print_rangoli(size):
    # your code goes here
    alp = ''
    to_print = []
    coun = 2
    for i in range(size):
        tmp = alp[:(len(alp)/2)+1]
        tmp = tmp[::-1]
        if i == 0:
            alp = alp[:(len(alp)/2)+1]+(chr(ord('a')+size-i-1))+tmp
        else:
            alp = alp[:(len(alp)/2)+1]+'-'+(chr(ord('a')+size-i-1))+'-'+tmp

        to_print.append('-'*(size*2-coun)+alp+'-'*(size*2-coun))
        print(to_print[i])
        coun += 2
    for i in range(1,len(to_print)):
        print(to_print[len(to_print)-i-1])
print_rangoli(30)
