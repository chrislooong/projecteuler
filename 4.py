# Strategy: iterate through all combinations of 3 digit numbers and store largest num that is a palindrome
largest_palindrome = -1
for i in range(100,1000):
	for j in range(i,1000):
		num = i*j
		# Is ;argest palindrome
		if str(num)[::-1] == str(num) and num > largest_palindrome:
			largest_palindrome = num
print(largest_palindrome)
