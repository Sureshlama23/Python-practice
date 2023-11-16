   # Function for Delete Element from list
 # del
 # pop()
 # remove()
 # clear

 #1 del
l=[10,20,30,40,50,60]
del l[2]
print(l) #[10, 20, 40, 50, 60]

del l[0]
print(l) #[20, 40, 50, 60]
print(" ")
  #2 pop()
a=[10,20,30,40,50,60]
a.pop(2)
print(a) #[10, 20, 40, 50, 60]

a.clear()
print(a)


# Update function elements from list

# insert
# append
# extends

l=[10,20,30,50]
l[1]=25
print(l)
   # [10, 25, 30, 50]

l=[10,20,30,40]
l.insert(-1,60)
print(l)

l.insert(0,5)
print(l)

# append()
a=[10,30,40,50]
a.append(60)
print(a)
b=[10,"Hello",70]
a.append(b)
print(a)

# extends
w=[10,20,40]
v=[60,70]
w.extend(v)
print(w)
# [10, 20, 40, 60, 70]
