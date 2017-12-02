def inverse_captcha_by_step(input_code, step):
  list_numbers = [int(i) for i in input_code]
  cumulative_sum = 0
  if len(list_numbers) < 2:
    return cumulative_sum
  list_numbers += list_numbers[0:step]
  zip_list = zip(list_numbers[:-step], list_numbers[step:])
  for (a, b) in zip_list:
    if a == b:
      cumulative_sum += a
  return cumulative_sum

def inverse_captcha(input_code):
  return inverse_captcha_by_step(input_code, 1)

def inverse_captcha_halfway(input_code):
  return inverse_captcha_by_step(input_code, len(input_code)/2)
  
