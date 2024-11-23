def find_second_largest(array):
    if len(array) < 2:
        return None  # Not enough elements

    first, second = float('-inf'), float('-inf')
    for num in array:
        if num > first:
            second = first
            first = num
        elif num > second:
            second = num
    return second

# Example usage:
array = [10, 20, 5, 7, 25]
print(find_second_largest(array))

#the optimized one 
def find_second_largest2(set):
    array=list(set)
    if len(array) < 2:
        return None  # Not enough elements
    array.sort()
    return array[-2]

# Example usage:
array = [10, 20, 5, 7, 25]

print(find_second_largest(array))
