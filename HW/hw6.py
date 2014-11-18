import json
from sets import Set

### utility functions-- don't edit these; just call them as needed
def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)

def short_name(username):
    """returns the abbreviated version of a username"""
    ss = username.split()
    return '%s %s.' % (ss[0], ss[-1][0])


def gen_photo_page(post_objects, filename):
    """generates a web page from a list of photo objects
     inputs:
       post_objects: a list of Post objects
       filename: output html file
    """
    out = open(filename, 'w')
    out.write('<html><head><title>HCDE310 Photos</title></head>\n') 
    out.write('<body>\n')

    img_template = '<a href="%s" title="%s"><img src="%s"/><br></a>\n'
    for post in post_objects:
        if isinstance(post, Photo):  # only write out Photo posts
            out.write(img_template % (post.photo_url, post.name, post.preview_url))

    out.write('</body></html>')
    out.close() 



### Building Block 1: the Post class
class Post():
    """object representing status update"""
    def __init__(self, post_dict):
        # self.message is the instance variable containing the post's message
        self.message = post_dict['message']  
        #print self.message
        
        # if the post dictionary has a 'comments' key, set self.comments to the
        # corresponding comments dictionary. otherwise, set self.comments to None
        if 'comments' in post_dict:
            self.comments = post_dict['comments']
            #print type(self.comments)
            print type(self.comments['data'][0])
        else:
            self.comments = None
     
        # if the post dictionary has a 'likes' key, set self.likes to
        # the corresponding likes dictionary.  otherwise, set self.likes to None
        if 'likes' in post_dict:
            self.likes = post_dict['likes']
        else:
            self.likes = None

    # (a): fill in code here to initialize the name instance variable
    #      to the short name of the user in the post dictionary. Hint: see your poster() function from hw6
    #      then uncomment the testing line in the main block at the end of the file
        self.name = short_name(post_dict['from']['name'])

    def unique_commenter(self):
        if self.comments_count() > 0:
            list_commenter = []
            #print type(self.comments['data'][0])
            for item in self.comments['data']:
                #print type(item)
                list_commenter.append(item['from']['name'])
            commenter = Set(list_commenter)
            return commenter
        
    # in step 1(b) uncomment the following two lines, and also the corresponding line in the main block
    def comments_count(self):
        """returns the number of comments"""
#        (b): fill in code here.  hint: None is a value, just like 0 or 'foo'
        if self.comments is not None:
            return len(self.comments['data'])
        else:
            return 0

    # uncomment the following two lines
    def likes_count(self):
        """returns the number of likes"""
        # (c): fill in code here.
        if self.likes is not None:
            return len(self.likes['data'])
        else:
            return 0

#     uncomment the following two lines
    def short_message(self):
        """returns the shortened (<=140 character) message"""
#        (d) fill in code here.
        if len(self.message)>140:
            return self.message[:140]
        else:
            return self.message
    
    def __str__(self):
        """string representation of the post"""
        s = '--- status update ---------\n'
        # uncomment the following lines after you write and test (a-d) [e]
        s += 'name: %s\n' % self.name                  # (a)
        s += 'comments: %s\n' % self.comments_count()  # (b)
        s += 'likes: %s\n' % self.likes_count()        # (c)
        s += 'message: %s\n' % self.short_message()    # (d)
        return s

#     uncomment the following two lines
    def is_question(self):
        """returns True if the message contains a '?'."""
#        (f) fill in code here
        msg = self.message
        #msg = self.short_message()
        if len(msg)>0:
            return msg[-1] == '?'
        else:
            return False



### Building Block 2: the Link class
class Link(Post):
    """object representing a Link post"""
    def __init__(self, post_dict):
        Post.__init__(self, post_dict)
        self.url = post_dict['link']

#     uncomment the following two lines
    def __str__(self):
        """string representation of the Link post"""
