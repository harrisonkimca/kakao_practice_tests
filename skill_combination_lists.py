# Explanation of combination decision tree
# https://www.youtube.com/watch?v=q0s6m7AiM7o
# https://www.geeksforgeeks.org/combinations-in-python-without-using-itertools/

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

# ITERTOOLS SOLUTION
from itertools import combinations

# print(list(combinations('abc', 2)))

# RECURSIVE SOLUTION
def find_combinations(lst, n):
  print(f"CALL combination. lst: {lst}, n: {n} len: {len(lst)}")
  # base case
  if n == 0:
    combos = [[]]
    print(f"RETURN combos: {combos}")
    return combos
  # list to store all combinations
  combos = []
  for i in range(0, len(lst)):
    
    m = lst[i]
    remLst = lst[i + 1:]
    print(f"lst: {lst} i: {i} n: {n} m[{i}]: {m} remLst:{remLst}")
    # recursion
    remainlst_combo = find_combinations(remLst, n-1)
    print(f"remainlst_combo:{remainlst_combo}")
    for p in remainlst_combo:
      print(f"m:{m} p:{*p,}")
      combos.append([m, *p])
      print(f"combos.append:{combos}")
  print(f"RETURN combos: {combos}")
  return combos

# find_combinations([1,2,3,4,5],3)

