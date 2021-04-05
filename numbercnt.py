a={'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}
b={}
for i in a.keys():
    for j in a.values():
        c=0
        if a[j]==a[i]:
            c=c+1 
        else:
            b=a
print(b)