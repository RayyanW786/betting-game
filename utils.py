def is_even(num: int) -> bool:
  if num % 2 == 0:
    return True
  else:
    return False
    
def is_prime(num: int) -> bool:
  flag = False
  if num <= 1:
    return False

  for i in range(2, num):
    if (num % i) == 0:
      flag = True
      break

  if flag:
    return False
  else:
    return True

def is_multiple_10(num: int) -> bool:
  if num % 10 == 0:
    return True
  else:
    return False