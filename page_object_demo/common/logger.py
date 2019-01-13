# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     logger
   Description :
   Author :       jz
   date：          2019/1/13
-------------------------------------------------
   Change Activity:
                   2019/1/13:
-------------------------------------------------
"""
__author__ = 'jz'


import logging
from logging.handlers import RotatingFileHandler
import os
import time
import dir_config

fmt = "%(asctime)s %(levelname)s %(filename)s %(funcName)s [line:%(lineno)d] %(message)s"
datefmt = " %a, %d %b %Y %H:%M:%S"
handler_1 = logging.StreamHandler()
curTime = time.strftime("%Y-%m-%d %H%M",time.localtime())
handler_2 = RotatingFileHandler(dir_config.log_dir+"/Api_Autotest_log_{0}.log".format(curTime),backupCount=20,encoding="utf-8")
logging.basicConfig(format=fmt,datefmt=datefmt,level=logging.INFO,handlers=[handler_1, handler_2])
logging.info('hehehe')

