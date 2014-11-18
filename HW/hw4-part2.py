######################################
# part 2: contributor counts
from __builtin__ import file

#Your next task is to extend the functionality from last week's homework
#assignment using functions.  In the last assignment, you read in the contents
#of a file, computed the poster contribution frequencies using a dictionary, and
#printed out the contents of that dictionary.

#This week, you'll write a function that computes the poster frequencies and
#returns the dictionary as a value. The dictionary will then be passed as a
#parameter to two more functions that will do something with it.


#### is_field() tests if the line represents the given kind of field
# you don't have to modify this function.
# inputs:
#   field_name: a string that specifies the kind of field
#   s: the string we are testing
# returns: True if s starts with field, False otherwise
def is_field(field_name, s):
    if s[:len(field_name)] == field_name:
        return True
    else:
        return False


#### contributor_counts() should return post and comment frequency for each user
# in the specified file
# input:
#   file_name: name of file being read
# returns: a dictionary of post and comment counts
# e.g., if we we had two posters, Alice (0 comments, 2 posts) and Bob (1 post, 2 comments), 
# our dictionary would look like
# cc = {"Alice":{"posts":2,"comments":0},"Bob":{"posts":1,"comments":2}}

# define contributor_counts() here.
# in this function, you MUST make at least one call to the function is_field
def contributor_counts(file):
    Dic = {}
    f = open(file,'r')
    name = ""
    for line in f:
        singleLine = line.split(":")
        if is_field("from", singleLine[0]):
            name = singleLine[1].strip()
            if name not in Dic:
                Dic[name] = {}
                Dic[name]["post"] = 0
                Dic[name]["comment"] = 0
                
        if is_field("post",singleLine[0]):
            Dic[name]["post"] += 1
            
        if is_field("comment",singleLine[0]):
            Dic[name]["comment"] += 1
          
    #print Dic      
    return Dic  
        
    

#### print_contributors() should print out the number of times each
# person posted and commented.
# The implementation should be similar to what was done in hw3 to print out
# contributor counts, but will use an if statement so that contributor counts of
# 1 will be printed as "once" and higher or zero counts will be "X times". For
# example:
#   "John Smith posted once and commented 2 times"
#   "Jane Smythe posted 4 times and commented 0 times"
#
# input parameter:
#   counts: dictionary of contributor counts

# define print_contributors() here.
def print_contributors(counts):
    ppl = counts.keys()
    for person in ppl:
        #person = person.strip()
        post_count = ""
        comment_count = ""
        if counts[person].get("post") == 1:
            post_count = "once"
        else:
            post_count = str(counts[person].get("post")) + " times"
            
        if counts[person].get("comment") == 1:
            comment_count = "once"
        else:
            comment_count = str(counts[person].get("comment")) + " times"
        
        print person + " posted " + str(post_count) + " and commented " + str(comment_count) +"."
    
    
    
#### save_contributors() should save a comma separated value (CSV) formatted
# file where the first item is the key of a dictionary and the second item is
# the value (e.g. name,post_count,comment_count).
# input parameters:
#   counts: dictionary of contributor counts
#   output_file_name: name of the file being saved to

# the first line in the file should be a header row:
# name,post_count,comment_count 

# define save_contributors() here.
def save_contributors(counts, output_file_name):
    f = open(output_file_name,'w')
    f.write("name,post_count,comment_count" + '\n')
    ppl = counts.keys()
    for person in ppl:
        f.write(person + ',' + str(counts[person].get("post")) + ',' + str(counts[person].get("comment")) + '\n')
        #f.write(str(counts[person].get("post")))
        #f.write(str(counts[person].get("comment")) + '\n')

# the following code runs your functions to make sure they work properly
# uncomment all valid lines of python code to test your functions

# read in and count contributions
contributions = contributor_counts("hw3feed.txt")

# human readable version
print '------'
print_contributors(contributions)

# computer readable version
save_contributors(contributions, 'contributors.csv')
