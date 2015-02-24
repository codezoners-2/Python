import sys

arguments = sys.argv[1:]
	
if not arguments:
	print "usage: scriptName -{parameter_list}"
	sys.exit(1)

# code to do things to arguments follows
print arguments
