import json

x = json.parse('{"name":"David", "height":1.8542, "favorite":6, "male":true, "religion":null}')

print json.stringify(x)
print json.stringify(x, None)
print json.stringify(x, None, 5)

# This gives a TypeError 'function' does not support indexing
#x = json.parse['["David"]']
