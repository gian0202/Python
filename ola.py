from selenium
import pandas as pd
from entrar import login
from entrar import senhaEntrar
from time import sleep
import pyautogui
import smtplib
from senha import senha
from senha import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

url = 'https://outlook.office.com/mail/inbox/id/AAQkAGEzNjI1ODA4LTk2MzktNDNhZS04MGIyLWJjZmRkZDhjOWFmNgAQAFlkZ7rDvPBLoXih4RZe%2B%2Fo%3D'
browser = Chrome()

browser.get(url)
browser.maximize_window()
#[u'{CDwindow-D001771s5632426A471AE75883435A710}', '{CDwindow-10DA637FD8FC8D96C72F8A541FBA1419}']

sleep (3)
escreva = browser.find_element_by_name("loginfmt")
escreva.send_keys(login)  #ele vai no login e coloca o email
clicar = browser.find_element_by_xpath('//*[@id="idSIButton9"]')
clicar.click() # e clica para entrar
sleep(3)
entrarSenha = browser.find_element_by_xpath('//*[@id="i0118"]')
entrarSenha.send_keys(senhaEntrar)  #coloca a senha
sleep(3)
browser.find_element_by_id('idSIButton9').click() #entrar
pyautogui.press('enter')  #ele aperta enter
try:
    browser.find_element_by_id('idSIButton9').click()
except:
    pass
sleep(7)
 #Entra na pasta chaamda digesto
browser.find_element_by_xpath('//*[@id="MainModule"]/div/div/div[1]/div/div/div/div/div[3]/div[8]/div/span[1]').click()
sleep(3)
browser.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div/div/div[1]/div[2]/div/div/div/div/div/div[1]/div/div/div[1]').click() #clicar email
window_before = browser.window_handles[0]
browser.find_element_by_xpath('//*[@id="x_templateBody"]/tbody/tr/td/div[1]/div[3]/b[1]/i/a').click()
window_after = browser.window_handles[1]
browser.switch_to.window(window_after)

sleep(2)
browser.find_element_by_xpath('/html/body/app-root/app-ip/app-header/header/div/div/div[2]/div/ul/li[5]/a').click()
 #Clica no login
sleep(2)
browser.find_element_by_xpath('/html/body/app-root/app-ip/app-header/header/div/div/div[2]/form/div/div[1]/input').send_keys(login) #coloca o email
sleep(2)
browser.find_element_by_xpath('/html/body/app-root/app-ip/app-header/header/div/div/div[2]/form/div/div[2]/button').click() #Clica em entrar
sleep(2)
browser.close() #Fecha a aba
sleep(2)
browser.switch_to.window(window_before)
sleep(10)
browser.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div[2]/div/div/div/div/div/div/div[1]/div[2]/div/div/div/div/div/div[1]/div/div/div[1]').click() #clicar no email de login
sleep(2)
window_before = browser.window_handles[0]
browser.find_element_by_xpath('//*[@id="x_templateBody"]/tbody/tr/td/p[1]/b/a').click()
window_after = browser.window_handles[1]
browser.switch_to.window(window_after)
sleep(2)
browser.close()

browser.switch_to.window(window_before)
sleep(3)
#Não esquecer de mudar
browser.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div[1]').click() #clicar email
sleep(3)


