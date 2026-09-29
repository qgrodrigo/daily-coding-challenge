def get_headings(csv):

    csv_split = csv.split(",")
    csv_clean = []

    for word in csv_split:
        csv_clean.append(word.strip())

    print(csv_clean)

    return csv_clean

get_headings("name,age,city") #should return ["name", "age", "city"].
get_headings("first name,last name,phone") #should return ["first name", "last name", "phone"].
get_headings("username , email , signup date ") #should return ["username", "email", "signup date"].