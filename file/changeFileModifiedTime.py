#! /usr/bin/env python3
import time
import sys
import os
import glob

def main():
    path = './test/'
    file_list = glob.glob(path+"/**", recursive=True)

    for fName in file_list:
        
        modifiedTime = time.localtime(os.stat(fName).st_mtime)
        accessTime = time.localtime(os.stat(fName).st_atime)
        #createdTime = time.localtime(os.stat(fName).st_ctime)


        mTime = time.strftime('%Y-%m-%d %H:%M:%S', modifiedTime)
        aTime = time.strftime('%Y-%m-%d %H:%M:%S', accessTime)
        #cTime = time.strftime('%Y-%m-%d %H:%M:%S', createdTime)
        print(fName + " modifiedTime is " +cTime)
        format = "%Y-%m-%d %H:%M:%S"

        # create struct_time object 修改成2020年
        mtime_t = time.mktime(time.strptime("2020"+mTime[4:], format))
        atime_t = time.mktime(time.strptime("2020"+aTime[4:], format))

        # change timestamp of file
        os.utime(fName, (atime_t, mtime_t))

if __name__ == '__main__':
    main()