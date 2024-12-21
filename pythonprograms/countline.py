def counts(inputfile):
    try:
        linecount=0
        wordcount=0
        charcount=0
        with open(inputfile,"r") as filedata:
            
            for line in filedata:
                linecount+=1
                charcount+=len(line)
                wordcount+=len(line.split())
            print("lines = ",linecount)   
            print("words = ",wordcount)   
            print("charcount = ",charcount)   
    except FileNotFoundError:
        print("file not found")

counts("C:\\Users\\adima\\OneDrive\\Desktop\\completeDSA\\pythonprograms\\sortedword.txt")