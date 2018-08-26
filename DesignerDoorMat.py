# Enter your code here. Read input from STDIN. Print output to STDOUT
input_1 = (raw_input())
numb = input_1.split(' ')
N = int(numb[0])
M = N*3
d1='.|..|.'
d2='.|.'
d3='WELCOME'
coun=1
for i in range(N):
    if i < N/2:
        if i !=0:
            d2 += d1
            coun+=1
        print d2.center(M,'-')

    if i == N/2:
        print d3.center(M,'-')
        coun = (coun*2)-1
    if i > N/2:
        print ('.|.'*coun).center(M,'-')
        coun -= 2
