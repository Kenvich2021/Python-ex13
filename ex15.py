from sys import argv

script, filename = argv



print "Here's your file name %r:" % filename
txt = open(filename)
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

print "type your text which text you want to open: "
text = raw_input("> ")
text_again = open(text)

print text_again.read()
