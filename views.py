
from django.shortcuts import render,redirect
from django.contrib.auth.models import User 
from django.http import JsonResponse , HttpResponse 
from bs4 import BeautifulSoup
from unicodedata import category
from django.views import View
import http
import smtplib
import requests
import json

def home(request):
    return HttpResponse("Hello, world. You're at the home page")

 

def track(request):
    topic = request.GET.get('topic', None)

    print('============'+topic)
 

    headers = {
                  "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/74.0.3729.169 Safari/537.36"}


     
    page = requests.get(topic, headers=headers)
 
 
    soup = BeautifulSoup(page.content, 'html.parser')

 

    product_price = soup.find('span', attrs={'class':'a-offscreen'})
    
    p = float(product_price.text.split()[0][1:].replace(",", ""))
       
    print("----------ggggggggggggggggg----------------")

    print(p)

    print("------------ggggggggggggggg--------------")

 
    def send_mail():

          SMTP_SERVER = "smtp.gmail.com"
          PORT = 587

          EMAIL_ID = "amitjatola991714@gmail.com"
          PASSWORD = "hrozxdsedsditcdt"


          server = smtplib.SMTP(SMTP_SERVER, PORT)

 
          server.starttls()


 
          server.login(EMAIL_ID, PASSWORD )
          subject = f"Price down! to :{p}"
          body = topic
          reciever_mail = 'kartikpatidar97@gmail.com'
          msg = f"Subject:{subject}\n\n{'price down'}\n\n{body}"

 
          server.sendmail(
               EMAIL_ID,
               reciever_mail,
                msg
              )
    
          print("mail send")
     
          server.quit()

   
    Target_Price=150

    if p < float(Target_Price):
            send_mail()
    
     

    data = {
            "price": p
         }

    print('json-data to be sent: ', data)
 
    return JsonResponse(data)



    