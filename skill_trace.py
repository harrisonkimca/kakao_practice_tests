from functools import wraps

# decorator to trace execution of recursive function
def trace(func):
  # cache func name, which will be used for trace print
  func_name = func.__name__
  # define the separator, which will indicate current recursion level (repeated N times)
  separator = '|  '
  # current recursion depth
  trace.recursion_depth = 0

  @wraps(func)
  def traced_func(*args, **kwargs):
    # repeat separator N times (where N is recursion depth)
    # `map(str, args)` prepares the iterable with str representation of positional arguments
    # `", ".join(map(str, args))` will generate comma-separated list of positional arguments
    # `"x"*5` will print `"xxxxx"` - so we can use multiplication operator to repeat separator
    print(f'{separator * trace.recursion_depth}|-- {func_name}({", ".join(map(str, args))})')
    # we're diving in
    trace.recursion_depth += 1
    result = func(*args, **kwargs)
    # going out of that level of recursion
    trace.recursion_depth -= 1
    # result is printed on the next level
    print(f'{separator * (trace.recursion_depth + 1)}|-- RETURN {result}')

    return result

  return traced_func

def factorial(n):
  if n == 1: return 1
  else: return n * factorial(n-1)


# since the name of decorated func is the same as the name of original one
# decorator will be applied to nested calls too
# factorial = trace(factorial)

# this will print all the recursion trace and the result at the bottom
# print(factorial(7))

# PERMUTATIONS RECURSIVE SOLUTION
def recursive(num,i=0):
  if i == len(num):
    print("".join(num))
  # loop through each element of the string
  for j in range(i,len(num)):
    # copy each element of string into list
    nums = [c for c in num]
    # swapping elements creates different combinations
    nums[i], nums[j] = nums[j], nums[i]
    # use recursion to generate different combinations under current element's subtree  
    recursive(nums, i+1)
    # call stack unwinds back to previous branch of subtree before recursion starts again

# recursive = trace(recursive)
# recursive('123')


'''
           Start
      /      |      \
     1       2       3 
    / \     / \     / \
   2   3   1   3   1   2
   |   |   |   |   |   |  
   3   2   3   1   2   1

The 'for loop' traverses each element of the string by locking in each element as the first element before using recursion to create subtrees of combinations under each element. The subtree under each element uses recursion to create different combinations by swapping elements after the first locked in element until the final element is reached. The recurision's call stack then unwinds back to any previous branches (left tree recursion to depth of 3 but right tree recursion to depth of 2 only to reach a previous branch) and begins a new recursion to create a new subtree of combinations.
'''

# COMBINATIONS RECURSIVE SOLUTION
def combination(lst, n):
  print(f"_________n:{n}_________")
  # base case
  if n == 0:
    return [[]]
     
  combos = []
  for i in range(0, len(lst)):
    print(f"______i:{i} len:{len(lst)}______")
    m = lst[i]
    remLst = lst[i + 1:]       
    remainlst_combo = combination(remLst, n-1)
    print(f"remainlst_combo:{remainlst_combo}")
    for p in remainlst_combo:
      combos.append([m, *p])
      print(f"combos_loop:{combos}")
    print(f"combos_end:{combos}")
    print("________________END_________________")
           
  return combos

combination = trace(combination)
print(combination([1,2,3,4,5],3))

'''

Combination decision tree

     [1, 2, 3, 4] 
   /    |    |    \
  1     2    3     4
 /|\   / \   |     |
2 3 4 3   4  4     X 

number of combinations:
  n! / (n-k)!k!

'''


def combo(lst, n):
  print(f"______________n:{n}______________")
  # n sets the depth of the nesting
  if n == 0:
    return [[]]
  combos = []
  for i in range(0, len(lst)):
    print(f"___________i:{i} len:{len(lst)}___________")
    m = lst[i]
    remLst = lst[i + 1:]
    print(f"lst[{i}]:{m}")
    print(f"lst[{i+1}]:{remLst}")
    combos.append([m,remLst])
    print(f"combos_loop:{combos}")
    combo(remLst, n-1)
    print("===============================")
    print(f"combos_end:{combos}")
    print("===============================")
  print("*************RETURN*************")
  return combos
    
    
combo = trace(combo)
# print(combo([1,2,3,4,5],3))

'''
      [1, 2, 3, 4, 5]  k = 3
      /                                 \               \
    1[2,3,4,5]                        2[3,4,5]        3[4,5]
       |            \     \   \       /    |  \       /   \
    2[3,4,5]      3[4,5] 4[5] 5[]  3[4,5] 4[5] 5[]  4[5] 5[]
   /    |   \      /   \   |   |    /  \    |   |    /    \
3[4,5] 4[5] 5[]  4[5] 5[] 5[] []  4[5] 5[] 5[] []  5[]    []


  [[3]]
  [[3],[4]]
  [[3],[4],[5]]
  [[2,3],[2,4],[2,5]]
  [[4]]
  [[4],[5]]
  [[2,3],[2,4],[2,5],[3,4],[3,5]]
  [[5]]
  [[2,3],[2,4],[2,5],[3,4],[3,5],[4,5]]
  [[2,3],[2,4],[2,5],[3,4],[3,5],[4,5],[]]
  [[1,2,3],[1,2,4],[1,2,5],[1,3,4],[1,3,5],[1,4,5]]
  [[4]]
  [[4],[5]]
  [[3,4],[3,5]]
  [[5]]
  [[3,4],[3,5],[4,5]]
  [[3,4],[3,5],[4,5],[]]
  [[1,2,3],[1,2,4],[1,2,5],[1,3,4],[1,3,5],[1,4,5],[2,3,4],[2,3,5],[2,4,5]]
  [[5]]
  [[4,5]]
  [[4,5],[]]
  [[1,2,3],[1,2,4],[1,2,5],[1,3,4],[1,3,5],[1,4,5],[2,3,4],[2,3,5],[2,4,5],[3,4,5]]
  [[1,2,3],[1,2,4],[1,2,5],[1,3,4],[1,3,5],[1,4,5],[2,3,4],[2,3,5],[2,4,5],[3,4,5],[]]
  [[1,2,3],[1,2,4],[1,2,5],[1,3,4],[1,3,5],[1,4,5],[2,3,4],[2,3,5],[2,4,5],[3,4,5]]

'''