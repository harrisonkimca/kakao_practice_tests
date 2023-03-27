'''

kakao 2019 new recruitment test

https://tech.kakao.com/2018/09/21/kakao-blind-recruitment-for2019-round-1/

Problem 6

'''

parameters = [
  {
    "word": "blind",
    "pages": ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n <meta charset=\"utf-8\">\n <meta property=\"og:url\" content=\"https://a.com\"/>\n</head> \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n <meta charset=\"utf-8\">\n <meta property=\"og:url\" content=\"https://b.com\"/>\n</head> \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n <meta charset=\"utf-8\">\n <meta property=\"og:url\" content=\"https://c.com\"/>\n</head> \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]
  },
  {
    "word": "muzi",
    "pages": ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n <meta charset=\"utf-8\">\n <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head> \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n <meta charset=\"utf-8\">\n <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head> \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]
  }
]

expected_results = [
  0,
  1
]

import re

def solution(word, pages):
  answer = 0
  link_counts = []  # number of external links
  normal_counts = []  # base score
  link_idx = {}  # index value per link
  idx_link = {}
  linkToLink = [[] for _ in range(21)]
  word = word.lower()  # compare only lower case letters

  # base score
  for k in range(len(pages)):
    page = pages[k]
    word_len = len(word)
    score = 0
    for i in range(len(page) - word_len):
      if page[i].lower() == word[0]:  # when first letter the same...
        if 'a' <= page[i - 1].lower() <= 'z':  # ...if consecutive characters in front of
          continue
        is_same = True
        for j in range(word_len):
          if word[j] != page[i + j].lower():
            is_same = False
            break
        if is_same:
          if 'a' <= page[i + word_len].lower() <= 'z':  # if consecutive characters after
            continue
          else:
            score += 1  # base score + 1
            continue
    normal_counts.append(score)

  for k in range(len(pages)):
    page = pages[k]
    real_link = re.search(r'(<meta property.+content=")(https://.*)"/>', page).group(2)  # search current url
    link_idx[k] = real_link  # store both link-index and index-link
    idx_link[real_link] = k

  # get link score
  for k in range(len(pages)):
    page = pages[k]
    real_link = re.findall(r'<a href="https://\S*">', page)  # search all external link urls
    link_counts.append(len(real_link))
    for link in real_link:
      l = link[9:-2]
      print(l)
      if l in idx_link:
        idx = idx_link[l]  # index number of linked link
        linkToLink[idx].append(k)

  scores = []
  for i in range(len(pages)):
    link_score = 0
    if len(linkToLink[i]) != 0:
      for idx in linkToLink[i]:  # links leading to this link
        link_score += normal_counts[idx] / link_counts[idx]
    scores.append(link_score + normal_counts[i])

  max_score = max(scores)
  for i in range(len(pages)):
    if scores[i] == max_score:
      answer = i
      break

  return answer

'''
# I don't know why I can't pass only 10 Tekke.
def solution_2(word, pages):
  answer = 0
  link_counts = []  # number of external links
  normal_counts = []  # base score
  link_idx = {}  # index value per link
  idx_link = {}
  linkToLink = [[] for _ in range(21)]
  word = word.lower()  # compare only lower case letters

  # base score
  for k in range(len(pages)):
    page = pages[k]
    word_len = len(word)
    is_tag = False
    score = 0
    for i in range(len(page) - word_len):
      if page[i] == '<':  # <~~~~> is the text inside the tag
        is_tag = True
      if page[i] == '>':
        is_tag = False
      if not is_tag:  # unless it is in the tag
        if page[i].lower() == word[0]:  # when the first letter is the same...
          if 'a' <= page[i - 1].lower() <= 'z':  # ...if consecutive characters in front of
            continue
          is_same = True
          for j in range(word_len):
            if word[j] != page[i + j].lower():
              is_same = False
              break
          if is_same:
            if 'a' <= page[i + word_len].lower() <= 'z':  # if consecutive characters after
              continue
            else:
              score += 1  # base score + 1
              continue
    normal_counts.append(score)

  for k in range(len(pages)):
    page = pages[k]
    string = page.split(' ')  # split by space
    find_url = False  # you need to find it in the meta value first
    # get a link to this webpage
    for p in string:
        if find_url:
            break
        if "content" in p and not find_url:
          new_link = p[9:]
          # Get Link
          for i in range(len(new_link) - 2):
            if new_link[i] == '\"' and new_link[i + 1] == "/" and new_link[i + 2] == ">":
              real_link = new_link[:i]
              if real_link in idx_link:  # after adding this, it passed 9 times
                continue
              link_idx[k] = real_link  # store both link-index and index-link
              idx_link[real_link] = k
              find_url = True
              break

  # get link score
  for k in range(len(pages)):
    page = pages[k]
    link_count = 0  # number of external links
    string = page.split(' ')  # split by space
    for p in string:
      if "href" in p:
        new_link = p[6:]
        # connect the link
        for i in range(len(new_link)):
          if new_link[i] == '\"' and new_link[i + 1] == ">":
            real_link = new_link[:i] # Links on this web page
            link_count += 1
            if real_link not in idx_link:
              break
            idx = idx_link[real_link]  # Index number of linked link
            if k in linkToLink[idx]:
              break
            linkToLink[idx].append(k)
    link_counts.append(link_count)  # Link count by index

  scores = []
  for i in range(len(pages)):
    link_score = 0
    if len(linkToLink[i]) != 0:
      for idx in linkToLink[i]:  # links leading to this link
        link_score += normal_counts[idx] / link_counts[idx]
    scores.append(link_score + normal_counts[i])

  max_score = max(scores)

  for i in range(len(pages)):
    if scores[i] == max_score:
      answer = i
      break

  print(scores)
  return answer
'''

def problem(**kwargs):
  word = kwargs["word"]
  pages = kwargs["pages"]

  result = solution(word, pages)
  # result = solution_2(word, pages)
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

