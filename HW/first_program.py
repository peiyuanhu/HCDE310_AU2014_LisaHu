# This file, with a .py extension, contains a python program
# Lines that start with the hash sign are ignored by Python. They are
# used for comments.

# Step 1: To run this program, in a terminal window, cd ~/Homeworks/hw0 and then type
# "python2.7 first_program.py" (at the bottom of the screen do: Menu->Terminal).


def hello():
    print "-----------------------------------------------------"
    print "Welcome to HCDE310."
    print "We hope you enjoy the class."
    print "-----------------------------------------------------"
    print "\n"       # print a newline to create a blank line


hello()
print ".... Let's say that again...  \n"
hello()

# Step 2: Now, try deleting the second hello(). Save the file.  Run
# the program again to see the results.

# Step 3: Now, insert "hello()" back into the editor buffer below this line. Try
# using the auto-complete feature: after you type in "hel", hit control-space to
# get possible completions, use arrow keys or the mouse to select, and then hit
# enter.

# Save the file. Run python2.7 again to see the results.

# Step 4: Now, try a Python program that uses variables. Uncomment the lines
# below, by removing the # signs at the beginning of the lines. Fill in values
# for length, width, height, and you. Then save and run the program again.
length = 10
width = 10
height = 10

me = "Lisa Hu"
print "Volume = ", width*height*length
print "My name is", me

# Step 5: Instead of running the program from a terminal window, you can
# actually run it from inside Eclipse. After you save it, click on the run icon
# in the ribbon, or Run from the menu. The output will show up at the bottom of
# the screen, in the Console window.
