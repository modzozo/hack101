# cat.py
import sys
def main():
	filename = "file.txt"
	file = open(filename, "r") # Here, "r" stands for open for reading
	content = file.read()
	print(content)
	file.close()

if __name__ == '__main__':
    main()

