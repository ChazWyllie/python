# Description: Implementing an array in Python
arr = [1, 2, 3, 4, 5]
print(f"array list (arr): {arr}")

# Reversing the array
reversed_arr = arr.reverse() # or arr = arr[::-1]
print(f"reversed array list (reversed_arr): {reversed_arr}")

# Accessing the first element
print(f"first element of arr: {arr[0]}")

# Accessing the last element
print(f"last element of arr: {arr[-1]}")

# Modifying the first element
arr[0] = 10
print(f"modified first element of arr: {arr[0]}")
print(f"array list (arr) with index 0 modified: {arr}")

# Inserting an element at the end
arr.append(6)
print(f"array list (arr) with 6 appended: {arr}")

# Inserting an element at a specific index
arr.insert(3, 7)
print(f"array list (arr) with 7 inserted at index 3: {arr}")

# Removing an element by value
arr.remove(7)
print(f"array list (arr) with 7 removed: {arr}")

# Removing an element by index
arr.pop(3)

# Searching if an element exists in an array
print(f"checking if 10 exists in arr: {10 in arr}")
if 10 in arr:
    print("Element exists")
    
# Traverse through the array
print("Traversing through the array")
for i in arr:
    print(f"index {arr.index(i)}: {i}")

# Finding the length of an array
print(f"length of arr: {len(arr)}")

# Finding the maximum element
print(f"maximum element in arr: {max(arr)}")

# Finding the index of an element
print(f"finding the index of an element 3: {arr.index(3)} is the position of 3 in arr")

# Finding the count of an element
print(f"finding the count of an element in arr 10: there are {arr.count(10)} 10s in arr")