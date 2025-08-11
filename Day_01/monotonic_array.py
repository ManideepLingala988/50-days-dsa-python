"""
Day 01 — Monotonic Array
Problem:
An array is monotonic if it is either entirely non-increasing or non-decreasing.

Approach:
- Track if array is increasing or decreasing
- Return True if one of them holds
Time Complexity: O(n)
Space Complexity: O(1)
"""

def monotonic_array(array):
    n = len(array)
    i = array[0]
    j = array[n - 1]

    if i > j: 
        for k in range(n - 1):
            if array[k] < array[k + 1]:
                return False
        return True

    elif i == j: 
        for k in range(n - 1):
            if array[k] != array[k + 1]:
                return False
        return True

    else:
        for k in range(n - 1):
            if array[k] > array[k + 1]:
                return False
        return True

print(monotonic_array([1, 2, 3, 4, 5]))   
print(monotonic_array([5, 4, 3, 2, 1]))   
print(monotonic_array([2, 2, 2, 2]))      
print(monotonic_array([1, 3, 2]))    
