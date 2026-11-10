def get_extension(filename):

    parts = filename.split('.')

    extension = "none"

    if "." in filename:
        extension = parts[-1]

    if extension == '':
        extension = "none"

    print(extension)

    return extension

## Tests:
get_extension("document.txt") #should return "txt".
get_extension("README") #should return "none".
get_extension("image.PNG") #should return "PNG".
get_extension(".gitignore") #should return "gitignore".
get_extension("archive.tar.gz") #should return "gz".
get_extension("final.draft.") #should return "none".