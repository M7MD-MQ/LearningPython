if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    sec_run=0
    s_arr=[]
    fir_run=arr[0]
    for i in range(len(arr)-1):
            if fir_run<arr[i+1]:
                fir_run=arr[i+1]

    for i in arr:
        if i != fir_run:
            s_arr.append(i)

    sec_run=s_arr[0]
    for i in range(len(s_arr)-1):
        if sec_run<s_arr[i+1]:
            sec_run=s_arr[i+1]

    print(sec_run)
