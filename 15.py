#Strategy: answer is going to be 2n choose n, n length of square, since path is 2n long and must choose n
# spots in which you go down (or right, analogous)
import math
n = 20
print(int(math.factorial(n*2)/((math.factorial(n)*math.factorial(n)))))
