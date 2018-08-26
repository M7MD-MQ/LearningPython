def wrap(string, max_width):
    s=''
    for i in range(len(string)):
        if i%max_width == 0:
            s+=string[i:i+max_width]+'\n'
    return s
