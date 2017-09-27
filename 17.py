# Strategy: keep maps of how many letters are in different conditions and go from there
result = 0
word_counts = {0:0, 1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4}
teen_counts = {10: 3, 11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8}
tens_counts = {0:0, 1:3, 2:6, 3:6, 4:5, 5:5, 6:5, 7:7, 8:6, 9:6}

for i in range(1,1000):
    # Add hundreds digit's contribution - number plus "hundred" and "and" when applicable
    old_result = result
    if i >= 100:
        # Add "x hundred"
        result += word_counts[i//100] + 7
        if i % 100 != 0:
            # Add "and"
            result += 3

    # Add last two digits' contribution
    # Is a special "teen" number
    if 10 < i % 100 < 20:
        result += teen_counts[i % 100]
    # Is not a special "teen" number - add tens and ones contrutions
    else:
        result += tens_counts[(i//10) % 10] + word_counts[i%10]
# Add one thousand
result += 3 + 8
print(result)
