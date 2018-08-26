def swap_case(s):
    for i in range(len(s)):
        w=''
    for i in range(len(s)):
        if s[i].isupper():
            w += s[i].lower()
        elif not(s[i].isupper()):
                w += s[i].upper()
    return w

if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result
