import pickle

l=[10,20,40,50]

file=open("pickle module.txt","wb")
pickle.dump(l,file)
file.close()
