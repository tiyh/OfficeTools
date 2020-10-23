#! /usr/bin/env python
# -*- coding: utf-8 -*-

import commands
import os
rootDir = os.path.abspath('.')
sourceDir = rootDir+r"/source"
targetDir = rootDir+r"/target"
if __name__ == "__main__":
    try:
        import psyco
        psyco.profile()
    except ImportError:
        pass
commands.getstatusoutput('rm -f '+targetDir+'/*')
for apkbag in os.listdir(sourceDir):
    if (apkbag[-4:]=='.apk' or apkbag[-4:]=='.jar'):
        (status, output) = commands.getstatusoutput('java -Xmx2048m -jar signapk.jar -w platform.x509.pem platform.pk8 ./source/'+apkbag+' ./target/'+apkbag)
    if (apkbag[-4:]=='.zip'):
        (status, output) = commands.getstatusoutput('java -Xmx2048m -jar signapk.jar -w testkey.x509.pem testkey.pk8 ./source/'+apkbag+' ./target/'+apkbag)
    print status, output

#<Android_Source_Path>/build/target/product/security,找到platform.pk8和platform.x509.pem系统密钥。
#<Android_Source_Path>/build/tools/signapk找到SignApk.java
#./keytool-importkeypair -k ./mstar.keystore -p android -pk8 platform.pk8_sd8400 -cert platform.x509.pem_sd8400 -alias platform
