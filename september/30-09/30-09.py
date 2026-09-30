def format_number(number):

    country_code = "+" + number[0]
    city_code ="(" + number[1:4] + ")"
    digits = number[4:7] + "-" + number[7:]

    phone_number = country_code + " " + city_code + " " + digits
    

    return phone_number