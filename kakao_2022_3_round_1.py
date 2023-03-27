'''

kakao 2022 new recruitment test

https://tech.kakao.com/2022/01/14/2022-kakao-recruitment-round-1/

Problem 3

'''


fees = [
  [180, 5000, 10, 600],
  [120, 0, 60, 591],
  [1, 461, 1, 10]
]

records = [
  ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"],
  ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"],
  ["00:00 1234 IN"]
]

expected_results = [
  [14600, 34400, 5000],
  [0, 591],
  [14841]
]


def make_logs(record):
  in_time = {}
  out_time = {}
  for entry in record:
    log = entry.split(' ')
    time = log[0].split(':')
    minutes = (int(time[0]) * 60) + int(time[1])
    if 'IN' in entry:
      if log[1] in in_time:
        in_time[log[1]].append(minutes)
      else:
        in_time[log[1]] = [minutes]
    elif 'OUT' in entry:
      if log[1] in out_time:
        out_time[log[1]].append(minutes)
      else:
        out_time[log[1]] = [minutes]
        
  return in_time, out_time

def get_parking_fees(fee, record):
  # daily max time (23:59)
  out_timestamp_max = 60 * 24 - 1
  # build dictionary using license plate numbers as keys
  in_time, out_time = make_logs(record)
  # assign fees to variables for clearer code
  default_time = fee[0]
  basic_fee = fee[1]
  unit_time = fee[2]
  unit_fee = fee[3]
  
  # assign all parking fees from each car to list and return list
  parking_fees = []

  # use in_time dictionary to select keys
  for key in sorted(in_time.keys()):
    total_time = 0
    total_fee = 0
    # loop through in_time and out_time dictionaries to match up in and out times
    for index, times in enumerate(in_time[key]):
      # assume that out_time only recorded when car leaves parking lot
      if key in out_time:
        if index < len(out_time[key]):
          out_timestamp = out_time[key][index]
        else:
          out_timestamp = out_timestamp_max
      # must include condition if car stays in parking lot after midnight (eg, case 3)
      else:
        out_timestamp = out_timestamp_max

      time = out_timestamp - in_time[key][index]
      total_time += time
    
    # use total parking time throughout the day to calculate parking total parking fees
    if total_time - default_time < 0:
      car_fee = basic_fee
      total_fee += int(car_fee)
    else:
      extra_time = total_time - default_time
      # round up for any time adjusted for the unit time
      rounded_time = int(extra_time/unit_time) + ((total_time % unit_time) > 0)
      car_fee = basic_fee + (rounded_time * unit_fee)
      total_fee += int(car_fee)
      
    parking_fees.append(total_fee)
    
  return parking_fees


for test_index in range(len(fees)):
  # if test_index == 2:
    fee = fees[test_index]
    record = records[test_index]
    
    result = get_parking_fees(fee,record)
    expected_result = expected_results[test_index]
    print(f"test {test_index}: ", end="")
    if result == expected_result:
      print("pass")
    else:
      print(f"fail (expected {expected_result}, but got {result})")
