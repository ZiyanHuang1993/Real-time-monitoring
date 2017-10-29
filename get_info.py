# -*- coding: utf-8 -*-
"""
@author: ZiyanHuang
"""

import urllib.request

def get_info(num):
    #Get the data provided by Sina Finance interface
    url = 'http://hq.sinajs.cn/?list=%s' % num
    req = urllib.request.Request(url)
    content = urllib.request.urlopen(req).read()
    
    #Extract the data to be used
    str  = content.decode('gbk')
    data = str.split('"')[1].split(',')
    name = "%-6s" %data[0]
    
    current_price  = "%-6s" % (float(data[3]))
    change_price   = "%-6s" % round(float(data[3]) - float(data[2]), 2)
    change_percent = (float(data[3]) - float(data[2])) * 100 / float(data[2])
    change_percent = "%-2s" %round(change_percent,2)
    change_percent += '%'
   
    #Return the required data
    info = "Stock name:{0} Price Change:{1} Price-Change rate:{2} the newest price:{3}".format(name, change_price, change_percent, current_price)
    return (info, float(current_price))