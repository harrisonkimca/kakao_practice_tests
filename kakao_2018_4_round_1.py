'''

kakao 2017 new recruitment test

https://tech.kakao.com/2017/09/27/kakao-blind-recruitment-round-1/#4-%EC%85%94%ED%8B%80%EB%B2%84%EC%8A%A4%EB%82%9C%EC%9D%B4%EB%8F%84-%EC%A4%91

Problem 4

'''

parameters = [
  {
    "n": 1,
    "t": 1,
    "m": 5,
    "time_table": [
      "08:00", 
      "08:01", 
      "08:02", 
      "08:03"
    ]
  },{
    "n": 2,
    "t": 10,
    "m": 2,
    "time_table": [
      "09:10", 
      "09:09", 
      "08:00"
    ]
  },{
    "n": 2,
    "t": 1,
    "m": 2,
    "time_table": [
      "09:00", 
      "09:00", 
      "09:00", 
      "09:00"
    ]
  },{
    "n": 1,
    "t": 1,
    "m": 5,
    "time_table": [
      "00:01", 
      "00:01", 
      "00:01", 
      "00:01", 
      "00:01"
    ]
  },{
    "n": 1,
    "t": 1,
    "m": 1,
    "time_table": [
      "23:59"
    ]
  },{
    "n": 10,
    "t": 60,
    "m": 45,
    "time_table": [
      "23:59",
      "23:59", 
      "23:59", 
      "23:59", 
      "23:59", 
      "23:59", 
      "23:59", 
      "23:59", 
      "23:59", 
      "23:59", 
      "23:59", 
      "23:59", 
      "23:59", 
      "23:59", 
      "23:59", 
      "23:59"
    ]
  },{
    "n": 3,
    "t": 10,
    "m": 1,
    "time_table": [
      "09:00",
      "09:11",
      "09:20"
    ]
  }
]

expected_results = [
  "09:00",
  "09:09",
  "08:59",
  "00:00",
  "09:00",
  "18:00",
  "09:10"
]

from datetime import datetime, timedelta

def find_latest_arrival_time(n, t, m, time_table):
  # convert to datetime objects
  start_time = datetime.strptime("09:00", '%H:%M')
  sleep_time = datetime.strptime("23:59", '%H:%M')
  # find time of last shuttle
  last_shuttle = (n-1) * t
  last_shuttle_time = start_time + timedelta(minutes=(last_shuttle))

  # convert time_table to datetime and sort by date
  passengers = []
  for time in time_table:
    passenger = datetime.strptime(time, '%H:%M')
    passengers.append(passenger)
  sorted_passengers = sorted(passengers)
  
  # early termination (ie, all seats available so shuttle time irrelevant)
  if m > len(sorted_passengers):
    dt_latest_arrival_time = last_shuttle_time
    str_latest_arrival_time = dt_latest_arrival_time.strftime('%H:%M')
    return str_latest_arrival_time

  # find the number of waiting passengers for the last shuttle
  # by removing waiting passengers that board earlier shuttles
  for i in range(n-1):
    shuttle = i * t
    shuttle_time = start_time + timedelta(minutes=shuttle)
    for j in range(m):
      if sorted_passengers[j] <= shuttle_time:
        sorted_passengers.pop(j)
  
  # if no seats available...
  if len(sorted_passengers) >= m:
    # ...find arrival time of last empty seat...
    cutoff_time = sorted_passengers[m-1]
    # ...if cutoff time is 23:59 then return tomorrow start time...
    if cutoff_time >= sleep_time:
      dt_latest_arrival_time = start_time
      str_latest_arrival_time = dt_latest_arrival_time.strftime('%H:%M')
      return str_latest_arrival_time
    # ...if not then arrive one-minute before last empty seat...
    else:
      dt_latest_arrival_time = cutoff_time - timedelta(minutes=1)
      str_latest_arrival_time = dt_latest_arrival_time.strftime('%H:%M')
      return str_latest_arrival_time
  # if seats available...
  else:
    # ...can arrive when the last shuttle leaves...
    dt_latest_arrival_time = last_shuttle_time
    str_latest_arrival_time = dt_latest_arrival_time.strftime('%H:%M')
    return str_latest_arrival_time


def problem(**kwargs):
  n = kwargs["n"]
  t = kwargs["t"]
  m = kwargs["m"]
  time_table = kwargs["time_table"]

  latest_arrival_time = find_latest_arrival_time(n, t, m, time_table)
  
  return latest_arrival_time

for test_index in range(len(expected_results)): 
  # if test_index == 0:
    result = problem(**parameters[test_index])
    expected_result = expected_results[test_index]
    print(f"test {test_index}: ", end="")
    if result == expected_result:
      print("pass")
    else:
      print(f"fail (expected {expected_result}, but got {result})")

