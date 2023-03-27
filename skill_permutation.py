# recursive solution
# https://www.programiz.com/python-programming/examples/permutation-of-string
# iterative solution
# https://stackoverflow.com/questions/18227931/iterative-solution-for-finding-string-permutations
# Best explanation of decision tree for recursive:
# https://www.youtube.com/watch?v=KukNnoN-SoY
# Best explanation of decision tree for iterative:
# https://www.youtube.com/watch?v=f-nJYykmp4k

from itertools import permutations

# ITERTOOLS SOLUTION
words = [''.join(p) for p in permutations('pro')]
# print("Itertools:")
# print(words)

# RECURSIVE SOLUTION
# full explanation in tracing.py
def recursive(num,i=0):
  # base case (recursion ends when only one number left for combinations)
  if i == len(num):
    print("".join(num))
  # loop through each number of num list (ie, if '123' then num[0],num[1],num[2])
  for j in range(i,len(num)):
    # copy each element of string into list 
    nums = [c for c in num]
    # swapping elements creates different combinations
    nums[i], nums[j] = nums[j], nums[i]
    # use recursion to generate different combinations under current element's subtree
    recursive(nums, i+1)
    # call stack unwinds back o previous branch of subtree before recursion starts again

# print("Recursive permutation")
# print(recursive('123'))

    
# ITERATIVE SOLUTION
# pop off each element from the stack and add element to every position
# of existing combinations to create new combinations until stack is empty
def permutation(num):
  # avoid empty stack
  if not num:
    return []
  # add num list to stack
  stack = list(num)
  # pop off last element from stack to build first combination
  results = [stack.pop()]
  print(f"results:{results}")
  while stack:
    # pop off next element from stack (continue until empty)
    current_num = stack.pop()
    # list to hold new sets of combinations
    # as elements added to each position
    new_results = []
    # use 'for loop' to insert current_num into every position
    # of existing results list
    for i in results:
      # use 'for loop' to in insert current_num into every position
      # of existing results list (including the end so all positions 
      # equals the length of i plus 1)
      for j in range(len(i) + 1):
        # current_num will be inserted at each index position 'j'
        # by splitting new_results list at position 'j'
        # and add to new_results list
        new_results.append(i[:j] + current_num + i[j:])
    # update results list to add new element combinations from new_results list
    results = new_results
    print(f"new_results:{results}")
  return results

print("Iterative permutation")
print(permutation('123'))


