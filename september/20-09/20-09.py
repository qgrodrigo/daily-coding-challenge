def number_of_files(file_size, file_unit, drive_size_gb):

    files = convert(file_unit, drive_size_gb) / file_size
    print(int(files))
    
    return int(files)

def convert( type, size):

    size_total = 0
    if(type == 'B'):

        size_total = size * 1000 * 1000 * 1000
    elif(type == 'KB'):
        size_total = size * 1000 * 1000
    else:
        size_total = size * 1000

    return size_total

number_of_files(500, "KB", 1) #should return 2000.
number_of_files(50000, "B", 1) #should return 20000.
number_of_files(5, "MB", 1) #should return 200.
number_of_files(4096, "B", 1.5) #should return 366210.
number_of_files(220.5, "KB", 100) #should return 453514.
number_of_files(4.5, "MB", 750) #should return 166666.
