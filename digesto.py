from selenium.webdriver import Chrome
import pandas as pd
from entrar import login
from entrar import senhaEntrar
from time import sleep
import pyautogui
import smtplib
from senha import senha
from senha import email
from flask import Flask
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("no-sandbox")
options.add_argument("--disable-extensions")
options.add_argument("--headless")
browser = Chrome(options=options)
url = 'https://outlook.office.com/mail/inbox/id/AAQkAGEzNjI1ODA4LTk2MzktNDNhZS04MGIyLWJjZmRkZDhjOWFmNgAQAFlkZ7rDvPBLoXih4RZe%2B%2Fo%3D'
#browser = Chrome()
browser.get(url)
#[u'{CDwindow-D001771s5632426A471AE75883435A710}', '{CDwindow-10DA637FD8FC8D96C72F8A541FBA1419}']

sleep (3)
escreva = browser.find_element_by_name("loginfmt")
escreva.send_keys(login)  #ele vai no login e coloca o email
clicar = browser.find_element_by_xpath('//*[@id="idSIButton9"]')
clicar.click() # e clica para entrar
sleep(3)
app = Flask("outlook")
@app.route("/entrarE", methods=["GET"])
def entrarE():
    return {'url':'https://outlook.office.com/mail/inbox/id/AAQkAGEzNjI1ODA4LTk2MzktNDNhZS04MGIyLWJjZmRkZDhjOWFmNgAQAFlkZ7rDvPBLoXih4RZe%2B%2Fo%3D',
    'ola':'mundo'}


@app.route("/entrarLogin", methods=["GET"])
def EntrarLogin():

    return clik(clicar)
app.run()
