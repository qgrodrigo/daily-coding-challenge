full_dot = '●'
empty_dot = '○'

def create_character(name, force, brain, character):

    #name validations
    if not isinstance(name, str):
        return 'The character name should be a string'
    if not name:
        return 'The character should have a name'
    if(len(name) > 10):
        return 'The character name is too long'
    if(' ' in name):
        return 'The character name should not contain spaces'
    
    #estatics validations

    if not isinstance(force, int) or not isinstance(brain, int) or not isinstance(character, int):
        return 'All stats should be integers'
    if force < 1 or brain < 1 or character < 1:
        return 'All stats should be no less than 1'
    if force > 4 or brain > 4 or character > 4:
            return 'All stats should be no more than 4'
    if not (force + brain + character)  == 7:
         return 'The character should start with 7 points'

    return (name + '\n' + 
    'STR ' + full_dot * force + empty_dot * (10 - force) + '\n' +
    'INT ' + full_dot * brain + empty_dot * (10 - brain) + '\n' +
    'CHA ' + full_dot * character + empty_dot * (10 - character))

print(create_character('ren', 4, 2, 1))