#! /usr/bin/env python3
import glob
import re
import os
import argparse
import pathlib

#https://pythonhosted.org/watchdog/
#包含两个参数
#    --workspace为要检查的makedown路径
#    ./markdown-checker.py --workspace=. 


parser = argparse.ArgumentParser(
    description='check Patch.',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--workspace', metavar='WORKSPACE', type=str, default='.', help='root workspace in jenlins server')


def checkUrlAccess(mdUrl,workspace,oneFile):
    url = mdUrl.strip()
    if url.startswith("http"):
        #todo
        i=1
    else :
        path = pathlib.Path(workspace+"/"+url)
        #print(workspace+"/"+url+" exist?:",path.exists())
        if not path.exists():
            tryFixUrl(mdUrl,workspace,oneFile)

def tryFixUrl(mdUrl,workspace,oneFile):
    print("tryFixUrl:"+ mdUrl)
    start = mdUrl.rindex('/')
    name = mdUrl[start+1:]
    mdFilelist = glob.glob(workspace+r"/**/"+name, recursive=True)
    if mdFilelist and len(mdFilelist)==1:
        updateFile(oneFile, mdUrl, mdFilelist[0])
    else:
        print("warning: fix "+name+" failed")

def updateFile(file,old_str,new_str):
    with open(file, "r", encoding="utf-8") as f1,open("%s.bak" % file, "w", encoding="utf-8") as f2:
        for line in f1:
            f2.write(re.sub(old_str,new_str,line))
    os.remove(file)
    os.rename("%s.bak" % file, file)

def checkMd(MD_PATH):
    mdFilelist = glob.glob(MD_PATH+r"/**/*.md", recursive=True)
    patchDict = {}
    for oneFile in mdFilelist:
        mdFile = open(oneFile)
        for line in mdFile.readlines():
            p1 = re.compile(r']\((.*?)\)', re.S)
            #p1 = re.compile(r'!\[(.*?)\]\((.*?)\)', re.S)
            matchObjs = re.findall(p1, line)
            if matchObjs:
                for oneMatch in matchObjs:
                    checkUrlAccess(oneMatch,MD_PATH,oneFile)
        mdFile.close()

def main():
    args = parser.parse_args()
    checkMd(args.workspace)

if __name__ == '__main__':
    main()