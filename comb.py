x=['a','b']
y=['c','d']
z=[]
i=0
while i<len(x):
    j=0
    while j<=1:
        c=x[i]+y[j]
        z.append(c)
        j=j+1
    i=i+1
print(z)