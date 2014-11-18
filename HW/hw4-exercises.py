###############################################################
## part 1: exercises

import csv

print '=== 1 ==='
# 1: function with one parameter
#### questioning_print() prints a string with a question mark (?) at the end
# input parameter:
#   s: the string to print
# define questioning_print() here.
def questioning_print(s):
    print s + "?"

# to help you understand the format of instructions for these exercises, we have
# given you a starter template below. Modify it. Note how the instructions
# mention a parameter, s, which becomes the parameter name in the function
# definition.

#def questioning_print(s):
#    <indented code block here>


# uncomment the next two lines to check if you correctly defined excited_print():
questioning_print('a word')
questioning_print('nice job')

print "=== 2 ==="
# 2: returning a value
#### questioning_string() returns a string with an question mark added to the end
# input parameter:
#   s: the string to question
# returns: a string

# define questioning_string() here
def questioning_string(s):
    return s+"?"
# uncomment the next two lines of code to check if you correctly defined the function
print questioning_string('may I have a word')
print questioning_string('nicer job')

print "=== 3 ==="
# 3: function with two parameters that returns a value
#### chars_after() returns a substring beginning at the specified position,
#chopping off all the characters before start_position
# input parameters:
#   start_position: index of first character to include
#   s: the string to take a slice of

# define chars_after() here:
def chars_after(start_postition, s):
    return s[start_postition:]
# uncomment the following two lines of code to check if you correctly defined the function
#try it with different values for X and Y
X = 5
Y = 4
print chars_after(Y, 'not fun')
print chars_after(X, 'from: Christina Chung')

print '=== 4 ==='
# 4: printing comma separated data in a dictionary.
#Print out the keys and values of the dictionary stored in variable d. The keys
#and values you print should be separated only by commas (there should be no
#spaces). Print each key,value pair on a different line. Your output should
#match the screenshot in the PDF document, although the order of the keys may
#differ.
d = {'a':1, 'b':2, 'c':3}
# put your code here
keys = d.keys()
for key in keys:
    print key + "," + str(d.get(key))

print '=== 5 ==='
# 5: saving a dictionary to a CSV file
#Write key and value pairs from d out to a file named 'exercise.csv'. (hint: the
#procedure is very close to that of (4), but you will need to make a small
#modification to the string you are writing out to the file, to add linebreaks)
# put your code here
file = open('exericse.csv', 'w')
keys = d.keys()
for key in keys:
    file.write(key + "," + str(d.get(key))+'\n');
    #file.write(\n)
print '=== 6 ==='
# 6: dictionaries in dictionaries (challenge)
# This may helpful for part 2 (depending how you do it)
# Recall that a dictionary's value can be any type of object -- even dictionaries.
# so, we might have:
#dinosaurs = {"carnivores":{"Velociraptor":3,"Coelophysis":1,"Tyranosaurus Rex":2},"herbivores":{"Avaceratops":3,"Brachiosaurus":1,"Diplodocus":2,"Stegosaurus":1}}


# for that dictionary, we can access our count of velociraptors with the following:
# raptorcount = dinosaurs['carnivores']['Velociraptor']
# or print it:
#print "raptors: "+str(dinosaurs['carnivores']['Velociraptor'])

# the first time we saw a Carnivore, we could have created a blank dictionary for
# for its value with the following:
#dinosuars['carnivores'] = {}
# or, instead, a dictionary with keys and zero values for raptors and Tyranosaurs,
# our favorite carnivorous dinosaurs, for the value with the following:
#dinosaurs['carnivores'] = {'Velociraptor':0,'Tyranosaurus Rex':0}

dinosaurlist = [("carnivores","Velociraptor"),("herbivores","Diplodocus"),("carnivores","Coelophysis"),("herbivores","Avaceratops"),("carnivores","Velociraptor"),("carnivores","Velociraptor"),("carnivores","Tyranosaurus Rex"),("herbivores","Avaceratops"),("carnivores","Tyranosaurus Rex"),("herbivores","Avaceratops"),("herbivores","Brachiosaurus"),("herbivores","Diplodocus"),("herbivores","Stegosaurus")]
dinosaurs= {}

# iterate over the tuples in dinosaurlist (above) to build the above dictionary
# note that dinosaurlist is a list of tuples (immutable lists). You can index items 
# in it just like you would with a list.
# put your code here
for pair in dinosaurlist:
    catogory = pair[0]
    animal = pair[1]
    
    if dinosaurs.has_key(catogory):
        if dinosaurs[catogory].has_key(animal):
            dinosaurs[catogory][animal]+=1
        else:
            dinosaurs[catogory][animal] = 1
    else:
        dinosaurs[catogory] = {}
        dinosaurs[catogory][animal] = 1
        
        

print dinosaurs


