'''

kakao 2020 new recruitment test

https://tech.kakao.com/2019/10/02/kakao-blind-recruitment-2020-round1/

Problem 4

'''

parameters = [
  {
    "words": [
      "frodo",
      "front",
      "frost",
      "frozen",
      "frame",
      "kakao"
    ],
    "queries": [
      "fro??",
      "????o",
      "fr???",
      "fro???",
      "pro?"
    ]
  }
]

expected_results = [
  [3, 2, 4, 1, 0]
]


class Node:
  def __init__(self, key):
    self.key = key
    self.children = {}  # connect the nodes below
    self.count = 0 # Check how many words there are down here in case a wild card comes after this.

class Trie:
  def __init__(self):
    self.head = Node(None)
    self.count = 0

  def insert(self, string):
    current_node = self.head
    for char in string:
      current_node.count += 1
      if char not in current_node.children:   # When abc comes in, put b below if b is not in child.
        current_node.children[char] = Node(char)
      current_node = current_node.children[char]

  def isin(self, string):
    current_node = self.head
    for char in string:
      if char not in current_node.children:
        return False
      current_node = current_node.children[char]
    return True

  def search(self, string):   # Find it on the premise that there is.
    current_node = self.head
    for char in string:
      current_node = current_node.children[char]
    return current_node.count

  def total(self):    # Total number of strings in a trie of this length
    current_node = self.head
    for key in current_node.children:
      print(key)
      self.count += current_node.children[key].count

def solution(words, queries):
  # How to divide a trie by length?
  front_trie = {}
  back_trie = {}
  for word in words:  # Insert character into trie
    word_len = len(word)
    if word_len not in front_trie:
      front_trie[word_len] = Trie()
      back_trie[word_len] = Trie()
    front_trie[word_len].insert(word)
    back_trie[word_len].insert(word[::-1])

  # Update total number of strings by length
  for key in front_trie:
    front_trie[key].total()
    back_trie[key].total()

  answer = []
  for query in queries:
    query_len = len(query)
    if query_len not in front_trie:
      answer.append(0)
      continue
    if query[0] == '?': # If the first character is a wildcard
      reversed_query = query[::-1].split('?')[0]
      if reversed_query == '':   # If the entire query is just a wildcard
        answer.append(back_trie[query_len].count)
      else:
        if back_trie[query_len].isin(reversed_query):
          answer.append(back_trie[query_len].search(reversed_query))
        else:
          answer.append(0)

    elif query[-1] == '?':  # If the last character is a wild card
      front_query = query.split('?')[0]
      if front_trie[query_len].isin(front_query):
        answer.append(front_trie[query_len].search(front_query))
      else:
        answer.append(0)
    else: # That's full text
      if front_trie[query_len].isin(query):
        answer.append(1)
      else:
        answer.append(0)
            
  return answer

def problem(**kwargs):
  words = kwargs["words"]
  queries = kwargs["queries"]

  result = solution(words, queries)
  return result

for test_index in range(len(expected_results)): 
  # if test_index == 0:
    result = problem(**parameters[test_index])
    expected_result = expected_results[test_index]
    print(f"test {test_index}: ", end="")
    if result == expected_result:
      print("pass")
    else:
      print(f"fail (expected {expected_result}, but got {result})")

