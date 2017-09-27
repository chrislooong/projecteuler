# Strategy: find cycles by doing the reverse mappings and storing the distance from 
# Also maintain the longest chain
distances = {1:1}
max_distance = 1
has_max_distance = 1
for i in range(2,1000000):
    # Find a number for which we know the distance
    nums_traversed = [i]
    while nums_traversed[-1] not in distances.keys():
        if nums_traversed[-1] % 2 != 0:
            next_number = 3 * nums_traversed[-1] + 1
        else:
            next_number = int(nums_traversed[-1] / 2)
        nums_traversed.append(next_number)
    # Populate the values we found except for the one most recently found
    base_distance = distances[nums_traversed[-1]]
    for j in range(len(nums_traversed)):
        distances[nums_traversed[-1*(j+1)]] = base_distance + j
    if distances[i] > max_distance:
        max_distance = distances[i]
        has_max_distance = i
print(has_max_distance)
