def generate_signature(name, title, company):

    signature = ''
    prefix = ''

    if ord(name[0].lower()) >= 97 and ord(name[0].lower()) <= 105:
        prefix ='>>'

    if ord(name[0].lower()) >= 106 and ord(name[0].lower()) <= 114:
            prefix ='--'

    if ord(name[0].lower()) >= 115 and ord(name[0].lower()) <= 122:
            prefix ='::'

    signature = prefix + name + ", " + title + " at " + company

    print(signature)

    return signature

## Tests:
generate_signature("Quinn Waverly", "Founder and CEO", "TechCo") 
#should return "--Quinn Waverly, Founder and CEO at TechCo".

generate_signature("Alice Reed", "Engineer", "TechCo") 
#should return ">>Alice Reed, Engineer at TechCo".

generate_signature("Tina Vaughn", "Developer", "example.com") 
#should return "::Tina Vaughn, Developer at example.com".

generate_signature("B. B.", "Product Tester", "AcmeCorp") 
#should return ">>B. B., Product Tester at AcmeCorp".

generate_signature("windstorm", "Cloud Architect", "Atmospheronics") 
#should return "::windstorm, Cloud Architect at Atmospheronics".