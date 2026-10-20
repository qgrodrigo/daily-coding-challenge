import re

def extract_attributes(element):

    rigth = 0
    attributes = []

    for i in range(len(element)):
        if(element[i] == '>'):
            rigth = i
            break
            
    first_tag = element[1:rigth]

    matches = re.findall(r'(\w+)="([^"]*)"', first_tag)

    for name, value in matches:
        attributes.append(f'{name}, {value}')

    print(attributes)

    return attributes

#Tests:
extract_attributes('<span class="red"></span>') #should return ["class, red"].
extract_attributes('<meta charset="UTF-8" />') #should return ["charset, UTF-8"].
extract_attributes("<p>Lorem ipsum dolor sit amet</p>") #should return [].
extract_attributes('<input name="email" type="email" required="true" />') #should return ["name, email", "type, email", "required, true"].
extract_attributes('<button id="submit" class="btn btn-primary">Submit</button>') #should return ["id, submit", "class, btn btn-primary"].