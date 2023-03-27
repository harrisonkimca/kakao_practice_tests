def bubble_sort(arr):
  swaps = True
  while swaps:
    # pass
    swaps = False
    for i, n in enumerate(arr):
      if i < len(arr)-1 and arr[i] > arr[i+1]:
        temp = arr[i]
        arr[i] = arr[i+1]
        arr[i+1] = temp
        swaps = True
  return arr

print(bubble_sort([6, 8, 2, 3, 4]))

def linear_search(arr, element_to_find):
  found = False
  i = 0
  while not found and i < len(arr):
    if arr[i] == element_to_find:
      found = True
    i = i + 1
  return found

print(linear_search([6, 8, 2, 3, 4], 2))
print(linear_search([6, 8, 2, 3, 4], 5))