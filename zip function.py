# iterate over 2+ lists at the same time(zip function)

l=[10,20,40,50]
l1=[20,50,30,70]

for a,b in zip(l,l1):
    print(a,b)

# second method

l=[10,20,40,50]
l1=[20,50,30,70,]
t=len(l)

for h in range(t):
    print(l[h],l1[h])
