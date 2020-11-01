# Getting a Different Number
# Given an array arr of unique nonnegative integers, 
# implement a function getDifferentNumber that finds the smallest nonnegative integer 
# that is NOT in the array.

# Even if your programming language of choice doesn’t have that restriction (like Python), 
# assume that the maximum value an integer can have is MAX_INT = 2^31-1. 
# So, for instance, the operation MAX_INT + 1 would be undefined in our case.

# Your algorithm should be efficient, both from a time and a space complexity perspectives.

# Solve first for the case when you’re NOT allowed to modify the input arr. 
# If successful and still have time, see if you can come up with an algorithm 
# with an improved space complexity when modifying arr is allowed. 
# Do so without trading off the time complexity.

# Analyze the time and space complexities of your algorithm.

# Example:
# input:  arr = [0, 1, 2, 3]
# output: 4 

# Solution 1 (not modifying original array)
# Time:
# O(n)
# Space:
# O(n)
# n = len(arr)

# Solution 2 (modifying original array)
# Time:
# O(n)
# Space:
# O(1)
# n = len(arr)

# Solution 1
def get_different_number(arr):
  expected = range(len(arr)) 
  present = {} 
  for i in arr:
    present[i] = True
                        
  for i in expected:
    if not i in present:
      return i
    
  return len(arr)

# Solution 2
def get_different_number2(arr): 
  for i in range(len(arr)):          
    if not arr[i] == i or arr[i] < len(arr): 
      val = arr[i]
      while val < len(arr) and arr[val] != val:
        temp = arr[val]
        arr[val] = val
        val = temp
        
  lookingFor = 0
  for i in (arr):
    if i != lookingFor:
      return lookingFor
    lookingFor += 1
    
  return len(arr)