if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    p=0
    ar=[]
    for i in range ( x + 1 ) :
        for j in range( y + 1):
            for k in range( z + 1):
                if k+j+i != n:
                    ar.append([])
                    ar[p] = [i , j , k]
                    p+=1
    print ar
