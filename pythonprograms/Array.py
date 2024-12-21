arr = []

arr.append(10)
arr.append(20)
arr.append(30)
arr.append(40)
print(arr)

index = 2
item = 15

if 0<= index <=len(arr):
 arr.insert(index,item)
else:
  print("cant insert")
print(arr) 

arr.reverse()
print(arr)