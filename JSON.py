# # JSON (JavaScript Object Notation).True
# It is mainly used for storing and transferring data between the browser and the server.True
# JSON is text, written with JavaScript object notation.True
# Python too support JSON with a built-in packege called json.True

# JSON support mainly 6 data types:
# 1.string
# 2. number
# 3. boolen
# 4. null
# 5. object
# 6. array

import json
blog={'URL':'www.wscubetech.com','name': 'Wscubetech'}
to_json=json.dumps(blog)
print(type(to_json),to_json)
# output:<class 'str'> {"URL": "www.wscubetech.com", "name": "Wscubetech"}

d={'course': 'Python', 'fees':'15000'}
c=json.dumps(d)
print(c,type(c))
# output:{"course": "Python", "fees": "15000"} <class 'str'>





import json



