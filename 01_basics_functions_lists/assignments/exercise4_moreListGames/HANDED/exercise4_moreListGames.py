#!/usr/bin/python

# C. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3].
# Hint: create a for loop and for each number check if it's not the same as the 
# one just added to the list.
def remove_adjacent(nums):
  # +++your code here+++
  return

# D. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideallyyou should make a single pass of both lists.
# so (['aa', 'xx'], ['bb', 'cc', 'zz']) returns ['aa', 'bb', 'cc', 'xx', 'zz']
def linear_merge(list1, list2):
  # +++your code here+++
  return

# Calls the above functions with interesting inputs.
def main():
  
  print 'remove_adjacent'
  print remove_adjacent([1, 2, 2, 3])
  print remove_adjacent([2, 2, 3, 3, 3])
  print remove_adjacent([])

  print
  print 'linear_merge'
  print linear_merge([10, 50, 90], [20, 30])
  print linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz'])
  print linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb'])


if __name__ == '__main__':
  main()
