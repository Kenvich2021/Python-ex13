# truoc khi lam bai can tao 1 file test.txt và new_test.txt

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %r to %s" % (from_file, to_file)

#we could do these two on one line, how?
in_file = open(from_file).read()


print "The input file is %d bytes long" % len(in_file)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w').write(in_file)


print "Alright, all done."

