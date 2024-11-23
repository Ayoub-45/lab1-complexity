def find_max(array):
    max_value = array[0]
    for num in array[1:]:
        if num > max_value:
            max_value = num
    return max_value

# Example usage:
array = [10, 20, 5, 7, 25]
print(find_max(array))
