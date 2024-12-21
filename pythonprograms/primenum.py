lower = int(input("enter the lower bound"))
high = int(input("enter the upper bound"))

for num in range(lower,high):
    if num>1:
        for i in range(2,int(num/2)+1):
            if(num%i==0):
                break
        else:
         print(num)