for x in range(80):
    teste=x+1
    try:
        print('estou passando no começo')

        browser.find_element_by_xpath('//*[@id="x_templateBody"]/tbody/tr/td/div[1]/div['+str(teste)+']/b[1]/i/a').click()
        sleep(3)
        window_after = browser.window_handles[1]
        browser.switch_to.window(window_after)
        sleep(3)
        #pega o processo :
        processo = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[1]/div[1]/div[1]/h3').text
        print(processo)

        #instancia:
        instancia = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[2]/div[1]/div/div/p[1]/span[1]').text
        print(instancia)
        #pega o tribnal
        txt =  browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[1]/div[1]/div[1]/h3').text
        x = txt.split()
        print(txt)
        #localidade:

        #data Distribuição: ''
        dataDistribuição = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[2]/div[1]/div/div/ul/li[2]/div[2]').text
        print(dataDistribuição)
        #audiencias:
        audiencias = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[2]/div[1]/div/div/ul/li[3]/div[2]/span').text
        print(audiencias)
        #valor da causa:
        valorCausa = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[2]/div[1]/div/div/ul/li[4]/div[2]').text
        print(valorCausa)
        #orgão julgador
        orgaojulgador = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[1]/div[2]/div[1]').text
        print(orgaojulgador)
        #classe
        classe = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[2]/div[1]/div/div/p[2]/span').text
        print(classe)
        #assunto
        assunto = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[2]/div[1]/div/div/p[3]').text
        print(assunto)
        #comarcae
        comarca = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[2]/div[1]/div/div/ul/li[1]/div[2]').text
        print(comarca)
        #dado autor, juiz, ent

        #nome
        nome12 = "  "
        nome13 = "  "
        nome14 = "  "
        try:
            #Nomes
            nome = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[3]/table/tbody/tr/td[1] ').text
            print(nome)
            nome12 = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[3]/table/tbody[2]/tr/td[1] ').text
            print(nome12)
            nome13 = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[3]/table/tbody[3]/tr/td[1] ').text
            print(nome12)
            nome14 = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[3]/table/tbody[4]/tr/td[1] ').text
            print(nome14)
            #OAB
        except:
            pass
        advogado12 = "  "
        advogado13 = "  "
        advogado14 = "  "

        try:
            #Advogados 1 ao 1.4
            advogado1 = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[3]/table/tbody/tr/td[2]').text
            print(advogado1)
            advogado12 = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[3]/table/tbody[2]/tr/td[2]').text
            print(advogado12)
            advogado13 = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[3]/table/tbody[3]/tr/td[2]').text
            print(advogado13)
            advogado14 = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[3]/table/tbody[4]/tr/td[2]').text
        except:
            pass
        OAB1 = " "
        OAB12 = " "
        OAB13 = "  "
        OAB14 = " "
        try:
            #OAB 1 a 1.4
            OAB1 = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[3]/table/tbody[1]/tr/td[3]/div').text
            print(OAB1)
            OAB12 = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[3]/table/tbody[2]/tr/td[3]/div').text
            print(OAB12)
            OAB13 = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[3]/table/tbody[3]/tr/td[3]/div').text
            print(OAB1)
            OAB14 = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[3]/table/tbody[4]/tr/td[3]/div').text
            print(OAB14)
        except:
            pass
        #nome2
        nome22 = "  "
        nome23 = "  "
        nome24 = "  "
        try:
            #Nome 2 a 2.4
            nome2 = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[4]/table/tbody/tr/td[1]').text
            print(nome2)
            nome22 = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[4]/table/tbody[2]/tr/td[1]').text
            print(nome22)
            nome23 = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[4]/table/tbody[3]/tr/td[1]').text
            print(nome23)
            nome24 = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[4]/table/tbody[4]/tr/td[1]').text
            print(nome24)
        except:
            pass
        advogado2 = "  "
        advogado22 = "  "
        advogado23 = "  "
        advogado24 = "  "
        try:
            #Advogado2 ao 2.4
            advogado2 = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[4]/table/tbody/tr/td[2]/div').text
            print(advogado2)
            advogado22 = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[4]/table/tbody[2]/tr/td[2]/div').text
            print(advogado22)
            advogado23 = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[4]/table/tbody[3]/tr/td[2]/div').text
            print(advogado23)
            advogado24 = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[4]/table/tbody[4]/tr/td[2]/div').text
            print(advogado24)
        except:
            pass
        OAB2 = " "
        OAB22 = " "
        OAB23 = " "
        OAB24 = " "
        try:
            OAB2 = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[4]/table/tbody/tr/td[3]/div').text
            print(OAB2)
            OAB22 = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[4]/table/tbody[2]/tr/td[3]/div').text
            print(OAB22)
            OAB23 = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[4]/table/tbody[3]/tr/td[3]/div').text
            print(OAB23)
            OAB24 = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[4]/table/tbody[4]/tr/td[3]/div').text
            print(OAB24)
        except:
            pass
        dado1 = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[3]/h4').text
        dado2 = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[4]/h4').text
        print('passei por aqui')
        #nome:
        dado3 = " "
        nome3 = " "
        nome32 = " "
        nome33 = " "
        nome34 = " "
        try:
            dado3 = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[5]/h4').text #pega o dado
            print(dado3)
            nome3 = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[5]/table/tbody[1]/tr/td[1]').text
            print(nome3)
            nome32 = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[5]/table/tbody[2]/tr/td[1]').text
            print(nome32)
            nome33 = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[5]/table/tbody[3]/tr/td[1]').text
            print(nome33)
            nome34 = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[5]/table/tbody[4]/tr/td[1]').text
            print(nome34)
        except:
            pass
        advogado3 = " "
        advogado32 = ""
        advogado33 = " "
        advogado34 = " "
        try:
            advogado3 = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[5]/table/tbody/tr/td[2]/div[1]').text
            print(advogado3)
            advogado32 = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[5]/table/tbody/tr/td[2]/div[2]').text
            print(advogado32)
            advogado33 = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[5]/table/tbody/tr/td[2]/div[3]').text
            print(advogado33)
            advogado34 = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[5]/table/tbody/tr/td[2]/div[4]').text
            print(advogado34)
        except:
            pass
        OAB3 = " "
        OAB32 = " "
        OAB33 = " "
        OAB34 = " "
        try:
            OAB3 = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[5]/table/tbody/tr/td[3]/div[1]').text
            OAB32 = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[5]/table/tbody/tr/td[3]/div[2]').text
            OAB33 = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[5]/table/tbody/tr/td[3]/div[3]').text
            OAB34 = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[5]/table/tbody[4]/tr/td[3]/div').text
        except:
            pass

        try:
            #Processos relacionados para quando tiver no 3 campo
            np = " "
            posicao3 = " "
            datadi = " "
            tribunal3 = " "
            Natureza2 = " "
            posicao3 = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[7]/h4').text
            np = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[7]/table/tbody/tr/td[1]').text
            datadi = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[7]/table/tbody/tr/td[2]').text
            tribunal3 = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[7]/table/tbody/tr/td[3]').text
            Natureza2 = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[7]/table/tbody/tr/td[4]').text
        except:
            pass
        try:
            dado4 = " "
            n1 = " "
            tribnal2 = " "
            dataD = " "
            Natureza = " "
            dado4 = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[9]/h4').text
            n1 = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[9]/table/tbody/tr/td[1]').text
            dataD = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[9]/table/tbody/tr/td[2]').text
            tribnal2 = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[9]/table/tbody/tr/td[3]').text
            Natureza = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[9]/table/tbody/tr/td[4]').text
        except:
             pass

        print(OAB3)
        add = pd.DataFrame ({'Processo': [x[3]],
        'Tribunal': [x[0]],
        'Órgão Julgador': [orgaojulgador],
        'Instancia': [instancia],
        'Classe': [classe],
        'Assunto': [assunto],
        'Comarca':[comarca],
        'Data de Distribuição': [dataDistribuição],
        'Audiencias': [audiencias],
        'Valor da causa': [valorCausa],
        'Posição': [dado1],     #Posição 1 :
        'Nome 1': [nome],
        'Nome 1.2': [nome12],
        'Nome 1.3': [nome13],
        'Advogado1':[advogado1],
        'Advogado 1.2': advogado12,
        'Advogado 1.3': advogado13,
        'OAB1': [OAB1],
        'OAB 1.2': [OAB12],
        'OAB 1.3': [OAB13],
        'Posição 3': [posicao3],
        'Posição 2': [dado2],   #Posição 2:
        'Nome 2': [nome2],
        'Nome 2.2': [nome22],
        'Nome 2.3':[nome23],
        'Advogado2': [advogado2],
        'Advogado 2.2': [advogado22],
        'advogado 2.3':[advogado23],
        'OAB2': [OAB2],
        'OAB 2.2': [OAB22],
        'Posição 3': [dado3],    #Posição 3:
        'Nome 3': [nome3],
        'Nome 3.3': [nome32],
        'advogado 3': [advogado3],
        'advogado 3.2': [advogado32],
        'advogado 3.3': [advogado33],
        'OAB 3': [OAB3],
        'OAB 3.2': [OAB32],
        'Posição 4': [dado4],
        'Nº Processo 3': [np],
        "Data de Distribuição 3": [datadi],
        'Tribunal 3 ': [tribunal3],
        'Natureza 3': [Natureza2],
        'Nº Processo 4 ': [n1],
        "Data de Distribuição 4": [dataD],
        'Tribunal 4': [tribnal2],
        'Natureza 4': [Natureza],
        })
        print('Movimentações')
        df = pd.read_excel("Movimentações.xlsx")
        print('Estou passando por aqui')
        df_final = df.append(add, ignore_index=False)
        df_final.to_excel('Movimentações.xlsx', index=False)
        print(df_final)
        browser.close()
        browser.switch_to.window(window_before)
        window_before = browser.window_handles[0]
    except:
        pass

fromaddr = email
toaddr = 'gianfloreal@gmail.com'
msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Importante"

body = "\n Olá, tudo bem? Estou enviando esses dados de teste!"

msg.attach(MIMEText(body, 'plain'))

filename = 'Movimentações.xlsx'

attachment = open('Movimentações.xlsx','rb')


part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)

attachment.close()

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, senha)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
print('\nEmail enviado com sucesso!')
