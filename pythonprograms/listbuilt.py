fruits = ["apple", "banana", "cherry", "date", "elderberry","apple"] 
print("Length of the list:", len(fruits)) 
print("Maximum value:", max(fruits)) 
print("Minimum value:", min(fruits))
print("sorted list: ", sorted(fruits))
numbers  = [10,20,30,40,50]
print("sum is :", sum(numbers))

print(sorted(numbers))

count = fruits.count("apple")
print(count)
index = fruits.index("date")
print(index)
fruits.reverse()
print("reverse :", fruits)

fruits.append("zone")
print(fruits)
fruits.remove("zone")
print(fruits)