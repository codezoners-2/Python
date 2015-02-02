#!/usr/bin/python

# A. Given a list of numbers, return the count of the number of
# numbers that are greater than 100 and less than 200
def countNumbers(numbers):
  # +++your code here+++
  return

# B. 60's first
# Given a list of numbers, return a list with the numbers in sorted order
# except group all the numbers between 60-69 first.
# e.g. [10, 60, 20, 66, 79, 5] yields
# [60, 66, 5, 10, 20, 79]
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.
def sixtiesFirst(numbers):
  # +++your code here+++
  return

# Calls the above functions with interesting inputs.
def main():
  print 'countNumbers'
  print countNumbers([20, 120, 1000, 199, 200])
  print countNumbers([120, 0, 201, 500, 9999])

  print
  print 'sixtiesFirst'
  print sixtiesFirst([10, 60, 20, 66, 79, 5])
  print sixtiesFirst([-5, 0, 61, 60, 59, 1, 199])
  
if __name__ == '__main__':
  main()
