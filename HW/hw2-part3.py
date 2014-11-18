### main assignment (part 3)
from __builtin__ import file

# Earlier this week, you learned to think about data processing and how to perform
# basic string and list operations. In this assignment, you'll count the number of lines,
# characters, and words in a file, excluding newline characters.

# We will keep things simple and define a word as something that is delimited by
# any whitespace, so that the number of words on a line that is read from a file
# is simply the number of strings returned by split().

# To help you get started on this first programming assignment, here is a list
# of Python functions and methods that we've discussed (or will discuss) in
# class, or covered in supplement 2, that you will probably find useful:
#    raw_input (optional)
#    open
#    split
#    len
#    print
#    rstrip()


print "----------"

# Try to make your program work first on test.txt, which has 21 characters, 3
# lines, and 5 words. (Note: end of line characters are included in this
# character count!) Then look at the contents of hw2feed.txt, so you can get a
# sense of the right answers, approximately. It's data extracted from our class
# Facebook group! Run your program work on hw2feed.txt and sherlock.txt. Take a
# screenshot of the output when running it on hw2feed.txt

fname = "hw2feed.txt"
#fname = raw_input("Please enter a file name: ")
num_chars = 0
num_lines = 0
num_words = 0

# fill in the rest here
file = open(fname)
for line in file:
    
    words = line.split()
    num_words += len(words)
    num_lines += 1
    #for word in words:
    num_chars += len(line)
    

# output code below is provided for you; you should not edit this
print num_chars, 'characters'
print num_lines, 'lines'
print num_words, 'words'
