# STRETCH: implement Linear Search				
def linear_search(arr, target):
    for i in arr:
      if arr[i] == target:
          return arr[i]
     
  # TO-DO: add missing code

    return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)-1

  # TO-DO: add missing code

  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
     high =arr.length -1
     low = 0
     middle = 0
    
     while low <= high:
      middle = (low+high)//2
      if arr[middle] == target:
       arr[middle] 
      if target > arr[middle] :
          low = middle +1
      else:
            high = middle +1
      return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls

  # TO-DO: add missing if/else statements, recursive calls
