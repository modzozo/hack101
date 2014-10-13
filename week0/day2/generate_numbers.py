#pytho3 cat2.py file.txt file2.txt
from sys import argv
from random import randint


def write_to_file(filename,num):
        file = open(filename, "w")
        contents = randint(1,num)
        file.close()
        return contents    

def main():
    if len(argv) <= 1:
        print("Provide valid filenames")
        filename = ""
    elif isinstance(argv[0],str) and isinstance(argv[1],int):
        print("As first argument provide a filename and as second an integer")

 #       filename = argv[0]
 #       print(write_to_file(filename))

if __name__ == '__main__':
    main()
