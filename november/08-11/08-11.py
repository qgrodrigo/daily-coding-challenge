def can_post(message):
    
    post_type = ''
    
    if len(message) <= 40:
        post_type = 'short post'
        
    if len(message) > 40 and len(message) <= 80:
        post_type = 'long post'
        
    if len(message) > 80:
        post_type = 'invalid post'
    
    print(post_type)
    
    return post_type

# Tests
can_post("Hello world") #should return "short post".
can_post("This is a longer message but still under eighty characters.") #should return "long post".
can_post("This message is too long to fit into either of the character limits for a social media post.") #should return "invalid post".
