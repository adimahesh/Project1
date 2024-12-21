

def revlines(filename):
    try:
        with open(filename,"r") as filedata:
            lines = filedata.readlines()

            for line in reversed(lines):
                print(line.strip())


    except FileNotFoundError:
        print("file not found")

revlines("C:\\Users\\adima\\OneDrive\\Desktop\\completeDSA\\pythonprograms\\exp.txt")