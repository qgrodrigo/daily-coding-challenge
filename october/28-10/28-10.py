def navigate(commands):

    back = []
    current = 'Home'
    forward = []

    only_commands = ['Back', 'Visit', 'Forward']

    for command in commands:

        if command.startswith("Visit "):
            page = command[6:]
            back.append(current)
            current = page
            forward.clear()

        if command == "Back":
            if back:
                forward.append(current)
                #print(f'back len: {len(back)}')
                current = back[-1]
                back.pop()

        if command == 'Forward':            
            if forward:
                back.append(current)
                current = forward[0]


    #print(f'back: {back}')
    print(f'current: {current}')
    #print(f'forward: {forward}')
    
    return current

#Tests:
navigate(["Visit About Us", "Back", "Forward"]) #should return "About Us".
navigate(["Forward"]) #should return "Home".
navigate(["Back"]) #should return "Home".
navigate(["Visit About Us", "Visit Gallery"]) #should return "Gallery".
navigate(["Visit About Us", "Visit Gallery", "Back", "Back"]) #should return "Home".
navigate(["Visit About", "Visit Gallery", "Back", "Visit Contact", "Forward"]) #should return "Contact".
navigate(["Visit About Us", "Visit Visit Us", "Forward", "Visit Contact Us", "Back"]) #should return "Visit Us".