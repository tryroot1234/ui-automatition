# _*_coding:utf-8_*_
import logging
import os
import time


class Logger(object):
    # logger就是给log起的名字
    def __init__(self, logger):
        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.INFO)
        # 创建一个hanlder，用于写入日志文件
        # 生成一个当前日期的日期字符串
        request_time = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        # os.getcwd()获取当前工作目录,os.path.dirname(os.getcwd())获取当前目录的上一级目录
        log_path = os.path.dirname(os.getcwd())+'/logs/'
        # 拼成日志名称 =路径+时间戳.log<br><br>
        # 创建一个handler，用于生成在磁盘上
        log_name = log_path+request_time+'.log'
        # logging模块自带的三个handler之一。继承自StreamHandler。将日志信息输出到磁盘文件上。
        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)
        # 再创建一个handler，用于输出控制台
        sh = logging.StreamHandler()
        sh.setLevel(logging.INFO)
        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # 给handler设置格式
        fh.setFormatter(formatter)
        sh.setFormatter(formatter)
        # 给logger添加handler  换句话说就是给该logger添加不同的handler
        self.logger.addHandler(fh)
        self.logger.addHandler(sh)

    def getlog(self):
        return self.logger
