# If you have a JSON string, you can parse it by using the json.loads()
# if method:
#     import json
#     #some JSON:
#     x='{'course': 'Python', 'fees':'15000','duration': '2 month'}'
#     #parse x:
#     y=json.loads(x)
#     # the result is a Python dictionary:
#     #output: {'course': 'Python', 'fees':'15000','duration': '2 month'}
#
import json

f='{"course":"Python","fees":15000,"duration":"2 month"}'
a=json.loads(f)
print(type(a))
print(a)

for b in a:
    print(b,a[b])