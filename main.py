# The mode formula is |
#  mode = l + (f1 - f0 / 2f1 - f0 - f2) * h

# Explaination :
# \(l\) = Lower limit of the modal class (the class interval with the highest frequency).\(h\) = Size of the class interval (assuming all class sizes are equal).\(f_{1}\) = Frequency of the modal class.\(f_{0}\) = Frequency of the class preceding (before) the modal class.\(f_{2}\) = Frequency of the class succeeding (after) the modal class.


#  execution :

# 1. Define your grouped data
# Representing class intervals as (lower_limit, upper_limit)
class_intervals = [(0, 10), (10, 20), (20, 30), (30, 40), (40, 50)]
frequencies = [5, 12, 20, 15, 8]

# 2. Find the index of the modal class (the maximum frequency)
max_freq = frequencies[0]
modal_index = 0

for i in range(1, len(frequencies)):
    if frequencies[i] > max_freq:
        max_freq = frequencies[i]
        modal_index = i

# 3. Extract the NCERT variables based on the modal index
l = class_intervals[modal_index][0]                 # Lower limit of modal class
h = class_intervals[modal_index][1] - l             # Class width (Upper - Lower)
f1 = frequencies[modal_index]                       # Modal class frequency

# Use safety checks in case the modal class is at the very beginning or end
f0 = frequencies[modal_index - 1] if modal_index > 0 else 0
f2 = frequencies[modal_index + 1] if modal_index < len(frequencies) - 1 else 0

# 4. Apply the exact NCERT Formula
numerator = f1 - f0
denominator = (2 * f1) - f0 - f2
mode = l + (numerator / denominator) * h

# 5. Output results
print(f"Modal Class: {class_intervals[modal_index]}")
print(f"Variables: l={l}, h={h}, f1={f1}, f0={f0}, f2={f2}")
print(f"Calculated Mode: {mode:.4f}")



#  The median formula :

# There are total two cases 

#  If n is odd :
# M = (n+1 / 2)^th term


#  If n is even:
#  M = ( (n / 2) term + (n / 2 + 1 ) / 2 )


# 1. Define raw, unsorted data
data = [12, 3, 5, 20, 8, 15, 18, 9]

# 2. Step 1: Sort the data in ascending order
sorted_data = sorted(data)
n = len(sorted_data)

# 3. Step 2: Apply conditional logic for Odd vs Even
if n % 2 != 0:
    # Odd case: Pick the single middle index
    middle_index = n // 2
    median = sorted_data[middle_index]
else:
    # Even case: Average the two middle indices
    idx1 = (n // 2) - 1
    idx2 = n // 2
    median = (sorted_data[idx1] + sorted_data[idx2]) / 2

# 4. Output results
print(f"Sorted Data: {sorted_data}")
print(f"Total elements (n): {n}")
print(f"Calculated Median: {median}")

