import array

# arrays.py

# Importing the array module

# Creating an array
arr = array.array('i', [1, 2, 3, 4, 5])
print("Initial array:", arr)

# Accessing elements
print("Element at index 0:", arr[0])
print("Element at index 2:", arr[2])

# Adding elements
arr.append(6)
print("Array after appending 6:", arr)

arr.insert(2, 9)
print("Array after inserting 9 at index 2:", arr)

# Removing elements
arr.remove(3)
print("Array after removing 3:", arr)

popped_element = arr.pop()
print("Array after popping an element:", arr)
print("Popped element:", popped_element)

# Updating elements
arr[1] = 7
print("Array after updating index 1 to 7:", arr)

# Slicing the array
sliced_arr = arr[1:4]
print("Sliced array (index 1 to 3):", sliced_arr)

# Looping through the array
print("Looping through the array:")
for element in arr:
    print(element)

# Length of the array
print("Length of the array:", len(arr))

# Array concatenation
arr2 = array.array('i', [10, 11, 12])
concatenated_arr = arr + arr2
print("Concatenated array:", concatenated_arr)

# Array repetition
repeated_arr = arr * 2
print("Repeated array:", repeated_arr)

# Finding the index of an element
index_of_7 = arr.index(7)
print("Index of element 7:", index_of_7)

# Counting occurrences of an element
count_of_1 = arr.count(1)
print("Count of element 1:", count_of_1)