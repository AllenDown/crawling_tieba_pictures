#! /usr/bin/env python
# -*- coding: utf-8 -*-

# this program is used to download the compressed picture

from bs4 import BeautifulSoup
import requests
import time  # setting sleep time to avoid too many requests in short time

urls = []  # saving the url that you want to use
general_url = 'http://tieba.baidu.com/p/5401922220?pn={}'  # the general url
num = 0  # used to name file of pictures


def get_pictures(url):
    global num
    web_data = requests.get(url)
    Soup = BeautifulSoup(web_data.text, 'lxml')  # interpret the web_data of specified url
    images = Soup.find_all('img', 'BDE_Image')  # find the image tag
    # download the picture
    for image in images:
        img = image.get('src')  # get real image path
        with open('./NGZK_11/'+str(num) + '.jpg', 'wb') as f:
            f.write(requests.get(img).content)  # write the image into disk
            f.close()
        print('getting {}th picture'.format(num))
        num = num + 1


# get pages what you want to deal with, and put url into a list
def get_pages(nums):
    for i in range(1, nums+1):
        urls.append(general_url.format(i))

get_pages(119)

for u in urls:
    time.sleep(2)
    get_pictures(u)  # grab the picture!
