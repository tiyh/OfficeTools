#! /usr/bin/env python3
import time
import sys
import os
import glob
import random
import subprocess
#export LANG=zh_CN.gb2312
import importlib
importlib.reload(sys)

def get_status_output(*args, **kwargs):
    p = subprocess.Popen(*args, **kwargs)
    stdout, stderr = p.communicate()
    return p.returncode, stdout, stderr

def main():
    path = './'
    file_list = glob.glob(path+"/**/*.zip", recursive=True)

    for fName in file_list:
        modifiedTime = time.localtime(os.stat(fName).st_mtime)
        accessTime = time.localtime(os.stat(fName).st_atime)

        mTime = time.strftime('%Y-%m-%d %H:%M:%S', modifiedTime)
        aTime = time.strftime('%Y-%m-%d %H:%M:%S', accessTime)
        format = "%Y-%m-%d %H:%M:%S"
        print(fName+",time:"+mTime)

        mtime_t = time.mktime(time.strptime(mTime[:14]+str(random.randint(10,22))+":"+str(random.randint(10,59)), format))
        atime_t = time.mktime(time.strptime(mTime[:14]+str(random.randint(10,22))+":"+str(random.randint(10,59)), format))
        myCommand='LANG=en_US.UTF-8; export LANG; LC_ALL=en_US.UTF-8; export LC_ALL; java -Xmx2048m -jar signapk.jar -w testkey.x509.pem testkey.pk8 ' + fName +' '+fName+'.bak'
        try:
            PIDS=subprocess.getstatusoutput(myCommand)
            pidlist=[]
            for i in PIDS[1].split("\n"):
                try:
                    pidlist.append(i.split()[1])
                except Exception as e:
                    pass

            print(pidlist)
            # change timestamp of file
            os.rename(fName,fName+".tiyh")
            os.rename(fName+".bak", fName)
            os.utime(fName, (atime_t, mtime_t))

        except Exception as e:
            print("Exception ignore "+fName)
            print(e)

if __name__ == '__main__':
    main()
