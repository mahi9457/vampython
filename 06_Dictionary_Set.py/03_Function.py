'''mydict.keys()           returns all keys
mydict.value()             returns all values
Mydict.itmes()             returns all (key,val) pairs as tuples
mydict.get("key")         returns the key according to value
mydict.update(newdict)     inserts the specified items to the dictionary  '''

info = {
    "friend" : "Preeti",
    "School" :  "G.I.C",
    "Class"  : 12
}
print(info.keys())

print(info.values())

print(info.items())

print(info.get("friend"))    # same things
print(info["friend"])        # same things

print(info.get("age"))      # that show none

try: print(info["age"])        # that show error
except:print("ERROR")