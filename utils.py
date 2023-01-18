import json
from typing import Optional, Union
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
  return flag
#   if flag:
#     return False
#   else:
#     return True

def is_multiple_10(num: int) -> bool:
    return num % 10 == 0:
#   if num % 10 == 0:
#     return True
#   else:
#     return False

def create_account(user: str) -> bool:
   with open("bank.json","r") as f:
     users = json.load(f)
   
   if str(user) in users.keys():
     return False
   else:
     users[str(user)] = {}
     users[str(user)]["bank"] = 500

   with open("bank.json","w") as f:
     json.dump(users, f)
   return True

def get_bank_data(user: Optional[str] = None) -> Union[None, int, dict]:
  with open("bank.json","r") as f:
    users = json.load(f)
  
  return users.get(str(user), {}).get("bank", None) if user else users
#   if user:
#     return users.get(str(user), {}).get("bank", None)
#   else:
#     return users

def update_bank(user: str, change: int = 0) -> int:
  users = get_bank_data()
  users[str(user)]["bank"] += change
  bal = users[str(user)]["bank"]
  if bal < 0:
    bal = 0
    users[str(user)]["bank"] = 0
  with open("bank.json","w") as f:
     json.dump(users, f)

  return bal
