def position(letter):
    return ord(letter) - ord('A')
def frequency_scan_26_times(array):
    freq = [0] * 26
    for i in range(26):
        letter = chr(i + ord('A'))
        freq[i] = sum(1 for x in array if x == letter)
    return freq
#solution 2: optimized
def frequency_single_scan(array):
    freq = [0] * 26
    for letter in array:
        freq[position(letter)] += 1
    return freq

# Example usage:
array = ['A', 'B', 'C', 'A', 'D', 'A']
print(frequency_single_scan(array))

array = ['A', 'B', 'C', 'A', 'D', 'A']
print(frequency_scan_26_times(array))
