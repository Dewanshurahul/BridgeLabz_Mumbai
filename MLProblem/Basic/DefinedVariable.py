try:
  age = 1
except NameError:
  print("Variable is not defined....!")
else:
  print("Variable is defined.")


try:
  name
except NameError:
  print("Variable is not defined....!")
else:
  print("Variable is defined.")