## Description
Arrays are contiguous memory structures that store elements (usually of the same type)
This folder consists of several simple operations that can be done with an array
## Key Characteristics of Arrays
- Index-based: Elements are accesed via indices (starting from 0)
- Contigious memory: Elements are stored back-to-back in memory
- Fixed size: In some languages, some arrays cannot change after creation
- Dynamic (Python lists): Python listrs can expand or contract based on the operation

## Basic Operations
- Access: arr[index]
- Insert: arr.append(value) or arr.insert(index, value)
- Delete: del arr[index] or arr.pop(index)
- Iteration: for i in arr:

## Time Complexity of Array Operations
- Access (by index) = O(1)
- Search (unsorted) = O(n)
- Insert (end) = O(1)
- Insert (at index) = O(n)
- Delete (by value) = O(n)
