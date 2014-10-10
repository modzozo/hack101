#The function should return true if there is an equal number of x's and o's in str. It should return false otherwise.You don't have to check for valid input
request = raw_input(" Please enter only a string of x's and o's: ")

def ExOh(str):
    count_x = request.count("x")
    count_o = request.count("o")
    if count_x == count_o:
	return True
    else:
	return False

print ExOh(request)
