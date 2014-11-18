
### you will need this function for part 4
def stripWordPunctuation(word):
    return word.strip(".,()<>\"\\'~?!;:*").strip()


print "== part 2 =="
### part 2: printing users
# Open the file hw3feed.txt to see what its contents are. Scan through it
# and you'll notice that lines containing users' names start with "from: ".

# Your job is to extract the names and print them out, exactly as it is shown in
# the screenshot in the PDF file. Hint: if you want to remove "from:"  you can
# use string slicing operations or the replace method.

# Duplicate names are okay!

fname = "hw3feed.txt"
f = open(fname,'r')
#fill in code here

for line in f:
    if line.find("from:") == 0:
       print line.strip('from:').strip()

print "== part 3 =="
### part 3: counting poster contribution frequency
# see the instructions in the PDF file. They are easier to follow with
# formatting

post_count = {}
f = open(fname,'r')

# read in and count the number of posts per user

#fill in code here
for line in f:
    if line.find("from:") == 0:
        name = line.strip('from:').strip()
        
        if post_count.has_key(name):
            #print "We saw this name before!"
            post_count[name] = post_count[name]+1
            #print post_count[name]
        else:
            #print "First time seeing this name!"
            post_count[name] = 1
            
       

# print the number of times each user posted
names = post_count.keys()

for name in names:
    print name + " " + str(post_count[name])
#fill in code here

print "== part 4 =="
### part 4: counting word frequency
# This is similar to post count in part 3 and you might
# even re-use some of your code. Count the number of
# times each word appears in all posts.

# for this, do not worry about punctuation
# so "word." might appear as a word.
# for a JFFE, you can get rid of the punctuation.

post_count = {}
f = open(fname,'r')

# read in and count of times each word appeared
article = f.read().strip()
words = article.split()

for word in words:
    word = stripWordPunctuation(word)
   
    if post_count.has_key(word):
        post_count[word] = post_count[word] + 1
    else:
        post_count[word] = 1
#fill in code here


# print the number of times each word appeared
words = post_count.keys()

for item in words:
    print item + " " + str(post_count[item])

