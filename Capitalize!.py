def solve(s):
    f_name=''
    for i in range(len(s)):
        if i == 0 :
            f_name=s[0].upper()
        elif s[i].isalpha() and i != 0 and s[i-1]==' ' :
            f_name+=s[i].upper()
        else:
            f_name+=s[i]

    return f_name
