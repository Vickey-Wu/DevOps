#!/usr/bin/python
# -*- coding:utf8 -*-

import dns.resolver
import os
import http.client, http.server

ip_list = []
app_domain = "www.baidu.com"


def get_ip_list(domain=""):
    try:
        A = dns.resolver.query(domain, "A")
    except Exception as e:
        print("dns resolver error: " + str(e))
        return
    for i in A.response.answer:
        for j in i.items:
            ip_list.append(j)
    return True



def check_ip(ip):
    check_url = str(ip) + ": 80"
    get_content = ""
    http.client.socket.setdefaulttimeout(5)
    conn = http.client.HTTPConnection(check_url)

    try:
        conn.request("GET", "/", headers={"Host": app_domain})
        r = conn.getresponse()
        get_content = r.read(15)
    finally:
        print(get_content)
        if bytes.decode(get_content) == "<!DOCTYPE html>":
            print(str(ip) + " [OK]")
        else:
            print(str(ip) + " [ERROR]")


if __name__ == "__main__":
    if get_ip_list(app_domain) and len(ip_list) > 0:
        for ip in ip_list:
            check_ip(ip)
    else:
        print("dns reslover error.")

