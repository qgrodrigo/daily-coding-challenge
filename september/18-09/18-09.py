def cost_to_fill(tank_size, fuel_level, price_per_gallon):

    cost = (tank_size - fuel_level) * price_per_gallon
    cost_format = f'${cost:.2f}'

    print(cost_format)

    return cost_format

cost_to_fill(20, 0, 4.00) #should return "$80.00"
cost_to_fill(15, 10, 3.50) #should return "$17.50"
cost_to_fill(18, 9, 3.25) #should return "$29.25".
cost_to_fill(12, 12, 4.99) #should return "$0.00".
cost_to_fill(15, 9.5, 3.98) #should return "$21.89"