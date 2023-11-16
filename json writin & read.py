import json
file=open("course.json","r")
a=file.read()
filedata=json.loads(a)
print(filedata)

for b in filedata:
     print(b)