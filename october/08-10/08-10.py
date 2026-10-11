def goldilocks_zone(mass):

    luminosity = mass ** 3.5
    init = 0.95 * luminosity ** 0.5
    end = 1.37 * luminosity ** 0.5

    distances = [round(init,2), round(end,2)]
    print(distances)

    return distances

goldilocks_zone(1) #should return [0.95, 1.37].
goldilocks_zone(0.5) #should return [0.28, 0.41].
goldilocks_zone(6) #should return [21.85, 31.51].
goldilocks_zone(3.7) #should return [9.38, 13.52].
goldilocks_zone(20) #should return [179.69, 259.13].