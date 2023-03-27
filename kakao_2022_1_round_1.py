'''

kakao 2022 new recruitment test

https://tech.kakao.com/2022/01/14/2022-kakao-recruitment-round-1/

Problem 1

'''


id_lists = [
  ["muzi", "frodo", "apeach", "neo"],
  ["con", "ryan"]
]

reports = [
  ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],
  ["ryan con", "ryan con", "ryan con", "ryan con"],
]

ks = [
  2,
  3
]

expected_results = [
  [2,1,1,0],
  [0,0]
]

# build dictionary using reported user id as unique key
def get_reported_ids(report):
  report_ids = {}
  for id in report:
    alert = id.split()
    if alert[1] in report_ids and alert[0] not in report_ids[alert[1]]:
      report_ids[alert[1]].append(alert[0])
    else:
      report_ids[alert[1]] = [alert[0]]
  return report_ids

def get_suspended_ids(id_list, report, k):
  suspended_ids = []
  number_of_reports = [0] * len(id_list)
  # get all ids with reports
  reported_ids = get_reported_ids(report)
  # identify all ids with k reports that qualify for suspension
  for suspended_id in reported_ids:
    if len(reported_ids[suspended_id]) >= k:
      # combine lists of suspended accounts into one suspended_ids list 
      suspended_ids += reported_ids[suspended_id]
  # count number of ids from id_list in suspened_id list and add to number_of_reports list
  for index, report_id in enumerate(id_list):
    if report_id in suspended_ids:
      number_of_reports[index] = suspended_ids.count(report_id)
  return number_of_reports

for test_index in range(len(id_lists)):
  # if test_index == 0:
    id_list = id_lists[test_index]
    report = reports[test_index]
    k = ks[test_index]
    
    result = get_suspended_ids(id_list,report,k)
    expected_result = expected_results[test_index]
    print(f"test {test_index}: ", end="")
    if result == expected_result:
      print("pass")
    else:
      print(f"fail (expected {expected_result}, but got {result})")
