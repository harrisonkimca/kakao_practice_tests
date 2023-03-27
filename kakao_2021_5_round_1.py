'''

kakao 2021 new recruitment test

https://tech.kakao.com/2021/01/25/2021-kakao-recruitment-round-1/

Problem 5

'''

parameters = [
  {
    "play_time": "00:00:10",
    "adv_time": "00:00:04",
    "log": [
      "00:00:01-00:00:03", 
      "00:00:02-00:00:05", 
      "00:00:04-00:00:07", 
      "00:00:06-00:00:07", 
      "00:00:08-00:00:10"
    ]
  },{
    "play_time": "00:01:40",
    "adv_time": "00:00:10",
    "log": [
      "00:00:15-00:00:20", 
      "00:00:17-00:00:25", 
      "00:00:30-00:00:35", 
      "00:00:32-00:00:45", 
      "00:00:34-00:00:50"
    ]
  },{
    "play_time": "02:03:55",
    "adv_time": "00:14:15",
    "log": [
      "01:20:15-01:45:14", 
      "00:40:31-01:00:00", 
      "00:25:50-00:48:29", 
      "01:30:59-01:53:29", 
      "01:37:44-02:02:30"
    ]
  },{
    "play_time": "99:59:59",
    "adv_time": "25:00:00",
    "log": [
      "69:59:59-89:59:59", 
      "01:00:00-21:00:00", 
      "79:59:59-99:59:59", 
      "11:00:00-31:00:00"
    ]
  },{
    "play_time": "50:00:00",
    "adv_time": "50:00:00",
    "log": [
      "15:36:51-38:21:49", 
      "10:14:18-15:36:51", 
      "38:21:49-42:51:45"
    ]
  }
]

expected_results = [
  "00:00:01",
  "00:00:31",
  "01:30:59",
  "01:00:00",
  "00:00:00"
]

def convert_to_seconds(time):
  hour,min,sec = time.split(":")
  hour_sec = int(hour) * 60 * 60
  min_sec = int(min) * 60
  time_sec = hour_sec + min_sec + int(sec)
  
  return time_sec

def convert_log_to_seconds(log):
  log_sec = []
  for entry in log:
    time = entry.split("-")
    start = time[0]
    end = time[1]
    
    start_sec = convert_to_seconds(start)
    end_sec = convert_to_seconds(end)
    log_sec.append((start_sec,end_sec))

  return log_sec

def convert_to_hms(time):
  time = time % (24 * 3600) # time does not exceed one day
  hours = time//(60*60) # '//' floor division
  minutes = time % (60*60)//60 # find remaining seconds and convert to minutes
  seconds = time % 60 # find remaining seconds
  
  return "%02d:%02d:%02d" % (hours, minutes, seconds)

# brute force method to find number of viewers at each second of play_time
def find_best_start_time_brute_force(play_time, adv_time, log_sec):
  max_viewership = 0
  viewership = []
  start = 0
  # count viewers at each second of play_time
  for sec in range(play_time - adv_time): # KEEP MAIN LOOP AS BRUTE FORCE
    viewers = 0
    # increment counter if second falls between start and end time of each log
    for log in log_sec: ## NESTED LOOP BAD FOR EFFICIENCY
      if sec >= log[0] and sec <= log[1]:
        viewers += 1
    # print(f"sec: {sec} viewers: {viewers}")
    # add viewers to list covering range of adv_time
    if len(viewership) < adv_time:
      viewership.append(viewers)
    # remove first element to keep range of adv_time
    else:
      viewership.pop(0)
      viewership.append(viewers)
    # sum viewership across the range of adv_time
    if len(viewership) == adv_time:
      viewership_total = sum(viewership) ## SUM HIDDEN LOOP ALSO BAD FOR EFFICIENCY
      # find best start time based on max_viewership
      if viewership_total > max_viewership:
        max_viewership = viewership_total
        start = sec - adv_time
        # print(f"{sec}. start: {start} MAX: {max_viewership}")
  return start

def find_best_start_time_efficient(play_time, adv_time, log_sec):

  # 0 1 2 3 4 5 6 7 8 9
  #   x x
  #     x x x
  #         x x x
  #             x
  #                 x x
  # 0 1 2 1 2 1 2 0 1 1
  
  # use list index to represent each second of play_time
  viewer_list = [0] * play_time
  # make list of start (switch tv on) and end (switch tv off) times
  for log in log_sec:
    # increase viewers for each start time in log
    viewer_list[log[0]] += 1
    # decrease viewers for each end time in log
    if log[1] < play_time-1:
      viewer_list[log[1]] -= 1
  # view_list represents array of switch on and switch off
  # print(f"viewer_list: {viewer_list}")

  # use viewer_list to generate list of number of viewers at each second of play_time
  viewership_list = [0] * play_time
  # viewer_list avoids nested loop to improve effficiency
  for i, sec in enumerate(viewer_list):
    if i == 0:
      viewership_list[i] += sec
    else:
      viewership_list[i] += viewership_list[i-1] + sec
  # viewership_list represents number of viewers at each second of play_time
  # print(f"viewership_list: {viewership_list}")

  # use viewship_list to generate list of cumulative total of user at each second of play_time
  best_list = [0] * play_time
  # best_list can be generated in separate loop to avoid nested loop
  for j, viewers in enumerate(viewership_list):
    if j == 0:
      best_list[j] += viewers
    else:
      best_list[j] += best_list[j-1] + viewers
  # print(f"best_list: {best_list}")

  # use list indexes to avoid nested loop and inefficient sum function
  max_viewership = 0
  start = 0
  for k, best_time in enumerate(best_list):
    if k >= (adv_time-1):
      # print(f"best_list[{k}] - best_list[{k-(adv_time-1)}] = {best_list[k]-best_list[k-(adv_time-1)]}")
      if best_list[k] - best_list[k-(adv_time-1)] > max_viewership:
        max_viewership = best_list[k] - best_list[k-(adv_time-1)]
        start = k-(adv_time-1)
        # print(f"max_viewership: {max_viewership} start: {start}")
  return start    

def problem(**kwargs):
  play_time = kwargs["play_time"]
  adv_time = kwargs["adv_time"]
  log = kwargs["log"]

  log_sec = convert_log_to_seconds(log)
  play_sec = convert_to_seconds(play_time)
  adv_sec = convert_to_seconds(adv_time)

  # start = find_best_start_time_brute_force(play_sec, adv_sec, log_sec)
  # start_hms = convert_to_hms(start)
  # print(f"start: {start} start_hms: {start_hms}")

  start = find_best_start_time_efficient(play_sec, adv_sec, log_sec)
  start_hms = convert_to_hms(start)
  print(f"start: {start} start_hms: {start_hms}")

  return start_hms

for test_index in range(len(expected_results)): 
  # if test_index == 0:
    result = problem(**parameters[test_index])
    expected_result = expected_results[test_index]
    print(f"test {test_index}: ", end="")
    if result == expected_result:
      print("pass")
    else:
      print(f"fail (expected {expected_result}, but got {result})")