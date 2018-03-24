#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2018/3/25 0:00 
# @name: tmp
# @author：vickey-wu


from IPy import IP
ip_0 = IP("192.168.0.0/16")
print(ip_0.len())       # 65536
[print(x) for x in ip_0]        # all ip within 192.168.0.0/16, 192.168.0.0,192.168.0.1,192.168.0.2---192.168.255.255

ip_1 = IP("192.168.0.0")
print(ip_1.make_net("255.255.255.0"))       # create network segment by given ip and mask