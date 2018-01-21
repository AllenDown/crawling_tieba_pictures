#! /usr/bin/env python
# -*- coding: utf-8 -*-

import imghdr
import os
import shutil

path = 'D:/python/grabing_tieba_pictures/NGZK_10/'


def rename_gif(path):
    files = os.listdir(path)
    for file in files:
        name = path + file
        # 判断是否是文件，不是的话不进行文件操作
        if os.path.isfile(name):
            # 判断文件类型
            if imghdr.what(name) == 'gif':
                print(file, ': gif')
                if not os.path.exists(path+'gif'):
                    print('创建文件夹')
                    os.mkdir(path+'gif')
                else:
                    pass
                # 重命名gif文件
                new_name = name.replace('jpg', 'gif')
                os.rename(name, new_name)
                # 将改名后的文件移动到gif文件夹下
                shutil.move(new_name, path+'gif')
            else:
                print(file, ': jpeg')
                continue
        else:
            continue

rename_gif(path)


