'''

kakao 2022 new recruitment test

https://tech.kakao.com/2022/01/14/2022-kakao-recruitment-round-1/

Problem 2

'''


ns = [
  437674,
  110011
]

ks = [
  3,
  10
]

expected_results = [
  3,
  2
]

# convert n to base k
def get_base(n,k):
  new_num = ''
  while n > 0:
    new_num = str(n % k) + new_num
    n //= k
  return new_num

# check if number snippet is a prime number or composite number
# (brute force divides every number until divisor found)
def is_composite(num_str):
  if int(num_str) == 1:
    return True
  for i in range(2,int(num_str)):
    if (int(num_str) % i) == 0:
      return False

# finds all primes smaller or equal to n
# https://www.geeksforgeeks.org/python-program-for-sieve-of-eratosthenes/
def SieveOfEratosthenes(num):
  # boolean array
  prime = [True for i in range(int(num)+1)]
  
  p = 2
  while (p * p <= int(num)):
    # if prime[p] is not changed then it is a prime
    if (prime[p] == True):
      # updating all multiples of p
      for i in range(p * p, int(num)+1, p):
        prime[i] = False
    p += 1
  
  # add all primes to check_primes list
  check_primes = []
  for p in range(2, int(num)+1):
    if prime[p]:
      check_primes.append(p)
  return check_primes


def get_prime_numbers(n, k):
  count = 0
  num = get_base(n,k)
  numbers = num.split('0')
  # remove empty strings from 'split' list
  clean_numbers = [ tok for tok in numbers if tok ]

  # *** brute force to check for primes
  # for number in clean_numbers:
  #   if not is_composite(number):
  #     count += 1

  # *** sieve of eratosthenes to check for primes
  for number in clean_numbers:
    check = SieveOfEratosthenes(number)  
    for prime in check:
      if prime == int(number):
        count += 1
  
  return count

for test_index in range(len(ns)):
  # if test_index == 0:
    n = ns[test_index]
    k = ks[test_index]
    
    result = get_prime_numbers(n,k)
    expected_result = expected_results[test_index]
    print(f"test {test_index}: ", end="")
    if result == expected_result:
      print("pass")
    else:
      print(f"fail (expected {expected_result}, but got {result})")
