#! /usr/bin/env python3
import urllib.request

def downloadImg(img_url, filename, api_token):
    header = {"Authorization": "Bearer " + api_token} # 设置http header
    request = urllib.request.Request(img_url, headers=header)
    try:
        response = urllib.request.urlopen(request)
        if (response.getcode() == 200):
            with open(filename, "wb") as f:
                f.write(response.read())
            return filename
    except:
        return "failed"

def canUrlVisit(img_url, api_token):
    header = {"Authorization": "Bearer " + api_token} # 设置http header
    request = urllib.request.Request(img_url, headers=header)
    try:
        response = urllib.request.urlopen(request)
        if (response.getcode() == 200):
            return True
    except:
        return False

if __name__ == '__main__':
    img_url = "https://cdn.nlark.com/yuque/0/2019/png/127877/1548156408615-1f09c601-abeb-4c73-a415-86b487850e9f.png"
    download_img(img_url, "./1.png","")