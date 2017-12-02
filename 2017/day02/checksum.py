def get_min_max_checksum(list_numbers):
  if len(list_numbers) < 2:
    return 0
  sorted_numbers = sorted(list_numbers)
  return sorted_numbers[-1] - sorted_numbers[0]

def evenly_divisible_checksum(list_numbers):
  if len(list_numbers) < 2:
    return 0
  sorted_numbers = sorted(list_numbers, reverse=True)
  for i, num in enumerate(sorted_numbers[:-1]):
    max_divisor = num / 2
    left_to_check = [n for n in sorted_numbers[i + 1:] if n == num or n <= max_divisor]
    for divisor in left_to_check:
      if num % divisor == 0:
        return num / divisor
  return 0

def split_row(input_row):
  list_numbers = []
  tmp_number = ''
  for i in input_row:
    if i.isdigit():
      tmp_number += i
    else:
      if len(tmp_number):
        list_numbers.append(int(tmp_number))
        tmp_number = '' 
  if len(tmp_number):
    list_numbers.append(int(tmp_number))     
  return list_numbers

def get_checksum(input_string, checksum_fn):
  rows = input_string.split('\n')
  int_rows = [split_row(row) for row in rows]
  checksums = [checksum_fn(row) for row in int_rows]
  return sum(checksums)

def checksum_from_file(file_name, checksum_fn):
  input_string = ''
  with open(file_name) as f:
    input_string = f.read()
  return get_checksum(input_string, checksum_fn)
