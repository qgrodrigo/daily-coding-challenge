#** start of main.py **

def has_exoplanet(readings):

    minimun_average = average_readings(readings) * 80 / 100
    

    return found_exoplanet(readings, minimun_average)

def found_exoplanet(readings, average):
    found = False
    for element in readings:
        if (char_to_luminosity(element) <= average):
            found = True
            break

    return found

def average_readings(readings):
    count = 0
    for element in readings:
        count += char_to_luminosity(element)
         
    average = count / len(readings)

    return average

def char_to_luminosity(char):
    if 'A' <= char <= 'Z':
        return ord(char) - ord('A') + 10
    elif '0' <= char <= '9':
        return int(char)
    else:
        raise ValueError("Carácter inválido")



#** end of main.py **

