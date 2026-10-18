def mask(card):

    masked_version = ''

    for i in range(len(card)):

        if(i < len(card) -4):
            if card[i] == ' ' or card[i] == '-':        
                masked_version +=  card[i]
            else:
                masked_version += '*'
        else:
            masked_version +=  card[i]

        
    print(masked_version)


    return masked_version

#Tests:
mask("4012-8888-8888-1881") #should return "****-****-****-1881".
mask("5105 1051 0510 5100") #should return "**** **** **** 5100".
mask("6011 1111 1111 1117") #should return "**** **** **** 1117".
mask("2223-0000-4845-0010") #should return "****-****-****-0010".