#        fill in code here (2.a)
#        the string being returned should be similar to that of Post.__str__()
#        except it should also print out the linked url (see PDF for details)
        s = '--- link ---------\n'
        # uncomment the following lines after you write and test (a-d) [e]
        s += 'name: %s\n' % self.name                  # (a)
        s += 'comments: %s\n' % self.comments_count()  # (b)
        s += 'likes: %s\n' % self.likes_count()        # (c)
        s += 'message: %s\n' % self.short_message()    # (d)
        s += 'linked url: %s\n' %self.url
        return s
    
### Building Block 3: the Photo class
class Photo(Post):
    """object representing a Photo post"""
    def __init__(self, post_dict):
        Post.__init__(self, post_dict)
        self.preview_url = post_dict['picture']
        self.photo_url = post_dict['link']

    def __str__(self):
#         fill in code here. (3.a)
#         the string being returned should be similiar to that of Post.__str__()
#         except it should also print out the linked photo (see PDF for details)
        s = '--- photo ---------\n'
        # uncomment the following lines after you write and test (a-d) [e]
        s += 'name: %s\n' % self.name                  # (a)
        s += 'comments: %s\n' % self.comments_count()  # (b)
        s += 'likes: %s\n' % self.likes_count()        # (c)
        s += 'message: %s\n' % self.short_message()    # (d)
        s += 'thumbnail: %s\n' %self.preview_url
        s += 'photo: %s\n' %self.photo_url
        return s

### Main block
if __name__ == '__main__':  # put all of your code within this if block
    # this loads up the facebook group data as a list of dictionaries
    post_dictionaries = json.load(open('hw6_fbgroup.json'))['data']
    print pretty(post_dictionaries[2])
    print "-- TEST 1 --"
    ### Test 1: polymorphism with  __str__() methods
    # sample Posts to print
    my_post_short = Post(post_dictionaries[2])
    my_post_long = Post(post_dictionaries[9])
    #print pretty(my_post_short)
    print "- elements -"
    # uncomment the following lines as you implement building block 1a-d:
    print my_post_short.name              # tests (1a)
    print my_post_short.comments_count()  # tests (1b)
    print my_post_short.likes_count()     # tests (1c)
    print my_post_short.short_message()   # tests (1d)
    print my_post_long.short_message()    # tests (1d)
    
    # uncomment the following two lines to test (1e)
    print "- short post -"
    print my_post_short
    print "- long post -"
    print my_post_long
    
    ## testing building block 2
    # sample Link to print
    my_link = Link(post_dictionaries[31])
    print my_link            # tests (2a)
    
    # testing building block 3
    my_photo = Photo(post_dictionaries[8])
    print my_photo                     # tests (3a)

    # convert all dictionaries to Post, Photo, and Link objects
    post_objects = []  # start off with empty list of objects
    for post_dict in post_dictionaries:
        # make a Post, Photo, or Link object from the post dictionary depending
        # on what type is specified in the 'type' key.
        if post_dict['type'] == 'status':
            post_object = Post(post_dict)
        elif post_dict['type'] == 'photo':
            post_object = Photo(post_dict)
        elif post_dict['type'] == 'link':
            post_object = Link(post_dict)
        # add the post object to the list
        post_objects.append(post_object)

    ### Test 2: Outputting Photo objects as a web page: (testing 3a,b)
#    uncomment the following line of code and verify that hcde310photos.html
#    displays thumbnail images that link back to the respective facebook photo
#    include hcde310photos.html in your Canvas upload

    gen_photo_page(post_objects, 'hcde310photos.html')


    ### Task 1: printing questions
    print ";;;;; Task 1: printing questions ;;;;;;;"
    first_35 = post_objects[:35]  # sample set of posts
    # fill in code here that prints questions in the first 35 post objects
    for post in first_35:
        name = post.name
        num_response = post.comments_count()
        if post.is_question():
            #print name
            print "------------"
            print name + "got " + str(num_response) + " responses to their question:"
            print post.short_message()
            print "Here is a set of unique commenters: " + str(post.unique_commenter())
            print "------------"
            
            
  
