import json

## helper functions
## short_name
# inputs:
#   s: a string of the format "firstname lastname"
# returns:
#   a string of the format "firstname first-initial-of-lname"
def short_name(s):
    ss = s.split()
    return '%s %s.' % (ss[0], ss[-1][0])

## use this function between building blocks and tasks to make output easier
## to read
def gap(s=''):
    print '\n-----------' + s + '-----------'

## use this function to make more readable output of nested data structures
def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)

## this loads up the facebook group data as a list of dictionaries, with value as dictionary.
posts = json.load(open('hw5_fbgroup.json'))['data']

#print posts
## this extracts 3 dictionaries from the list of posts, which you will use
## as examples throughout the homework

mypost = posts[2]            # this is a post with comments
mypost2 = posts[5]           # this is post without comments
mypost3 = posts[12]          # this is a post with likes


## here is what a post dictionary looks like
print "==== example post ===="
print pretty(posts)

## posts is a list of dictionaries
#print 'there are', len(posts), 'posts!'


### Building Block 1
## extracting the name of a poster
gap('building block 1')

## write code that extracts and prints the data associated with the 'from'
## key in mypost
#<your-code-here>
#print pretty(mypost)
#print mypost["from"]

for item in mypost["from"]:
    print "\"" + item + "\"" + ": " + mypost["from"][item]
    
## write code that extracts and prints the name of the user who posted mypost
#<your-code-here>

print mypost["from"]["name"]

## define a function called poster()
##  input parameter:
##    post: a dictionary that represents one FB post
##  return:
##    a string that is the short name of the person who made the post
##    make use of the short_name function defined above
#<your-code-here>
def poster(post):
    name = post["from"]["name"]
    return short_name(name)
    


## uncomment the following two lines of code. It should print the short name
# of the user that posted the item in mypost and mypost2.
# make use of the short_name function defined above
print poster(mypost)
print poster(mypost2)


### Building block 2
## extracting the number of comments for a post
gap('building block 2')

## some posts have comments
#print mypost['comments']

## other posts don't
# if you uncomment the following line, you'll get an error
#print mypost2['comments']

## here are what comment dictionaries look like
gap("a comment's data structure")
#print pretty(mypost['comments'])

## this is how you get the number of comments from a comment dictionary
## if, and only if, that dictionary has comments (otherwise you get)
## an error
print "Comment count:", len(mypost['comments']['data'])

## write a function called post_comment_count() that extracts and
## returns the number of comments from a post dictionary.
#<your-code-here>
def post_comment_count(post):
    if post.has_key('comments'):
        return len(post['comments']['data'])
    else:
        return 0
    
## uncomment the following two lines of code. they should print 3 and 0
print post_comment_count(mypost)
print post_comment_count(mypost2)

### Building block 3
# extracting like counts (is very similar to comment
# counts, but likes dictionary may be missing)

## here are what 'like' dictionaries contain. Note that Facebook has only
#provided the names of a subset of the people who liked the post
gap("a post's likes data structure")
#print pretty(mypost3['likes'])

## but some posts don't have likes. You get an error when you uncomment the following
# print pretty(mypost['likes'])

## write code that gets the number of likes from mypost3
#<your-code-here>
print len(mypost3['likes']['data'])
## write a function called post_like_count() that extracts and
## returns the number of likes from a post dictionary
## if the dictionary does not contain any likes, it should return 0
#<your-code-here>
def post_like_count(post):
    if post.has_key('likes'):
        return len(post['likes']['data'])
    else:
        return 0
## the following two lines should print 0 and 2 when uncommented
print post_like_count(mypost)
print post_like_count(mypost3)


### Task 1
# Print out one line for each post in the dataset using the 3 functions
# that you have written
# Your output should look like:
#   NAME posted to the group and received X comments and Y likes
# with one line per post
gap("Task 1")
#<your-code-here>
for entry in posts:
    name = poster(entry)
    like = post_like_count(entry)
    comment = post_comment_count(entry)
    print name + " posted to the group and received " + str(comment) + " comments and " + str(like) + " likes"

### Task 2
# count total number of posts, likes received, and comments received
# for each user; results should be stored in the three dictionaries below
gap("Task 2")
post_counts = {}     # how many times each contributor (user) posted
like_counts = {}     # how many likes a contributor received
comment_counts = {}  # how many comments a contributor received
#<your-code-here>
#Dic = {}
for entry in posts:
    name = poster(entry)
    like = post_like_count(entry)
    comment = post_comment_count(entry)
    if post_counts.has_key(name):
        post_counts[name]+=1
    else:
        post_counts[name] = 1
    if like_counts.has_key(name):
        like_counts[name]+=like
    else:
        like_counts[name] = like
    if comment_counts.has_key(name):
        comment_counts[name]+=comment
    else:
        comment_counts[name] = comment
        

## uncomment out the following two lines to test out your counting procedure
for name in post_counts:
    print '%s %d %d %d' % (name, post_counts.get(name,0), like_counts.get(name,0), comment_counts.get(name,0))


### Task 3
## save the above information to a CSV file called hw5_output.csv
## HINT: you did this for the previous hw.
gap("Task 3")

#<your-code-here>
file = open('hw5_output.csv','w')
file.write("name,posts,likes,comments" + "\n")
for name in post_counts:
   name = short_name(name)
   postcount = post_counts.get(name,0)
   
   likecount = like_counts.get(name,0)
   commentcount = comment_counts.get(name,0)
   #file.write("dd")
   #file.write(name + "," + str(postcount)+ "\n")
   file.write(name + "," + str(postcount) + "," + str(likecount) + "," + str(commentcount) + "\n")
    

### Task 4
# google doc your data: see PDF for instructions
