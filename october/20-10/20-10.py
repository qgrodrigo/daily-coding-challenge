def calculate_tips(meal_price, custom_tip):

    price = float(meal_price[1:])
    tips = []

    fifteen_percent_tip = f'${price * 15 / 100:.2f}'
    twenty_percent_tip = f'${price * 20 / 100:.2f}'
    custom = f'${float(custom_tip[:-1]) * price / 100:.2f}'

    tips.append(fifteen_percent_tip)
    tips.append(twenty_percent_tip)
    tips.append(custom)

    print(tips)

    return tips

#Tests:
calculate_tips("$10.00", "25%") #should return ["$1.50", "$2.00", "$2.50"].
calculate_tips("$89.67", "26%") #should return ["$13.45", "$17.93", "$23.31"].
calculate_tips("$19.85", "9%") #should return ["$2.98", "$3.97", "$1.79"].