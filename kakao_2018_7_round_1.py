'''

kakao 2018 new recruitment test

https://tech.kakao.com/2017/09/27/kakao-blind-recruitment-round-1/

Problem 7

'''

parameters = [
  {
    "lines": ["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]
  },
  {
    "lines": ["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]
  }
]

expected_results = [
  1,
  2
]

def solution(lines):
  times = []
  answer = 0
  for line in lines:
    time = line[11:23]  # 그냥 시간 데이터
    hour = int(time[:2])    # 시, 분, 초 로 나눔.
    minute = int(time[3:5])
    second = float(time[6:12])

    end_time = hour * 10000 + minute * 100 + second
    T = float(line[24:-1])    # 처리시간 T
    start_sec = round(second - T , 3) + 0.001 # 시작 시간 구함

    if start_sec < 0:
      minute -= 1
      start_sec += 60
      if minute < 0:
        hour -= 1
        minute += 60
    start_time = hour * 10000 + minute * 100 + start_sec
    times.append([start_time,end_time])
 # times : [(시작시간 시,분,초), (종료시간 시,분,초)] 로 이루어진 배열

  for i in range(len(times)):
    init_start_time = times[i][0]
    plus_one = init_start_time + 1
    count = 0

    for time in times:
      if init_start_time <= time[0] < plus_one or init_start_time <= time[1] < plus_one:
        count += 1
      elif time[0] < init_start_time < plus_one < time[1]:
        count += 1

    answer = max(count,answer)
  print(times)

  for i in range(len(times)):
    init_end_time = times[i][1]
    plus_one = init_end_time + 1
    count = 0

    for time in times:
      if init_end_time <= time[0] < plus_one or init_end_time <= time[1] < plus_one:
        count += 1
      elif time[0] < init_end_time < plus_one < time[1]:
        count += 1
    answer = max(count, answer)
  return answer

def problem(**kwargs):
  lines = kwargs["lines"]

  result = solution(lines)
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

