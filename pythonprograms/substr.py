def strsort(substr,str):
    for i in range(len(str)-len(substr)+1):
        if str[i:i+len(substr)]==substr:
            return True
        
    else:
     return False
    
string = "Hello world"
substr = "Hello"

if strsort(substr,string):
  print(f"{substr} exist in string")
else:
    print("invalid")