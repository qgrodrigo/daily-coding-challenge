#** start of main.py **

def classification(temp):
    message = ""

    if(temp <= 3699):
        message = "M"
    elif(temp <= 5199):
        message = "K"
    elif(temp <= 5999):
        message = "G"
    elif(temp <= 7499):
        message = "F"
    elif(temp <= 9999):
        message = "A"
    elif(temp <= 29999):
        message = "B"
    else:
        message = "O"
    

    return message

#** end of main.py **

