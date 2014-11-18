'''
Created on Oct 29, 2014

@author: me
'''
import urllib,urllib2,json
from BeautifulSoup import BeautifulSoup
from apt_pkg import DATE

def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)

flickr_baseurl = 'https://api.flickr.com/services/rest/?'
api_key = '7d5908ba74cd34d120c336335db9fc24'

def flickr_get_people_info(user_id):
    url = flickr_baseurl+'&method=flickr.people.getInfo' + '&api_key='+api_key +'&user_id='+user_id +'&format=json'
    return creat_dic(url)

def flickr_get_contact_list(user_id):
    url = flickr_baseurl+'&method=flickr.contacts.getPublicList' + '&api_key='+api_key +'&user_id='+user_id +'&format=json'
    return creat_dic(url)

def flickr_get_interesting_photos(extras, per_page = 100):
    url = flickr_baseurl+'&method=flickr.interestingness.getList' + '&api_key='+api_key +'&extras='+extras +'&per_page='+str(per_page) +'&format=json'
    return creat_dic(url)
    
def flickr_get_public_photos(user_id):
    '''This method takes user id and returns a dictionary of user's public photos.'''
    url = flickr_baseurl+'&method=flickr.people.getPublicPhotos' + '&api_key='+api_key +'&user_id='+user_id +'&format=json'
    return creat_dic(url)

def flickr_get_public_groups(user_id):
    '''This method takes user id and returns a dictionary of user's public photos.'''
    url = flickr_baseurl+'&method=flickr.people.getPublicGroups' + '&api_key='+api_key +'&user_id='+user_id +'&format=json'
    return creat_dic(url)


def flickr_get_location(photo_id):
    url = flickr_baseurl+'&method=flickr.photos.geo.getLocation' + '&api_key='+api_key +'&photo_id='+photo_id +'&format=json'
    return creat_dic(url)

def photo_url(user_id,photo_id):
    '''This method takes two parameters: user id and photo id to generate photo url.'''
    return 'https://www.flickr.com/photos/'+user_id+'/'+photo_id

def creat_dic(url):
    '''Take a Flickr method call url and turn it into a dictionary if it doesn't have error.'''
    test = (urllib2.urlopen(url).read())[14:-1]
    dic = json.loads(test)
    if not bad_url(dic):
        return dic
    
def bad_url(dic):  
    '''Take a dictionary and check whether it hit error code.'''
    if dic['stat'] == 'fail':
        #print 'OOps, We encountered an error'
        #print 'error code: ' + str(dic['code'])
        #print 'error message: ' + dic['message']
        return True
    else:
        return False
        

def main():
    #input = raw_input('What do you want to see?'+'\n')
    interesting_photo = flickr_get_interesting_photos('')
    #print pretty(interesting_photo)
    lib_of_photo = {}
    output = open('Flickrphoto.csv','w')
    output.write('Photo_ID,photographer, first picture taken date, number of contacts' +'\n')
    
    for item in interesting_photo['photos']['photo']:
         
        #print '----------'
        owner_id = item['owner']
        photo_id = item['id']
        #owner_public_photo = flickr_get_public_photos(owner_id)
        #print pretty(owner_photo)
        #total_photo = owner_public_photo['photos']['total']
        #print total_photo
         
        #loc = flickr_get_location(photo_id)
        author = flickr_get_people_info(owner_id)
         
        #print pretty(author)
         
        #username = author['person']['username']['_content']
        firstdatetaken = author['person']['photos']['firstdatetaken']['_content']
        number_of_contacts = len(flickr_get_contact_list(owner_id)['contacts']['contact'])
        #print pretty(flickr_get_public_groups(owner_id))
        #print owner_id
        #print username
        #print firstdatetaken
        #print number_of_contacts
#         if flickr_get_contact_list(owner_id) != {}:
#             number_of_groups = len(flickr_get_public_groups(owner_id)['groups']['group'])
#         else:
#             number_of_groups = 'N/A'
        #url = photo_url(owner_id,photo_id)
        #print '----------'
         
        
        output.write(photo_id+','+ owner_id+','+firstdatetaken +','+ str(number_of_contacts)+'\n')
        
#         lib_of_photo[photo_id] = {}
#         #lib_of_photo[photo_id]['author'] = flickr_get_people_info(owner_id)['username']['_content']
#         lib_of_photo[photo_id]['photographer'] = username
#         lib_of_photo[photo_id]['firstpictaken'] = firstdatetaken
#         lib_of_photo[photo_id]['contacts'] = str(number_of_contacts)
#         lib_of_photo[photo_id]['groups'] = str(number_of_groups)
        #lib_of_photo[photo_id]['latitude'] = loc['photo']['location']['latitude']
        #lib_of_photo[photo_id]['longitude'] = loc['photo']['location']['longitude']
        
    
#     print 'We are going to generate a sheet of picture from Flickr and their url'
#     nameOfFile = raw_input('what do you want to name the file?'+'\n')
#     output = open(nameOfFile+'.csv','w')
#     output.write('Photo_ID,photographer, first picture taken date, number of contacts, number of groupd, URL'+'\n')
#     keys = lib_of_photo.keys()
#     for item in keys:
#         output.write(item + ',' + lib_of_photo[item]['photographer']+','+ lib_of_photo[item]['firstpictaken']+','+ lib_of_photo[item]['contacts']+','+ lib_of_photo[item]['groups']+','+ lib_of_photo[item]['url']+'\n')
    print 'done'    

main()
