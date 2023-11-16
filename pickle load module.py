import pickle

file=open("pickle module.txt","rb")
l=pickle.load(file)
print(l)