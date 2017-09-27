# Strategy: Store the maximum path to get to a particular spot. Populate this and then return the maximum of the
# bottom row

path = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""
overall_max_paths = []
path = path.split("\n")
for row in range(len(path)):
    path[row] = path[row].split(" ")
for row in range(len(path)):
    # Base base
    if row == 0:
        overall_max_paths.append([int(path[0][0])])
        continue
    max_paths = []
    for col in range(len(path[row])):
        # Left edge case
        if col == 0:
            max_paths.append(int(path[row][col]) + int(overall_max_paths[row-1][col]))
        # Right edge case
        elif col == len(path[row]) - 1:
            max_paths.append(int(path[row][col]) + int(overall_max_paths[row-1][col-1]))
        # General case
        else:
            max_paths.append(int(path[row][col]) + int(max(overall_max_paths[row-1][col], overall_max_paths[row-1][col-1])))
    overall_max_paths.append(max_paths)
print(max(overall_max_paths[-1]))
