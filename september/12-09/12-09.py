def too_much_screen_time(hours):

    too_much = False

    #condicionals
    #Si un solo día tiene 10 horas o más, es demasiado.
    for i in hours:
        if(i >= 10):
            too_much = True

    #Si el promedio de tres días seguidos es mayor o igual a 8 horas, es demasiado.
    for i in range(len(hours)-2):
        mean = sum(hours[i:i+3]) / 3
        if(mean >= 8):
            too_much = True

    #Si el promedio de los siete días es mayor o igual a 6 horas, es demasiado.
    mean = sum(hours) / len(hours)
    if(mean >= 6):
        too_much = True

    #print(too_much)

    return too_much


too_much_screen_time([1, 2, 3, 4, 5, 6, 7]) #should return False.
#too_much_screen_time([7, 8, 8, 4, 2, 2, 3]) #should return False.
#too_much_screen_time([5, 6, 6, 6, 6, 6, 6]) #should return False.
#too_much_screen_time([3, 9, 4, 8, 5, 7, 6]) #should return True.