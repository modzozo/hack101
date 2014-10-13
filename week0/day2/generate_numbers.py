#pytho3 cat2.py file.txt file2.txt
from sys import argv
from random import randint

def main():
    if len(argv) < 3:
        print("Provide valid filename and number")
        
    filename=argv[1]
    number = 0 
    number=int(argv[2])
    file=open(filename,"w")
    for i in range(number):
        random_number=randint(0,1000)
        file.write(str(random_number))
        file.write(" ")
    file.write("\n")
    file.close()
        

 #       filename = argv[0]
 #       print(write_to_file(filename))

if __name__ == '__main__':
    main()