#                                      tracing                        backtracking                                                                                                                                                                                                                                                                                                                 tracing                    backtracking                                                                                                                                                                                      tracing                  backtracking                                                                                                                      tracing                backtracking                                                tracing               backtracking                         
#                                      lst=[1, 2, 3, 4, 5] len=5                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
#                                      i=0                            <-- remainlst_combo=[[1,2,3],[1,2,4],[1,2,5],[1,3,4],[1,3,5],[1,4,5]]                                                                                                                                                                                                                                                        i=1                        <-- remainlst_combo=[[1,2,3],[1,2,4],[1,2,5],[1,3,4],[1,3,5],[1,4,5],[2,3,4],[2,3,5],[2,4,5]]                                                                                                     i=2                      <-- remainlst_combo=[[1,2,3],[1,2,4],[1,2,5],[1,3,4],[1,3,5],[1,4,5],[2,3,4],[2,3,5],[2,4,5],[3,4,5]]                             i=3                                                                                i=4                   <-- return combos=[[1,2,3],[1,2,4],[1,2,5],[1,3,4],[1,3,5],[1,4,5],[2,3,4],[2,3,5],[2,4,5],[3,4,5]]
#                                      n=3, m=1, remLst=[2,3,4,5]     <-- remainlst_combo=[[2,3],[2,4],[2,5],[3,4],[3,5],[4,5]]                                                                                                                                                                                                                                                                    n=3, m=2, remLst=[3,4,5]   <-- remainlst_combo=[[3,4],[3,5],[4,5]]                                                                                                                                                           n=3, m=3, remLst=[4,5]   <-- remainlst_combo=[[4,5]]                                                                                                       n=3, m=4, remLst=[5]   <-- remainlst_combo=[]                                      n=3, m=5, remLst=[]   <-- remainlst_combo=[]
#                                              |                      m=1, p=(2,3), append[[m=1,p=[2,3]]], combos=[[1,2,3]]                                                                                                                                                                                                                                                                              |                    m=2, p=(3,4), append[[m=2,p=[3,4]]], combos=[[1,2,3],[1,2,4],[1,2,5],[1,3,4],[1,3,5],[1,4,5],[2,3,4]]                                                                                                     |                m=3, p=(4,5), append[[m=3,p=[4,5]]], combos=[[1,2,3],[1,2,4],[1,2,5],[1,3,4],[1,3,5],[1,4,5],[2,3,4],[2,3,5],[2,4,5],[3,4,5]]           |                                                                                  |               m=5, p=(), skip for_loop (empty array)
#                                              |                      m=1, p=(2,4), append[[m=1,p=[2,4]]], combos=[[1,2,3],[1,2,4]]                                                                                                                                                                                                                                                                      |                    m=2, p=(3,5), append[[m=2,p=[3,5]]], combos=[[1,2,3],[1,2,4],[1,2,5],[1,3,4],[1,3,5],[1,4,5],[2,3,4],[2,3,5]]                                                                                     lst=[4,5] len=2                                                                                                                                            lst=[5], len=1                                                                     lst[], len=0          
#                                              |                      m=1, p=(2,5), append[[m=1,p=[2,5]]], combos=[[1,2,3],[1,2,4],[1,2,5]]                                                                                                                                                                                                                                                              |                    m=2, p=(4,5), append[[m=2,p=[4,5]]], combos=[[1,2,3],[1,2,4],[1,2,5],[1,3,4],[1,3,5],[1,4,5],[2,3,4],[2,3,5],[2,4,5]]                                                                             /                                                                       \                                                                                  /                                                                                  i=0                   <-- return combos=[] (empty array)
#                                              |                      m=1, p=(3,4), append[[m=1,p=[3,4]]], combos=[[1,2,3],[1,2,4],[1,2,5],[1,3,4]]                                                                                                                                                                                                                                                lst=[3,4,5] len=3                                                                                                                                                                                                            tracing                backtracking                                     tracing                backtracking                                                tracing                backtracking                                                n=2, m=[], remLst=[]  <-- len=0, skip for_loop, append nothing
#                                              |                      m=1, p=(3,5), append[[m=1,p=[3,5]]], combos=[[1,2,3],[1,2,4],[1,2,5],[1,3,4],[1,3,5]]                                                                                                                                                                                                                 /                                                                               \                                                                                  \                                                                                i=0                    <-- remainlst_combo=[[4,5]]                      i=1                    <-- return combos=[[4,5]]                                   i=0                    <-- return combos=[]
#                                              |                      m=1, p=(4,5), append[[m=1,p=[4,5]]], combos=[[1,2,3],[1,2,4],[1,2,5],[1,3,4],[1,3,5],[1,4,5]]                                                                                                                                                                                                        tracing                  backtracking                                          tracing                backtracking                                                tracing                backtracking                                                n=2, m=4, remLst=[5]   <-- remainlst_combo=[[5]]                        n=2, m=5, remLst=[]    <-- remainlst_combo=[] (empty array - just return combos)   n=2, m=5, remLst=[]    <-- remainlst_combo=[] (empty array - just return combos)
#                                      lst=[2,3,4,5] len=4                                                                                                                                                                                                                                                                                                                 i=0                      <-- remainlst_combo=[[3,4],[3,5]]                     i=1                    <-- remainlst_combo=[[3,4],[3,5],[4,5]]                     i=2                    <-- return combos=[[3,4],[3,5],[4,5]]                             |                m=4, p=(5), append[[m=4,p=5]], combos=[[[4,5]]         |                m=5, p=(), skip for_loop (empty array)                            |                m=5, p=(), skip for_loop (empty array)
#        /                                                                              \                                                                                                 \                                                                                              \                                                                                 n=2, m=3, remLst=[4,5]   <-- remainlst_combo=[[4],[5]]                         n=2, m=4, remLst=[5]   <-- remainlst_combo=[[5]]                                   n=2, m=5, remLst=[]    <-- remainlst_combo=[] (empty array - just return combos)         |                                                                 lst=[] len=0                                                                       lst=[] len=0           
# tracing                    backtracking                                                tracing                   backtracking                                                            tracing                backtracking                                                            tracing              backtracking                                                      |                  m=3, p=(4), append[[m=3,p=4]], combos=[[3,4]]                |               m=4, p=(5), append[[m=4,p=5]], combos=[[3,4],[3,5],[4,5]]         |                m=5, p=(), skip for_loop (empty array)                      lst=[5] len=1                                                           i=0                    <-- return combos=[] (empty array)                          i=0                    <-- return combos=[] (empty array)
# i=0                        <-- remainlst_combo=[[2,3],[2,4],[2,5]]                     i=1                       <-- remainlst_combo=[[2,3],[2,4],[2,5],[3,4],[3,5]]                     i=2                    <-- remainlst_combo=[[2,3],[2,4],[2,5],[3,4],[3,5],[4,5]]               i=3                  <-- return combos=[[2,3],[2,4],[2,5],[3,4],[3,5],[4,5]]           |                  m=3, p=(5), append[[m=3,p=5]], combos=[[3,4],[3,5]]          |                                                                           lst=[] len 0                                                                       i=0                    <-- return combos=[[5]]                          n=1, m=[], remLst=[]   <-- len=0, skip for_loop, append nothing                    n=1, m=[], remLst=[]   <-- len=0, skip for_loop, append nothing
# n=2, m=2, remLst=[3,4,5]   <-- remainlst_combo=[[3],[4],[5]]                           n=2, m=3, remLst=[4,5]    <-- remainlst_combo=[[4],[5]]                                           n=2, m=4, remLst=[5]   <-- remainlst_combo=[[5]]                                               n=2, m=5, remLst=[]  <-- remainlst_combo=[] (empty array - just return combos)   lst=[4,5] len=2                                                                lst=[5] len 1                                                                      i=0                    <-- return combos=[] (empty array)                          n=1, m=5, remLst=[]    <-- remainllist_combo=[[5]]
#          |                 m=2, p=[3], append[[m=2,p=3]], combos=[[2,3]]                  |                      m=3, p=[4], append[[m=3,p=4]], combos=[[2,3],[2,4],[2,5],[3,4]]            |                   m=4, p=[5], append[[5]], combos=[[2,3],[2,4],[2,5],[3,4],[3,5],[4,5]]      |                 m=5, p=[], skip for_loop (empty array)                      i=0                      <-- return combos=[[4],[5]]                           i=0                    <-- return combos=[[5]]                                     n=1, m=[], remLst=[]   <-- len=0, skip for_loop, append nothing                          |
#          |                 m=2, p=[4], append[[m=2,p=4]], combos=[[2,3],[2,4]]            |                      m=3, p=[5], append[[m=3,p=5]], combos=[[2,3],[2,4],[2,5],[3,4],[3,5]]   lst[5], len=1                                                                                  lst[], len=0                                                                     n=1, m=4, remLst=[5]     <-- remainlst_combo=[[4],[5]]                         n=1, m=5, remLst=[]    <-- remainlst_combo=[[5]]                                                                                                                      i=0, m=5, remLst=[], remainlist_combo=[[]], append[m=5]                   
#          |                 m=2, p=[5], append[[m=2,p=5]], combos=[[2,3],[2,4],[2,5]]   lst[4,5] len=2                                                                                    i=0                    <-- return combos=[[5]]                                                 i=0                  <-- return combos=[] (empty array)                                |                                                                              |                                                                                                                                                               i=1, m=[], remLst=[], remainlist_combo=[[]], append nothing
# lst=[3,4,5] len=3                                                                      i=0                       <-- return combos=[[4],[5]]                                             n=1, m=5, remLst=[]    <-- remainlst_combo=[[5]]                                               n=1, m=[], remLst=[] <-- len=0, skip for_loop, append nothing                    i=0, m=4, remLst=[5], remainlst_combo=[[]], append[m=4]                        i=0, m=5, remLst=[], remainlist_combo=[[]], append[m=5]                                                                                                                     /
# i=0                        <-- return combos [[3],[4],[5]]                             n=1, m=4, remLst=[5]      <-- remainlst_combo=[[4],[5]]                                             |                                                                                                                                                                             i=1, m=5, remLst=[], remainlst_combo=[[]], append[m=5]                         i=1, m=[], remLst=[], remainlist_combo=[[]], append nothing                                                                                                              lst=[]  
# n=1, m=3, remLst=[4,5]     <-- remainlst_combo=[[3],[4],[5]]                                    |                                                                                        i=0, m=5, remLst=[], remainlst_combo=[[]], append[m=5]                                                                                                                                /          \                                                                   /                                                                                                                                                                  n=0 
#          |                                                                             i=0, m=4, remLst=[5], remainlst_combo=[[]], append[m=4]                                           i=0, m=[], remLst=[], remainlst_combo=[[]], append nothing                                                                                                                         lst[5]       lst[]                                                             lst[5]                                                                                                                                                                return [[]]
# i=0, m=3, remLst=[4,5], remainlst_combo=[[]], append[m=3]                              i=1, m=5, remLst=[], remainlst_combo=[[]], append[m=5]                                                  /                                                                                                                                                                            n=0          n=0                                                               n=0                                                                                                                                                                 
# i=1, m=4, remLst=[5], remainlst_combo=[[]], append[m=4]                                      /            \                                                                                 lst=[]                                                                                                                                                                          return [[]]  return [[]]                                                       return [[]]                                                                                                                                                         
# i=2, m=5, remLst=[], remainlst_combo=[[]], append[m=5]                                    lst=[5]        lst=[]                                                                             n=0                                                                                                                                                                                                        
#         /           |           \                                                         n=0            n=0                                                                                return [[]]                                                                            
#    lst=[4,5]     lst=[5]      lst=[]                                                      return [[]]    return [[]]                                                                                                                                                               
#    n=0           n=0          n = 0                                                      
#    return [[]]   return[[]]   return =[[]]  
#
# recursive call, draw | on the tree going down
# return value, go back up the arrow |
#
#       [1, 2, 3, 4, 5]  k = 3
#       /                                 \               \
#     1[2,3,4,5]                        2[3,4,5]        3[4,5]
#        |            \     \   \       /    |  \       /   \
#     2[3,4,5]      3[4,5] 4[5] 5[]  3[4,5] 4[5] 5[]  4[5] 5[]
#    /    |   \      /   \   |   |    /  \    |   |    /    \
# 3[4,5] 4[5] 5[]  4[5] 5[] 5[] []  4[5] 5[] 5[] []  5[]    []
#
#   [[3]]
#   [[3],[4]]
#   [[3],[4],[5]]
#   [[2,3],[2,4],[2,5]]
#   [[4]]
#   [[4],[5]]
#   [[2,3],[2,4],[2,5],[3,4],[3,5]]
#   [[5]]
#   [[2,3],[2,4],[2,5],[3,4],[3,5],[4,5]]
#   [[2,3],[2,4],[2,5],[3,4],[3,5],[4,5],[]]
#   [[1,2,3],[1,2,4],[1,2,5],[1,3,4],[1,3,5],[1,4,5]]
#   [[4]]
#   [[4],[5]]
#   [[3,4],[3,5]]
#   [[5]]
#   [[3,4],[3,5],[4,5]]
#   [[3,4],[3,5],[4,5],[]]
#   [[1,2,3],[1,2,4],[1,2,5],[1,3,4],[1,3,5],[1,4,5],[2,3,4],[2,3,5],[2,4,5]]
#   [[5]]
#   [[4,5]]
#   [[4,5],[]]
#   [[1,2,3],[1,2,4],[1,2,5],[1,3,4],[1,3,5],[1,4,5],[2,3,4],[2,3,5],[2,4,5],[3,4,5]]
#   [[1,2,3],[1,2,4],[1,2,5],[1,3,4],[1,3,5],[1,4,5],[2,3,4],[2,3,5],[2,4,5],[3,4,5],[]]
#   [[1,2,3],[1,2,4],[1,2,5],[1,3,4],[1,3,5],[1,4,5],[2,3,4],[2,3,5],[2,4,5],[3,4,5]]
#
# CALL combination. lst:[1,2,3,4,5], n:3 len:5
# lst:[1,2,3,4,5] i:0 n:3 m[0]:1 remLst:[2,3,4,5]
# CALL combination. lst:[2,3,4,5], n:2 len:4
#      lst:[2,3,4,5] i:0 n:2 m[0]:2 remLst:[3,4,5]
#           CALL combination. lst:[3,4,5], n:1 len:3
#           lst:[3,4,5] i:0 n:1 m[0]:3 remLst:[4,5]
#                CALL combination. lst:[4,5], n:0 len:2
#                RETURN combos:[[]]
#                remainlst_combo:[[]]
#                m:3 p:()
#                combos.append:[[3]]
#           lst:[3,4,5] i:1 n:1 m[1]:4 remLst:[5]
#                CALL combination. lst:[5], n:0 len:1
#                RETURN combos:[[]]
#                remainlst_combo:[[]]
#                m:4 p:()
#                combos.append:[[3],[4]]
#           lst:[3,4,5] i:2 n:1 m[2]:5 remLst:[]
#                CALL combination. lst:[], n:0 len:0
#                RETURN combos:[[]]
#                remainlst_combo:[[]]
#                m:5 p:()
#                combos.append:[[3],[4],[5]]
#                RETURN combos:[[3],[4],[5]]
#                     remainlst_combo:[[3],[4],[5]]
#                     m:2 p:(3,)
#                     combos.append:[[2,3]]
#                     m:2 p:(4,)
#                     combos.append:[[2,3],[2,4]]
#                     m:2 p:(5,)
#                     combos.append:[[2,3],[2,4],[2,5]]
#      lst:[2,3,4,5] i:1 n:2 m[1]:3 remLst:[4,5]
#           CALL combination. lst:[4,5], n:1 len:2
#           lst:[4,5] i:0 n:1 m[0]:4 remLst:[5]
#                CALL combination. lst:[5], n:0 len:1
#                RETURN combos:[[]]
#                remainlst_combo:[[]]
#                m:4 p:()
#                combos.append:[[4]]
#           lst:[4,5] i:1 n:1 m[1]:5 remLst:[]
#                CALL combination. lst:[], n:0 len:0
#                RETURN combos:[[]]
#                remainlst_combo:[[]]
#                m:5 p:()
#                combos.append:[[4],[5]]
#                RETURN combos: [[4],[5]]
#                     remainlst_combo:[[4],[5]]
#                     m:3 p:(4,)
#                     combos.append:[[2,3],[2,4],[2,5],[3,4]]
#                     m:3 p:(5,)
#                     combos.append:[[2,3],[2,4],[2,5],[3,4],[3,5]]
#      lst:[2,3,4,5] i:2 n:2 m[2]:4 remLst:[5]
#           CALL combination. lst:[5], n:1 len:1
#           lst:[5] i:0 n:1 m[0]:5 remLst:[]
#                CALL combination. lst:[], n:0 len:0
#                RETURN combos:[[]]
#                remainlst_combo:[[]]
#                m:5 p:()
#                combos.append:[[5]]
#                RETURN combos:[[5]]
#                     remainlst_combo:[[5]]
#                     m:4 p:(5,)
#                     combos.append:[[2,3],[2,4],[2,5],[3,4],[3,5],[4,5]]
#      lst:[2,3,4,5] i:3 n:2 m[3]:5 remLst:[]
#           CALL combination. lst:[], n:1 len:0
#                RETURN combos:[]
#                remainlst_combo:[]
#                RETURN combos:[[2,3],[2,4],[2,5],[3,4],[3,5],[4,5]]
#                     remainlst_combo:[[2,3],[2,4],[2,5],[3,4],[3,5],[4,5]]
#                     m:1 p:(2,3)
#                     combos.append:[[1,2,3]]
#                     m:1 p:(2,4)
#                     combos.append:[[1,2,3],[1,2,4]]
#                     m:1 p:(2,5)
#                     combos.append:[[1,2,3],[1,2,4],[1,2,5]]
#                     m:1 p:(3,4)
#                     combos.append:[[1,2,3],[1,2,4],[1,2,5],[1,3,4]]
#                     m:1 p:(3,5)
#                     combos.append:[[1,2,3],[1,2,4],[1,2,5],[1,3,4],[1,3,5]]
#                     m:1 p:(4,5)
#                     combos.append:[[1,2,3],[1,2,4],[1,2,5],[1,3,4],[1,3,5],[1,4,5]]
# lst:[1,2,3,4,5] i:1 n:3 m[1]:2 remLst:[3,4,5]
#      CALL combination. lst:[3,4,5], n:2 len:3
#      lst:[3,4,5] i:0 n:2 m[0]:3 remLst:[4,5]
#           CALL combination. lst:[4,5], n:1 len:2
#           lst:[4,5] i:0 n:1 m[0]:4 remLst:[5]
#           CALL combination. lst:[5], n:0 len:1
#           RETURN combos: [[]]
#           remainlst_combo:[[]]
#           m:4 p:()
#           combos.append:[[4]]
#           lst:[4,5] i:1 n:1 m[1]:5 remLst:[]
#           CALL combination. lst:[], n:0 len:0
#           RETURN combos:[[]]
#           remainlst_combo:[[]]
#           m:5 p:()
#           combos.append:[[4],[5]]
#           RETURN combos: [[4],[5]]
#                remainlst_combo:[[4],[5]]
#                m:3 p:(4,)
#                combos.append:[[3,4]]
#                m:3 p:(5,)
#                combos.append:[[3,4],[3, ]]
#      lst:[3,4,5] i:1 n:2 m[1]:4 remLst:[5]
#           CALL combination. lst:[5], n:1 len:1
#           lst:[5] i:0 n:1 m[0]:5 remLst:[]
#           CALL combination. lst:[], n:0 len:0
#           RETURN combos:[[]]
#           remainlst_combo:[[]]
#           m:5 p:()
#           combos.append:[[5]]
#           RETURN combos:[[5]]
#                remainlst_combo:[[5]] 
#                m:4 p:(5,)
#                combos.append:[[3,4],[3,5],[4,5]]
#      lst:[3,4,5] i:2 n:2 m[2]:5 remLst:[]
#           CALL combination. lst:[], n:1 len:0
#           RETURN combos:[]
#           remainlst_combo:[]
#           RETURN combos:[[3,4],[3,5],[4,5]]
#                remainlst_combo:[[3,4],[3,5],[4,5]]
#                m:2 p:(3,4)
#                combos.append:[[1,2,3],[1,2,4],[1,2,5],[1,3,4],[1,3,5],[1,4,5],[2,3,4]]
#                m:2 p:(3,5)
#                combos.append:[[1,2,3],[1,2,4],[1,2,5],[1,3,4],[1,3,5],[1,4,5],[2,3,4],[2,3,5]]
#                m:2 p:(4,5)
#                combos.append:[[1,2,3],[1,2,4],[1,2,5],[1,3,4],[1,3,5],[1,4,5],[2,3,4],[2,3,5],[2,4,5]]
# lst:[1,2,3,4,5] i:2 n:3 m[2]:3 remLst:[4,5] 
#      CALL combination. lst:[4,5], n:2 len:2
#      lst:[4,5] i:0 n:2 m[0]:4 remLst:[5]
#           CALL combination. lst:[5], n:1 len:1
#           lst:[5] i:0 n:1 m[0]:5 remLst:[]
#           CALL combination. lst:[], n:0 len:0
#           RETURN combos:[[]]
#           remainlst_combo:[[]]
#           m:5 p:()
#           combos.append:[[5]]
#           RETURN combos:[[5]]
#                remainlst_combo:[[5]]
#                m:4 p:(5,)
#                combos.append:[[4,5]]
#      lst:[4,5] i:1 n:2 m[1]:5 remLst:[]
#           CALL combination. lst:[], n:1 len:0
#           RETURN combos:[]
#           remainlst_combo:[]
#           RETURN combos:[[4,5]]
#                remainlst_combo:[[4,5]]
#                m:3 p:(4,5)
#                combos.append:[[1,2,3],[1,2,4],[1,2,5],[1,3,4],[1,3,5],[1,4,5],[2,3,4],[2,3,5],[2,4,5],[3,4,5]]
# lst:[1,2,3,4,5] i:3 n:3 m[3]:4 remLst:[5]
#      CALL combination. lst:[5], n:2 len:1
#      lst:[5] i:0 n:2 m[0]:5 remLst:[]
#           CALL combination. lst:[], n:1 len:0
#           RETURN combos:[]
#           remainlst_combo:[]
#           RETURN combos:[]
#                remainlst_combo:[]
# lst:[1,2,3,4,5] i:4 n:3 m[4]:5 remLst:[]
#      CALL combination. lst:[], n:2 len:0
#      RETURN combos:[]
#           remainlst_combo:[]
#           RETURN combos: [[1,2,3],[1,2,4],[1,2,5],[1,3,4],[1,3,5],[1,4,5],[2,3,4],[2,3,5],[2,4,5],[3,4,5]]
#
#
# ITERATIVE SOLUTION
# https://stackoverflow.com/questions/41694722/algorithm-for-itertools-combinations-in-python
def list_combinations(iterable, k):
  # pool is the total list of iterables
  pool = tuple(iterable)
  n = len(pool)
  if k > n:
    return
  # indices holds index combinations as list of lists
  indices = list(range(k)) # one index per for_loop
  yield tuple(pool[i] for i in indices)
  print(f"indices:{indices}")
  print(f"pool:{pool}")
  # while_loop increments index value at each position i
  while True:
    # for_loop traverses across index positions from back to front
    for i in reversed(range(k)):
      print(f"______________i:{i} indices[{i}]:{indices[i]}______________")
      # max position value for i in index list equals i+n-k
      if indices[i] != i + n - k:
        print(f"max (nesting): increment value at position {i}: {indices[i]} --> {indices[i]+1}")
        # break out of for_loop to increment value at position i
        break
      print(f"move to next i")
    else:
      # end while_loop after traversing all positions
      return
    # increment value at position i
    indices[i] += 1
    print(f"indices:{indices}")
    # reset all positions > i to 1 larger than previous position
    for j in range(i+1, k):
      indices[j] = indices[j-1] + 1
      print(f">>> reset:{indices} <<<")
    yield tuple(pool[i] for i in indices)

