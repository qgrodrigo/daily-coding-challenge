import re

def validate(email):

    #@ validation
    if(email.count('@') < 1 or email.count('@') > 1):
        return False

    arroba_position = email.find('@')
    user = email[: arroba_position]
    domain = email[arroba_position + 1:]

    #user validations
    if(not user or not domain):
        return False

    user_pattern = r'^[a-zA-Z0-9._-]+$'
    if not re.fullmatch(user_pattern, user):
        return False
    
    if(user[0] == '.' or user[-1] == '.'):
        return False

    if '..' in user or '..' in domain:
        return False
    
    #domain validations

    if '.' not in domain:
        return False

    if not re.search(r'\.[a-zA-Z]{2,}$', domain):
        return False
    
    return True

#Tests
validate("a@b.cd") #should return True.
print(validate("hell.-w.rld@example.com")) #should return True.
validate(".b@sh.rc") #should return False.
print(validate("example@test.c0")) #should return False.
validate("freecodecamp.org") #should return False.
validate("develop.ment_user@c0D!NG.R.CKS") #should return True.
validate("hello.@wo.rld") #should return False.
validate("hello@world..com") #should return False.
validate("develop..ment_user@c0D!NG.R.CKS") #should return False.
validate("git@commit@push.io") #should return False.