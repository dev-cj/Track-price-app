import requests
from bs4 import BeautifulSoup
import smtplib
#change url here
URL = 'https://www.amazon.in/JBL-Portable-Wireless-Bluetooth-Speaker/dp/B00TFGWAA8/ref=sr_1_3?keywords=jbl+speaker&qid=1564099199&s=gateway&smid=A14CZOWI0VEHLG&sr=8-3'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
def check_price():

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')
    #for amazon
    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_dealprice").get_text()
    converted_price = float(price[1:7].replace(",", ""))
    #change price here
    if (converted_price < 1500):
        send_mail()
    print(title.strip())
    print(converted_price)

def send_mail():
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    #add login id and password
    s.login('your login email id', 'your mail password')
    subject = 'Hurray You can afford it!'
    body = 'Check the link'+ URL
    msg = f"Subject:{subject}\n\n{body}"
    s.sendmail(
        #replace from email and to email
        'from email',
        'to email',
        msg
        
    )
    print('Hey email has been sent!')

    s.quit()

check_price()