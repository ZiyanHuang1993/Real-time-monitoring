# -*- coding: utf-8 -*-
"""
@author: ZiyanHuang
"""

import monitor_price as a
import time

#number_list[0] : stock's number
#number_list[1] : your target price
#number_list[2] : 0 : remind you when stock's price < your target price
#                 1 : remind you when stock's price > your target price

number_list=[['sh600522',10.6,1],
             ['sz002302',22.0,1],
             ['sz000961',7.10,0]]

flag = []
for i in range(len(number_list)):
    flag.append(False)

while(True):
    a.monitor_price(number_list, flag)
    time.sleep(20)
