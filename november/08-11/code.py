
def can_post(message):
    
    post_type = ""
    if(len(message) <= 40):
        post_type = "short post"
    elif(len(message) > 40 and len(message) <= 80):
        post_type = "long post"
    elif(len(message) > 80):
        post_type = "invalid post"

    return post_type

# end of main.py **

