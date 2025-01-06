# hashmap or hash table is a datastructure that can access elements in O(1)

hashmap = {}

print(hashmap.get("key", 0))

hashmap["key"] = 3
hashmap["key2"] = 5

print(hashmap.get("key", 0))


print("hashmap.keys()")
for i in hashmap.keys():
    print(i)

print("hashmap.values()")
for i in hashmap.values():
    print(i)

print("hashmap.items()")
for i in hashmap.items():
    print(i)






