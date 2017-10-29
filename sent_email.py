# -*- coding: utf-8 -*-
"""
@author: ZiyanHuang
"""

import smtplib
from email.mime.text import MIMEText
from email.header    import Header
from email.utils     import parseaddr, formataddr


def sent_email(s):
    #email setting ----------------------------
    my_sender = 'm15395429293@163.com'                  # the mailbox sending the mail
    my_pass   = 'hzy201839'                  # smtp password of the mailbox
    receiver  = ['249090696@qq.com']                 # the mailbox receiving the mail. more than one also works
    #email setting ----------------------------
    
    #email content ----------------------------
    msg            = MIMEText(s, 'plain', 'utf-8')
    msg['From']    = _format_addr("SENDER <%s>" % my_sender)
    msg['To']      = _format_addr("RECEIVER <%s>" % receiver)
    msg['Subject'] = Header('real-time price of stock', 'utf-8').encode()
    #email content ----------------------------
    
    try:
        smtpObj = smtplib.SMTP('smtp.163.com', 25)
        smtpObj.login(my_sender, my_pass)
        smtpObj.sendmail(my_sender, receiver, msg.as_string())
        smtpObj.quit()
        print("Mail sent successfully")
    except:
        print("Error:Could not send mail")

def _format_addr(a):
    name, addr = parseaddr(a)
    return formataddr((Header(name, 'utf-8').encode(), addr))
