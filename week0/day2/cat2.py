#pytho3 cat2.py file.txt file2.txt
from sys import argv

def cat(filename):
    try:
        file = open(filename, "r")
        contents = file.read()  
        file.close()
        return contents    
        
    except IOError:
        return False
        return contents.rstrip()
def main():
    if len(argv) <= 1:
        print("Provide valid filenames")
        filename = ""
    for i in range(1, len(argv)):
        filename = argv[i]
        print(cat(filename))

if __name__ == '__main__':
    main()