# combinations_list = list(list_combinations([0,1,2,3,4],3))
# print(combinations_list)
#
# 
#          [0,1,2,3,4]
#   /   |    |    |    |   \
# 012  023  034  123  134  234   <-- reset all positions >i when moving to next i 
# 013  024       124                 (+1 of previous position value)
# 014
#
#
# indices:[0, 1, 2]
# pool:(0, 1, 2, 3, 4)
# ______________i:2 indices[2]:2______________
# max (nesting): increment value at position 2: 2 --> 3
# indices:[0, 1, 3]
# ______________i:2 indices[2]:3______________
# max (nesting): increment value at position 2: 3 --> 4
# indices:[0, 1, 4]
# ______________i:2 indices[2]:4______________
# move to next i
# ______________i:1 indices[1]:1______________
# max (nesting): increment value at position 1: 1 --> 2
# indices:[0, 2, 4]
# >>> reset:[0, 2, 3] <<<
# ______________i:2 indices[2]:3______________
# max (nesting): increment value at position 2: 3 --> 4
# indices:[0, 2, 4]
# ______________i:2 indices[2]:4______________
# move to next i
# ______________i:1 indices[1]:2______________
# max (nesting): increment value at position 1: 2 --> 3
# indices:[0, 3, 4]
# >>> reset:[0, 3, 4] <<<
# ______________i:2 indices[2]:4______________
# move to next i
# ______________i:1 indices[1]:3______________
# move to next i
# ______________i:0 indices[0]:0______________
# max (nesting): increment value at position 0: 0 --> 1
# indices:[1, 3, 4]
# >>> reset:[1, 2, 4] <<<
# >>> reset:[1, 2, 3] <<<
# ______________i:2 indices[2]:3______________
# max (nesting): increment value at position 2: 3 --> 4
# indices:[1, 2, 4]
# ______________i:2 indices[2]:4______________
# move to next i
# ______________i:1 indices[1]:2______________
# max (nesting): increment value at position 1: 2 --> 3
# indices:[1, 3, 4]
# >>> reset:[1, 3, 4] <<<
# ______________i:2 indices[2]:4______________
# move to next i
# ______________i:1 indices[1]:3______________
# move to next i
# ______________i:0 indices[0]:1______________
# max (nesting): increment value at position 0: 1 --> 2
# indices:[2, 3, 4]
# >>> reset:[2, 3, 4] <<<
# >>> reset:[2, 3, 4] <<<
# ______________i:2 indices[2]:4______________
# move to next i
# ______________i:1 indices[1]:3______________
# move to next i
# ______________i:0 indices[0]:2______________
# move to next i
# [(0, 1, 2), (0, 1, 3), (0, 1, 4), (0, 2, 3), (0, 2, 4), (0, 3, 4), (1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]

   
####################################

