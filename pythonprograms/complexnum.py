num1 = float(input("enter num1 "))
img1 = float(input("enter img1 "))

num2 =float(input("enter num2 "))
img2 = float(input("enter img2"))

compx1 = complex(num1,img1)
compx2 = complex(num2,img2)

addition = compx1 + compx2
mult = compx1*compx2

print(f"addition of {compx1} and {compx2} is {addition}")
print(f"multiplication of {compx1} and {compx2} is {mult}")