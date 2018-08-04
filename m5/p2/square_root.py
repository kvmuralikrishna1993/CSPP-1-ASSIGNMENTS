'''# Write a python program to find the square root of the given number 
# using approximation method'''

def main():
	'''Program start here'''
	st_ = float(input())
	"""#your code here"""
	low_ = 0
	high_ = st_
	guess_ = (low_+high_)/2
	mimimal_ = 0.01
	while (guess_**2-st_) <= mimimal_:
		if abs(guess_**2 - st_) == 0:
			break
		if guess_**2 > st_:
			high_ = guess_
		else:low_ = guess_
	print(guess_)
if __name__== "__main__":
	main()