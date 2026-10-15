def strip_tags(html):

    words = html
    positions = []

    for index in range (len(html)):
        pos = 0     
        if(html[index] == '<'):
            positions.append(index)
        if(html[index] == '>'):
            positions.append(index + 1)
            

    for i in range(0, len(positions), 2):   
        x = positions[i]
        y = positions[i+1]

        text_to_replace = html[x:y]
        words= words.replace(text_to_replace, '')

    print(words)

    return words


#Tests
strip_tags('<a href="#">Click here</a>') #should return "Click here".
strip_tags('<p class="center">Hello <b>World</b>!</p>') #should return "Hello World!"
strip_tags('<img src="cat.jpg" alt="Cat">') #should return an empty string ("").
strip_tags('<main id="main"><section class="section">section</section><section class="section">section</section></main>') #should return sectionsection.