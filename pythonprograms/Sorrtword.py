def sortwords(inputfile,outputfile):
 try:
     with open(inputfile,"r") as filedata:
        words = filedata.read().split()
        lowercase=[word.lower() for word in words]
        sortedwords=sorted(lowercase)
     with open(outputfile,"w") as fileout:
        for words in sortedwords:
           fileout.write(words+"\n")
        print(f"sorted words {outputfile}")

 except FileNotFoundError:
    print("file not found")

inputfile="C:\\Users\\adima\\OneDrive\\Desktop\\completeDSA\\pythonprograms\\words.txt"
outputfile="C:\\Users\\adima\\OneDrive\\Desktop\\completeDSA\\pythonprograms\\sortedword.txt"

sortwords(inputfile,outputfile)