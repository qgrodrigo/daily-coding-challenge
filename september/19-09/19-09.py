def number_of_photos(photo_size_mb, drive_size_gb):

    photos = (drive_size_gb * 1000) / photo_size_mb


    return int(photos)

number_of_photos(1, 1) # should return 1000.
number_of_photos(2, 1) #should return 500.
number_of_photos(4, 256) #should return 64000.
number_of_photos(3.5, 750) #should return 214285.
number_of_photos(3.5, 5.5) #should return 1571.