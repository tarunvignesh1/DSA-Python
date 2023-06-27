# HashSet

mySet = set()

mySet.add(13)
mySet.add(17)
mySet.add(18)

print(17 in mySet)
print(20 in mySet)


# Hashmap

mymap = {}

mymap["alice"] = 88
mymap["bob"] = 77
print(mymap)

for key in mymap:
    print(key,mymap[key])

for val in mymap.values():
    print(val)

for key,val in mymap.items():
    print(key,val)

    