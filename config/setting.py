#!/usr/bin/python3
# coding=utf-8
# Author: @Tao.

import pathlib
import os
"""
配置文件
"""
# 路径设置
relative_directory = pathlib.Path(__file__).parent.parent  # EmailAll代码相对路径
modules_storage_dir = relative_directory.joinpath('modules')  # modules存放目录
result_save_dir = relative_directory.joinpath('result')

rule_func = list()

emails = list()
proxy_str = os.getenv('proxy')
proxy=None
if proxy_str:
    if  not 'socks' in proxy_str:
        proxy = {'http': '127.0.0.1:2333', 'https': '127.0.0.1:2333'}
        proxy = {'http': proxy_str, 'https': proxy_str}

    else:
        proxy='socks5://127.0.0.1:1080'
        proxy=proxy_str
else:
    proxy=None