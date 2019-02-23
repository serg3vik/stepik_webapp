from django.shortcuts import render
from django.http import HttpResponse

import smtplib

def sendmail(request):
    querymsg = request.GET.get('msg')
    responce = "No message given"
    if (querymsg):
        responce = querymsg
    print(responce)
    '''
    server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
    server.set_debuglevel(2)
    server.ehlo()

    fromaddr = 'free-for-spam@yandex.ru'
    toaddrs  = 'serg.oker@gmail.com'
     #server.starttls()
    server.login('free-for-spam@yandex.ru', '7455601')
    msg_header =  ("From: %s\r\nTo: %s\r\n\r\n"
       % (fromaddr, ", ".join(toaddrs)))
    msg = msg_header + 'HELLO FROM DJANGO!'

    server.sendmail('free-for-spam@yandex.ru', 'serg.oker@gmail.com', msg)
    server.quit()
    '''
    return HttpResponse(responce)
