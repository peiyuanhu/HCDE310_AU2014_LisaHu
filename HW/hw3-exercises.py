### part 1: exercises
pet_count = {'dog': 3, 'cat': 2, 'rabbit': 7, 'fish': 5}

print "== 1 =="
# 1: accessing values at a specified key in a dictionary.

# Write code to print the number of rabbits in the household (the value
# associated with key 'rabbit' in the dictionary pet_count). Hint: this is just
# one simple line of code.

print pet_count['rabbit']

print "== 2 =="
# 2: incrementing the value of a dictionary at a key.

# Write code to increment the number of rabbits in the house by one (add 1 to the
# existing value of pet_count at key 'rabbit').  Then, print out the number of rabbits
# in the household.

pet_count['rabbit'] += 1
print pet_count['rabbit']

print "== 3 =="
# 3: adding an entry to a dictionary. 

# Write code to insert a new key, 'hamster' into the dictionary, with a value of 4.
# Verify that it worked by print out the value associated with the key 'hamster'

pet_count['hamster'] = 4
print pet_count['hamster']

print "== 4 =="
# 4: concatenating strings and integers. 

# Write code that creates a string that says 'There are X cats', where X is the
# number of cats extracted from the pet_count dictionary.  Print the string.
# Hint: you will need to use the + string concatenation operator in conjunction
# with str().

print "There are " + str(pet_count['cat']) + " cats."

print "== 5 =="
# 5: iterating over keys in a dictionary.  

# Write code that prints each kind of pet (key), one line at a time using a for
# loop.

for pet in pet_count:
    print pet

print "== 6 =="
# 6: iterating over keys to access values in a dictionary. 

# Write code that prints each kind of pet (key), followed by a colon and the
# number of pets (e.g., cat: 2), one line at a time using a for loop.
for pet in pet_count:
    print pet + ": " + str(pet_count[pet])

print "== 7 =="
# 7: testing membership in a dictionary.

# Write code to test whether 'hamster' is in the pet_count dictionary.  If the test
# yields true, print "there are <x> hamsters", where <x> is the current number of
# hamsters in the household.  Do the same thing for the key 'chinchilla.
if 'hamster' in pet_count:
    print "there are " + str(pet_count['hamster']) + " hamsters"
if 'chinchilla' in pet_count:
    print "there are " + str(pet_count['chinchilla']) + " chinchilla"


print "== 8 =="
# 8: default values

# this code asks about wheter the list we have any of the potential pets (in
# the list potential pets) in our dictionary. but the code has errors.
# change the line below ##change the next line so that it prints 0 when we 
# have no animals of that type (i.e., that animal is not a key in our dictionary)
# rather than generating an error. 

# you can do this in one line or more lines. If you use more than one line,
# that is okay.

potentialpets = ['cat','mouse','pig','velociraptor','frog','fish','hamster']
for animal in potentialpets:
    ## change the next line
    pet_count.setdefault(animal,0)
    print animal+": "+str(pet_count[animal])
