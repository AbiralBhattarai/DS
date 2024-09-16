#Almost everything covered in the basicOverview, but lets see how to input date & time in python
import datetime
time_str = input("Enter time HH:MM:SS ")
time_obj = datetime.datetime.strptime(time_str,"%H:%M:%S")
print(time_obj)
date_str = input("Enter date YYYY:MM:DD ")
date_obj = datetime.datetime.strptime(date_str,"%Y-%m-%d")
print(date_obj,time_obj)