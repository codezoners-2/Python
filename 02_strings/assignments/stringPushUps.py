# BOTH_ENDS
# Given a string s, return a string made of the first 2
# and the last 2 chars of the original string,
# so 'spring' yields 'spng'. However, if the string length
# is less than 2, return instead the empty string.
def both_ends(s):
  if len(s)<2:
	  return []
  else:
	  return s[0:2] + s[-2:]

# FIX_START
# Given a string s, return a string
# where all occurences of its first char have
# been changed to '*', except do not change
# the first char itself.
# e.g. 'babble' yields 'ba**le'
# Assume that the string is length 1 or more.
# Hint: s.replace(stra, strb) returns a version of string s
# where all instances of stra have been replaced by strb.
def fix_start(s):
  # +++your code here+++
  return


# MIX_UP
# Given strings a and b, return a single string with a and b separated
# by a space '<a> <b>', except swap the first 2 chars of each string.
# e.g.
#   'mix', pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Assume a and b are length 2 or more.
def mix_up(a, b):
  # +++your code here+++
  return

# VERBING
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
def verbing(s):
  # +++your code here+++
  return

############ SWITCH DRIVER / OBSERVER ROLES ################

# NOT_BAD
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
  # +++your code here+++
  return


# FRONT_BACK
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(a, b):
  # +++your code here+++
  return

#==============================================

def main():

  print 'both_ends'
  print both_ends('spring')
  print both_ends('Hello')
  print both_ends('a')
  print both_ends('xyz')

  
  print
  print 'fix_start'
  fix_start('babble')
  fix_start('aardvark')
  fix_start('google')
  fix_start('donut')

  print
  print 'mix_up'
  mix_up('mix', 'pod')
  mix_up('dog', 'dinner')
  mix_up('gnash', 'sport')
  mix_up('pezzy', 'firm')

  print
  print 'verbing'
  verbing('hail')
  verbing('swiming')
  verbing('do')

  print
  print 'not_bad'
  not_bad('This movie is not so bad')
  not_bad('This dinner is not that bad!')
  not_bad('This tea is not hot')
  not_bad("It's bad yet not")

  print
  print 'front_back'
  front_back('abcd', 'xy')
  front_back('abcde', 'xyz')
  front_back('Kitten', 'Donut')
  
# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()
