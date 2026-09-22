def number_of_videos(video_size, video_unit, drive_size, drive_unit):

    if(video_unit == 'TB'):
        return 'Invalid video unit'

    elif(drive_unit == 'MB' or drive_unit == 'KB' or drive_unit == 'B'):
        return 'Invalid drive unit'

    else:
        return int(convert(drive_size, drive_unit) / convert(video_size, video_unit))


    


def convert(size, unit):
    convert_size = 0

    if(unit == 'KB'):
        convert_size = size * 1000
    elif(unit == 'MB'):
        convert_size = size * 1000 * 1000
    elif(unit == 'GB'):
        convert_size = size * 1000 * 1000 * 1000
    else:
        convert_size = size * 1000 * 1000 * 1000 * 1000

    return convert_size

#print(convert(200, 'MB'))

number_of_videos(500, "MB", 100, "GB") #should return 200
number_of_videos(1, "TB", 10, "TB") #should return "Invalid video unit"
number_of_videos(2000, "MB", 100000, "MB") #should return "Invalid drive unit"
number_of_videos(500000, "KB", 2, "TB") #should return 4000.
number_of_videos(1.5, "GB", 2.2, "TB") #should return 1466.