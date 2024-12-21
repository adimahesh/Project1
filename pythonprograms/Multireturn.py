def multreturn(numbers):
    total = sum(numbers)
    average = total/len(numbers)
    maxi = max(numbers)
    mini = min(numbers)

    return total,average,maxi,mini

data = [10,20,30,40,50]
total,average,maxi,mini=multreturn(data)
print(total)
print(average)
print(maxi)
print(mini)
