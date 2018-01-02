#! /usr/bin/env python
# -*- coding: utf-8 -*-

# this program is used to download the original picture

from bs4 import BeautifulSoup
import requests
import time  # setting sleep time to avoid too many requests in short time
import os
import configparser


urls = []  # saving the url that you want to use
num = 1
config = configparser.ConfigParser()

# get config info from config.ini
with open('config.ini', 'r') as file:
    config.read_file(file)
    general_url = str(config.get('tieba', 'url'))
    pages = config.getint('tieba', 'pages')
    folder = config.get('tieba', 'folder')
    if not os.path.exists(folder):
        os.mkdir(folder)
        print('create {} folder'.format(folder))
    else:
        print(folder+' has existed')
    for i in range(1, pages+1):
        urls.append(general_url.format(i))


def get_pictures(url):
    global num
    web_data = requests.get(url)
    Soup = BeautifulSoup(web_data.text, 'lxml')  # interpret the web_data of specified url
    images = Soup.find_all('img', 'BDE_Image')  # find the image tag
    for image in images:
        img = image.get('src')
        original_img = img[0:30]+'pic/item/'+img[-44:]  # get original image path
        print(original_img)
        with open('./'+folder+'/' + str(num) + '.jpg', 'wb') as f:
            f.write(requests.get(original_img).content)  # write the image into disk
            f.close()
        print('get {}th picture'.format(num))
        num = num + 1


for u in urls:
    get_pictures(u)  # grab the picture!
    time.sleep(2)
