def image_search(images, term):

    search_result = []

    for image in images:
        if term.lower() in image.lower():
            search_result.append(image)

    print(search_result)

    return search_result

## Tests:
image_search(["dog.png", "cat.jpg", "parrot.jpeg"], "dog") #should return ["dog.png"].
image_search(["Sunset.jpg", "Beach.png", "sunflower.jpeg"], "sun") #should return ["Sunset.jpg", "sunflower.jpeg"].
image_search(["Moon.png", "sun.jpeg", "stars.png"], "PNG") #should return ["Moon.png", "stars.png"].
image_search(["cat.jpg", "dogToy.jpeg", "kitty-cat.png", "catNip.jpeg", "franken_cat.gif"], "Cat") #should return ["cat.jpg", "kitty-cat.png", "catNip.jpeg", "franken_cat.gif"].