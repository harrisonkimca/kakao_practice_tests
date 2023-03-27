# string = "aabbaccc"
# string = "ababcdcdababcdcd"
# string = "abcabcdede"
string = "abcabcabcabcdededededede"
# string = "xababcdcdababcdcd"

# compare characters in string in 1, 2s, 3s...n/2
def compare_string_characters(string):
  print(f"string: {string} len: {len(string)}")
  # parse string in 2s, 4s, 6s...
  for cut_length in range(1, len(string)):
    cut_location = cut_length
    previous = string[:cut_length]
    while cut_location + cut_length <= len(string):
      print(f"cut_length: {cut_length} compare: {previous} to: {string[cut_location:cut_location + cut_length]}")
      if previous == string[cut_location:cut_location + cut_length]:
        print("same")
      else:
        print("different")
      
      previous = string[cut_location:cut_location + cut_length]
      cut_location += cut_length


# compare characters in string in 1, 2s, 3s...n/2
# and compress string by replacing replicated characters by int
def get_best_compression(string):
  print(f"string: {string} len: {len(string)}")
  best_compression = string
  # cut string into 1s, 2s, 3s...n/2 (cut = number of characters)
  # to check for matching characters 
  for cut_length in range(1, len(string)):
    # move accross string in 1s, 2s, 3s... (ie, cut)
    current_cut_location = cut_length
    # set first group of characters to check duplicates against 
    match = string[:cut_length]
    count = 1
    compression_string = ""
    # loop until end of string reached
    while current_cut_location + cut_length <= len(string):
      # increment count while parsed character identical to previous...
      if match == string[current_cut_location:current_cut_location + cut_length]:
        count += 1
      # ...once parsed character fails to match...
      else:
        # ...if more than one character matches then concatenate
        # count to string (after converting to string)
        if count > 1:
          compression_string += str(count)
        # ...concatenate count to bef...  
        compression_string += match
        print(f"cut_length: {cut_length} compressed_string: {compression_string}")
        # ...reset count to 1 for next parsing...
        count = 1
        # ...reset bef to current non-identical character
        match = string[current_cut_location:current_cut_location + cut_length]
          
      # advance to next charter in string
      current_cut_location += cut_length
    # last character cannot be checked so do separate check... 
    if count > 1:
      compression_string += str(count)
    compression_string += string[current_cut_location - cut_length:]
    # ...and store compressed string if shorter than previous string
    if len(compression_string) < len(best_compression):
      best_compression = compression_string

  return len(best_compression), best_compression


# compare_string_characters(string)
string_length, compression = get_best_compression(string)
print(f"length: {string_length} best_compression: {compression}")