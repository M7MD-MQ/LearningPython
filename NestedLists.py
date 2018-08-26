names = {}
grads = []
lowst_g=0
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    names[name]=score
    grads.append(score)
grads.sort()
s_lowst_g = grads[0]
for j in range(len(grads)):
    if grads[j]>s_lowst_g:
        s_lowst_g = grads[j]
        break
for key in sorted(names.iterkeys()):
    if names[key] == s_lowst_g:
        print(key)
 
