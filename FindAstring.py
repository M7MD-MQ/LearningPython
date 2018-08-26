def count_substring(st, s):
    flag = True
    count=0
    for i in range(len(st)):
        if s[0] == st[i] and (len(st)-i)>=len(s):
            for j in range(len(s)):
                if s[j] != st[i+j]:
                    flag = False
                    break
                else:
                    flag = True
            if flag:
                count +=1
    return count


if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()

    count = count_substring(string, sub_string)
    print count    
