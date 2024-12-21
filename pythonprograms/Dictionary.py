
def key_chech(dictionary,key):
    return key in dictionary

mydict = {
    "cherry":1,
    "apple":2,
    "banana":3
}

print(key_chech(mydict,"apple"))
mykey = "Tomato"
if key_chech(mydict,mykey):
    print(f"key {mykey} exist")
else:
   print(f"{mykey} Doesn't exist") 