### exercises
# Part 3
#from hw1.hw1 import lst
s = "This is a test string for this homework."
lst = [1, 2, 3, 4, 5, 6, 7, 8]

print "=1="
# 1: iterated operation over list

# Write code that iterates over each element of lst using a for loop, printing
# each element on a new line

for x in lst:
    print x


print "=2="
# 2: summing values of a list
# Write code that adds up all the elements of lst
# using a for loop, then prints out the sum. (hint: you will need to add to the
# variable total at every step of the for loop)
#
# Note: this is the example I
# used to teach you the accumulation pattern in lecture. Try to reconstruct the
# code here without looking at that code. You'll be glad for working through it
# do it when you get to part III of this HW and have to use the accumulation
# pattern in a more creative way.
total = 0
# fill in the rest here
for x in lst:
    total+=x
    
print total
    
print "=3="
# 3: splitting strings
# Write code that splits s into a list separate words
# (where each word is defined to be any series of characters separated by a
# whitespace).  Print out the list using a for loop (as in (1)), one word per line.

list = s.split()
for word in list:
    print word
    
print "=4="
# 4: replacing an element of a list
# Replace the element of lst whose value is 3 with the value 'three' and
# then print lst
lst[2] = 'three'
print lst

print "=5="
# 5: print out a file, verbatim
# Read and print each line contained in 'test.txt'.  Your program should
# output the text exactly as it is in test.txt.
# (Hint: you may need to use rstrip() to remove the newline character at the end
# of each line, to avoid getting an extra blank line between each real line.)
fname = "test.txt"
# fill in the rest here
file = open(fname)
for line in file:
    line = line.strip()
    print line

print "=6="
# 6: print out only items containing a certain string
# (see instructions for parts 6a, 6b, 6c)

catlist = ['puma', 'mountain lion', 'snow leopard', 'lion', 'tiger', 'leopard', 'jaguar', 'cheetah', 'cougar', 'clouded leopard', 'Cowardly Lion', 'Kpo the Leopard', 'Pink Panther', 'Tigger', 'Tony the Tiger']

print "==6a=="
# 6a iterate over catlist. print out where in each line the string tiger can be found
# (if it cannot be found, print -1). hint: print the output of find()
# Case does not matter. It should match "tiger" or "Tiger"
for cat in catlist:
    cat = cat.lower()
    print cat.find('tiger')
        
    

print "==6b=="
#6b:
binlist = [0,1,1,0,1,1,0]

# Iterate over binlist. If the current item equals 0
# print "Zero". Otherwise, don't print anything.
# Note: this may be easier after Monday's lecture.
for item in binlist:
    if int(item)== 0:
        print 'Zero'

print "==6c=="
# 6c
# now, iterate over catlist. print out only the items that contain the string leopard
# case does not matter, you should match Leopard or leopard
# hint: you will need to use if. find() may help.
# You might not be able to do this until after Monday's lecture.

for cat in catlist:
    
    if cat.find('leopard')&cat.find('Leopard') != -1:
        print cat
        
        

