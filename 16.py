# Strategy: to get around the fact that ints cannot be 300 digits long,
# use an array to store the number were doubling and sum its digits in the end

a = [1]
# double a 1000 times
for i in range(1000):
    # Iterate through array which is the numbers reversed order and double them
    carry_the_one = False
    for i in range(len(a)):
        a[i] *= 2
        if carry_the_one:
            a[i] += 1
        if a[i] >= 10:
            carry_the_one = True
            a[i] = a[i] % 10
        else:
            carry_the_one = False
    if carry_the_one == True:
        a.append(1)
print(sum(a))
