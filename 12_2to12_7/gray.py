#!/usr/local/bin/python
# -*- coding: UTF-8 -*-
# python灰帽编程QQ群  292041723（100人小群做过PY安全编程的进）
# 端口扫描器
import socket
import threading
import time
socket.setdefaulttimeout(3)  # 设置了全局默认超时时间


def socket_port(ip, PORT):  #扫描开放端口
    try:
        if PORT >= 65535:
            print(u"端口扫描结束0-65535")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # s.settimeout(float(1))  #延时5S
        # s.connect((ip,PORT))
        result = s.connect_ex((ip, PORT))
        if result == 0:
            print(ip, u":", PORT, u"端口开放")
        s.close()
    except:
        print(u"扫描端口异常2")


def IP__port(data):         # 扫描端口
    try:
        # data="127.0.0.1"
        t = time.time()
        for i in range(78, 100):   # 65535
            # threading.start_new_thread(socket_port, (data, int(i)))
            socket_port(data, int(i))
            time.sleep(0.03) # 确保先运行Seeker中的方法
        print(u'扫描端口完成用时 time:%f' % (time.time()-t))
    except:
        print(u"扫描端口异常1")


if __name__ == '__main__':
    #socket_port("192.168.1.1",80)  # 扫描开放端口
    IP__port("192.168.1.1") # 多线程
