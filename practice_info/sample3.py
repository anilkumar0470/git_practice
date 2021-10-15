class sample3():
    def __init__(self):
        print("sample3 __init__")

    def execute_test(self):
        print("execute test")

import os
import time
import glob

now = time.time()
print(now)
# files = glob.glob(".")
# print(files)
# import datetime
# files =  os.listdir()
# print(files)
# file = files[1]
# print(file)
# age = now - os.path.getctime(file)
# print(age)
# dt_object = datetime.datetime.fromtimestamp(age)
# print(dt_object)
# date = datetime.datetime.strptime(dt_object, "%Y-%M-%d %H:%M:%S")
# print (date.timetuple().tm_yday)



import os


files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)

oldest = files[0]
newest = files[-1]

print ("Oldest:", oldest)
print ("Newest:", newest)
print ("All by modified oldest to newest:", files)

for file in files:
    if os.path.isdir(file):
        folder_files = os.listdir(os.path.join(os.getcwd(), file))
        for folder_file in folder_files:
            if folder_file.endswith("srs"):
                timestamp = os.path.getctime(os.path.join(os.getcwd(), file,folder_file))
                from datetime import datetime
                print(datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S'))
            #'2013-10-19 16:25:38'