# https://docs.python.org/3/library/itertools.html#itertools.combinations
# Without for-else & using lst indices 
def find_combos(lst,k): # k is number of edges/splits per combination
  combinations_list = []
  n = len(lst)
  if k > n:
    return combinations_list
  indices = list(range(k)) # one index per for_loop
  combo = list(lst[i] for i in indices)
  combinations_list.append(combo)
  while True:
    max_reached = True
    for i in reversed(range(k)):
      if indices[i] != i + n - k:
        max_reached = False
        break
    if max_reached:
      return combinations_list
    indices[i] += 1
    for j in range(i+1, k):
      indices[j] = indices[j-1] + 1
    combos = list(lst[l] for l in indices)
    combinations_list.append(combos)
  return combinations_list

combinations_output = find_combos(['a','b','c','d','e'],3)
print(combinations_output)
# 'abc', 'abd', 'abe', 'acd', 'ace', 'ade', 'bcd', 'bce', 'bde', 'cde'

# Without for-else & using integers
# https://docs.python.org/3/library/itertools.html#itertools.combinations
def find_combos(lst,k): # k is number of edges/splits per combination
  combinations_list = []
  n = len(lst)
  if k > n:
    return combinations_list
  indices = list(range(k)) # one index per for_loop
  combinations_list.append(indices.copy())
  while True:
    max_reached = True
    for i in reversed(range(k)):
      if indices[i] != i + n - k:
        max_reached = False
        break
    if max_reached:
      return combinations_list
    indices[i] += 1
    for j in range(i+1, k):
      indices[j] = indices[j-1] + 1
    combinations_list.append(indices.copy())
  return combinations_list

combos_list = find_combos([0,1,2,3,4],3)
print(combos_list)
# 012, 013, 014, 023, 024, 034, 123, 124, 134, 234