from selenium.webdriver import Chrome
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
from selenium.webdriver.chrome.options import Options
#options = Options()
#options.add_argument("no-sandbox")
#options.add_argument("--disable-extensions")
#options.add_argument("--headless")
#browser = Chrome(options=options)
url = 'https://op.digesto.com.br/user/login?login_token=gian.silva%40liss.net.br.FW0NXg.z6kvrLh4Jt2Rd8uf7UfnHXMhQQI'
browser = Chrome()
browser.get(url)
browser.maximize_window()
df1 = pd.read_excel('Digesto.xlsx', sheet_name = 'Digesto', usecols = "E")


df2 = pd.read_excel('//home//gian//Downloads//extrato_uso_distrib.xlsx', usecols = "E")

# interseção da df2 com a df1
df3 = df2.loc[df2['Detalhes do recurso'].isin(df1['Detalhes do recurso'])]
print(df3)

#diferença df3 com o df2
df4= pd.concat([df2,df3]).drop_duplicates(keep=False)
print(df4)

a = (df4.iloc[2].values)
print(str(a))
b = str(a).split('.')
print(b[2])
processos= list(df4['Detalhes do recurso'])
for processo in processos:
    num = str(processos).split('.')
    print(processo)
    print(num[2])
    browser.get('https://op.digesto.com.br/#/tribproc/proc/'+str(processo)+'?tipo_numero='+str(num[2])+'')
    print("passei no link")
    sleep(2)
    nome = []
    nome2 = []
    nome33 = []
    nome44 = []
    nome55 = []
    advogado = []
    advogado2=[]
    advogado3 =[]
    advogado4 = []
    advogado5 = []
    OAB = []
    OAB2=[]
    OAB3 = []
    OAB4 = []
    OAB5 = []
    data = []
    tipo = []
    mv = []
    data2 = []
    tipo2=[]
    mv2 = []
    data3=[]
    tipo3=[]
    mv3=[]
    paginas = [1, 2, 3, 4, 5, 6, 7, 8]
    paginas2 = [1, 2, 3, 4, 5, 6, 7 ,1,2,3,4,5,6,7,8]
    paginas3 = [1, 2, 3, 4, 5, 6, 7,1,2,3,4,5,6,7,8,1,2,3,4]

    txtd=browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[1]/div[2]/div[2]').text
    print('estou passando no começo')
    txt =  browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[1]/div[1]/div[1]/h3').text
    x = txt.split()
    print(x)
    #instancia:
    instancia = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[2]/div[1]/div/div/p[1]/span[1]').text
    print(instancia)

    #pega o tribnal
    sleep(2)
    txt =  browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[1]/div[1]/div[1]/h3').text
    x = txt.split()
    print(x)
    sleep(2)
    tribunal = x[0]
    print(tribunal)
    uf = str(tribunal).split('TJ')
    try:
        uf2=None
        uf2 = uf[1]
        print (uf2)
    except:
        pass
    #localidade:

    #data Distribuição: ''
    dataDistribuição = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[2]/div[1]/div/div/ul/li[2]/div[2]').text
    print(dataDistribuição)
    #audiencias:
    audiencias = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[2]/div[1]/div/div/ul/li[3]/div[2]').text
    print(audiencias)
    #valor da causa:
    valorCausa = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[2]/div[1]/div/div/ul/li[4]/div[2]').text
    print(valorCausa)
    #orgão julgador
    orgaojulgador = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[1]/div[2]/div[1]').text
    print(orgaojulgador)
    #classe
    classe = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[2]/div[1]/div/div/p[2]').text
    print(classe)
    #assunto
    try:
        assunto = None
        assunto = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[2]/div[1]/div/div/p[3]/span').text
        print(assunto)
    except:
        pass
    try:
        assunto2 = None
        assunto2 = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[2]/div[1]/div/div/p[2]/span').text
    except:
        pass

    #comarcae
    comarca = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[2]/div[1]/div/div/ul/li[1]/div[2]').text
    print(comarca)
    #dado autor, juiz, ent
    for x in range(10):
        teste=x+1
        try:
            v=0
            dado1 = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[3]/h4').text
            nome.append(browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[3]/table/tbody['+str(teste)+']/tr/td[1] ').text)
            print(nome)
        except:
            nome.append(None)

        pass
        try:
            advogado.append(browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[3]/table/tbody['+str(teste)+']/tr/td[2]').text)
            print(advgado)
        except:
            advogado.append(None)
            pass
        try:
            OAB.append(browser.find_element_by_xpath(' /html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[3]/table/tbody['+str(teste)+']/tr/td[3]/div').text)
        except:
            OAB.append(None)
            pass
    for x in range(10):
        teste=x+1
        try:
            dado2 = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[4]/h4').text

            nome2.append(browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[4]/table/tbody['+str(teste)+']/tr/td[1]').text)
            print(nome2)
        except:
            nome2.append(None)
            pass
        try:
            advogado2.append(browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[4]/table/tbody['+str(teste)+']/tr/td[2]/div').text)
            print(advogado2)
        except:
            advogado2.append(None)
            pass
        try:
            OAB2.append(browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[4]/table/tbody['+str(teste)+']/tr/td[3]/div').text)
            print(OAB2)
            v=2
        except:
            OAB2.append(None)
            pass
        print(v)
        try:
            dado3 = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[5]/h4').text
            nome33.append(browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[5]/table/tbody['+str(teste)+']/tr/td[1]').text)

        except:
            nome33.append(None)
            pass
        try:
            advogado3.append(browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[5]/table/tbody['+str(teste)+']/tr/td[2]/div').text)

        except:
            advogado3.append(None)
            pass
        try:
            OAB3.append(browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[5]/table/tbody['+str(teste)+']/tr/td[3]').text)
            v=4
        except:
            OAB3.append(None)
            pass
        print(v)
        try:
            dado4 = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[6]/h4').text

            nome44.append(browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[6]/table/tbody['+str(teste)+']/tr/td[1]').text)
            pass
        except:
            nome44.append(None)
            pass
        try:

            advogado4.append(browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[6]/table/tbody['+str(teste)+']/tr/td[2]/div').text)
        except:
            advogado4.append(None)
            pass
        try:
            OAB4.append(browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[6]/table/tbody['+str(teste)+']/tr/td[3]/div').text)
            v=6
        except:
            OAB4.append(None)
            pass
        print(v)
        try:
            dado5 = ""
            dado5 = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[7]/h4').text
            nome55.append(browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[7]/table/tbody['+str(teste)+']/tr/td[1]').text)
        except:
            nome55.append(None)
            pass
        try:
            advogado5.append(browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[7]/table/tbody['+str(teste)+']/tr/td[2]/div').text)

        except:
            advogado5.append(None)
            pass
        try:
            OAB5.append(browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[7]/table/tbody['+str(teste)+']/tr/td[3]/div').text)
            v=8
        except:
            OAB5.append(None)
            pass
    print(v)

    for x in range(20):

        soma = v+6

        try:
            browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div['+str(soma)+']/table/tbody['+str(paginas[x])+']/tr[1]/td[4]/div[2]/a').click()
            sleep(1)
            data.append(browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div['+str(soma)+']/table/tbody['+str(paginas[x])+']/tr[1]/td[1]').text)
            print(data)
            sleep(1)
            tipo.append (browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div['+str(soma)+']/table/tbody['+str(paginas[x])+']/tr[1]/td[2]/p').text)
            print(tipo)
            sleep(1)
            mv.append(browser.find_element_by_xpath(' /html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div['+str(soma)+']/table/tbody['+str(paginas[x])+']/tr[2]/td/table/tbody/tr/td/p').text)
            print(mv)
            sleep(1)
            print(x)
        except:
            data.append(None)
            tipo.append(None)
            mv.append(None)
            pass
        try:
            if(x==7):
                print(x)
                print("Passei no if == 8")
                pg2 = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/nav/ul/li[3]/a')
                sleep(3)
                pg2.click()

                print(paginas2[x])
                browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div['+str(soma)+']/table/tbody['+str(paginas2[x])+']/tr[1]/td[4]/div[2]/a').click()
                sleep(1)
                data.append(browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div['+str(soma)+']/table/tbody['+str(paginas2[x])+']/tr[1]/td[1]').text)
                print(data)
                sleep(1)
                tipo.append (browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div['+str(soma)+']/table/tbody['+str(paginas2[x])+']/tr[1]/td[2]/p').text)
                print(tipo)
                sleep(1)
                mv.append(browser.find_element_by_xpath(' /html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div['+str(soma)+']/table/tbody['+str(paginas2[x])+']/tr[2]/td/table/tbody/tr/td/p').text)
                print(mv)
                sleep(1)
        except:
            data.append(None)
            tipo.append(None)
            mv.append(None)
            pass
        try:
            if(x >= 8):
                print("Passei no if > 8")
                sleep(2)
                pgmaior8 = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/nav/ul/li[4]/a')
                pgmaior8.text
                print(paginas2[x])

                browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div['+str(soma)+']/table/tbody['+str(paginas2[x])+']/tr[1]/td[4]/div[2]/a/span[2]/i').click()
                sleep(1)
                data.append(browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div['+str(soma)+']/table/tbody['+str(paginas2[x])+']/tr[1]/td[1]').text)
                print(data)
                sleep(1)
                tipo.append (browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div['+str(soma)+']/table/tbody['+str(paginas2[x])+']/tr[1]/td[2]/p').text)
                print(tipo)
                sleep(1)
                mv.append(browser.find_element_by_xpath(' /html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div['+str(soma)+']/table/tbody['+str(paginas2[x])+']/tr[2]/td/table/tbody/tr/td/p').text)
                print(mv)
                sleep(1)
        except:
            data.append(None)
            tipo.append(None)
            mv.append(None)
            pass

        try:
            if(x==15):
                print("Passei no if == 16")
                pg3 = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/nav[1]/ul/li[5]/a')
                sleep(2)
                pg3.click()
                sleep(3)
                browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div['+str(soma)+']/table/tbody['+str(paginas3[x])+']/tr[1]/td[4]/div[2]/a').click()
                sleep(1)
                data.append(browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div['+str(soma)+']/table/tbody['+str(paginas3[x])+']/tr[1]/td[1]').text)
                print(data)
                sleep(1)
                tipo.append (browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div['+str(soma)+']/table/tbody['+str(paginas3[x])+']/tr[1]/td[2]/p').text)
                print(tipo)
                sleep(1)
                mv.append(browser.find_element_by_xpath(' /html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div['+str(soma)+']/table/tbody['+str(paginas3[x])+']/tr[2]/td/table/tbody/tr/td/p').text)
                print(mv)
                sleep(1)
        except:
            data.append(None)
            tipo.append(None)
            mv.append(None)
            pass
        try:
            if(x > 15):
                pg3 = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/nav[1]/ul/li[5]/a')
                pg3.text
                browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div['+str(soma)+']/table/tbody['+str(paginas3[x])+']/tr[1]/td[4]/div[2]/a').click()
                sleep(1)
                data.append(browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div['+str(soma)+']/table/tbody['+str(paginas3[x])+']/tr[1]/td[1]').text)
                print(data)
                sleep(1)
                tipo.append (browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div['+str(soma)+']/table/tbody['+str(paginas3[x])+']/tr[1]/td[2]/p').text)
                print(tipo)
                sleep(1)
                mv.append(browser.find_element_by_xpath(' /html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div['+str(soma)+']/table/tbody['+str(paginas3[x])+']/tr[2]/td/table/tbody/tr/td/p').text)
                print(mv)
                sleep(1)
        except:
            data.append(None)
            tipo.append(None)
            mv.append(None)
            pass


    p = pd.DataFrame({
    'Detalhes do recurso': [processo],



    })
    add = pd.DataFrame ({'Processo': [processo],
    'Tribunal': [tribunal],
    'UF': [uf2],
    'Instancia': [instancia],
    'Órgão Julgador': [orgaojulgador],
    'Classe': [classe],
    'Assunto': [assunto],
    'Comarca':[comarca],
    'Data de Distribuição': [dataDistribuição],
    'Audiencias': [audiencias],
    'Valor da causa': [valorCausa],
    #Posição 1
    'Posição': [dado1],
    'Nome 1': [nome[0]],
    'Nome 1.2': [nome[1]],
    'Nome 1.3': [nome[2]],
    'Nome 1.4': [nome[3]],
    'Nome 1.5': [nome[4]],
    'Nome 1.6': [nome[5]],
    'Nome 1.7': [nome[6]],
    'Nome 1.8': [nome[7]],
    'Nome 1.9': [nome[8]],
    'Nome 1.10': [nome[9]],
    'Advogado 1': [advogado[0]],
    'Advogado 1.2': [advogado[1]],
    'Advogado 1.3': [advogado[2]],
    'Advogado 1.4': [advogado[3]],
    'Advogado 1.5': [advogado[4]],
    'Advogado 1.6': [advogado[5]],
    'Advogado 1.7': [advogado[6]],
    'Advogado 1.8': [advogado[7]],
    'Advogado 1.9': [advogado[8]],
    'Advogado 1.10': [advogado[9]],
    'OAB 1': [OAB[0]],
    'OAB 1.2': [OAB[1]],
    'OAB 1.3': [OAB[2]],
    'OAB 1.4': [OAB[3]],
    'OAB 1.5': [OAB[4]],

    #Posição 2:
    'Posição 2': [dado2],
    'Nome 2': [nome2[0]],
    'Nome 2.2': [nome2[1]],
    'Nome 2.3': [nome2[2]],
    'Nome 2.4': [nome2[3]],
    'Nome 2.5': [nome2[4]],
    'Nome2.6': [nome2[5]],
    'Nome2.7': [nome2[6]],
    'Nome2.8': [nome2[7]],
    'Nome2.9': [nome2[8]],
    'Nome2.10': [nome2[9]],
    'Advogado 2': [advogado2[0]],
    'Advogado 2.2': [advogado2[1]],
    'Advogado 2.3': [advogado2[2]],
    'Advogado 2.4': [advogado2[3]],
    'Advogado 2.5': [advogado2[4]],
    'Advogado 2.6': [advogado2[5]],
    'Advogado 2.7': [advogado2[6]],
    'Advogado 2.8': [advogado2[7]],
    'Advogado 2.9': [advogado2[8]],
    'Advogado 2.10': [advogado2[9]],
    'OAB 2': [OAB2[0]],
    'OAB 2.2': [OAB2[1]],
    'OAB 2.3': [OAB2[2]],
    'OAB 2.4': [OAB2[3]],
    'OAB 2.5': [OAB2[4]],
    #3
    'Posicão 3': [dado3],
    'Nome 3': [nome33[0]],
    'Nome 3.2': [nome33[1]],
    'Nome 3.3': [nome33[2]],
    'Nome 3.4': [nome33[3]],
    'Nome 3.5': [nome33[4]],
    'Advogado 3': [advogado3[0]],
    'Advogado 3.2': [advogado3[1]],
    'Advogado 3.3': [advogado3[2]],
    'Advogado 3.4': [advogado3[3]],
    'Advogado 3.5': [advogado3[4]],
    'OAB 3': [OAB3[0]],
    'OAB 3.2': [OAB3[1]],
    'OAB 3.3': [OAB3[2]],
    'OAB 3.4': [OAB3[3]],
    'OAB 3.5': [OAB3[4]],
    #4
    'Posição 4': [dado4],
    'Nome 4': [nome44[0]],
    'Nome 4.2': [nome44[1]],
    'Nome 4.3': [nome44[2]],
    'Nome 4.4': [nome44[3]],
    'Nome 4.5': [nome44[4]],
    'Advogado 4': [advogado4[0]],
    'Advogado 4.2': [advogado4[1]],
    'Advogado 4.3': [advogado4[2]],
    'Advogado 4.4': [advogado4[3]],
    'Advogado 4.5': [advogado4[4]],
    'OAB 4': [OAB4[0]],
    'OAB 4.2': [OAB4[1]],
    'OAB 4.3': [OAB4[2]],
    'OAB 4.4': [OAB4[3]],
    'OAB 4.5': [OAB4[4]],
    #5
    'Posição 5': [dado5],
    'Nome 5': [nome55[0]],
    'Nome 5.2': [nome55[1]],
    'Nome 5.3': [nome55[2]],
    'Nome 5.4': [nome55[3]],
    'Nome 5.5': [nome55[4]],
    'Advogado 5': [advogado5[0]],
    'Advogado 5.2': [advogado5[1]],
    'Advogado 5.3': [advogado5[2]],
    'Advogado 5.4': [advogado5[3]],
    'Advogado 5.5': [advogado5[4]],
    'OAB 5': [OAB5[0]],
    'OAB 5.2': [OAB5[1]],
    'OAB 5.3': [OAB5[2]],
    'OAB 5.4': [OAB5[3]],
    'OAB 5.5': [OAB5[4]],
    #Movimentações
    'Data 1': [data[0]],
    'Data 2': [data[1]],
    'Data 3': [data[2]],
    'Data 4': [data[3]],
    'Data 5': [data[4]],
    'Data 6': [data[5]],
    'Data 7': [data[6]],
    'Data 8': [data[7]],
    'Data 9': [data[8]],
    'Data 10': [data[9]],
    'Data 11': [data[10]],
    'Data 12': [data[11]],
    'Data 13': [data[12]],
    'Data 14': [data[13]],
    'Data 15': [data[14]],
    'Data 16': [data[15]],
    'Data 17':[data[16]],
    'Data 18':[data[17]],
    'Data 19':[data[18]],
    'Data 20':[data[19]],
    'tipo 1': [tipo[0]],
    'tipo 2': [tipo[1]],
    'tipo 3': [tipo[2]],
    'tipo 4': [tipo[3]],
    'tipo 5': [tipo[4]],
    'tipo 6': [tipo[5]],
    'tipo 7': [tipo[6]],
    'tipo 8': [tipo[7]],
    'tipo 9': [tipo[8]],
    'tipo 10': [tipo[9]],
    'tipo 11': [tipo[10]],
    'tipo 12': [tipo[11]],
    'tipo 13': [tipo[12]],
    'tipo 14': [tipo[13]],
    'tipo 15': [tipo[14]],
    'tipo 16': [tipo[15]],
    'tipo 17': [tipo[16]],
    'tipo 18': [tipo[17]],
    'tipo 19': [tipo[18]],
    'tipo 20': [tipo[19]],
    'Movimentação 1': [mv[0]],
    'Movimentação 2': [mv[1]],
    'Movimentação 3': [mv[2]],
    'Movimentação 4': [mv[3]],
    'Movimentação 5': [mv[4]],
    'Movimentação 6': [mv[5]],
    'Movimentação 7': [mv[6]],
    'Movimentação 8': [mv[7]],
    'Movimentação 9': [mv[8]],
    'Movimentação 10': [mv[9]],
    'Movimentação 11': [mv[10]],
    'Movimentação 12': [mv[11]],
    'Movimentação 13': [mv[12]],
    'Movimentação 14': [mv[13]],
    'Movimentação 15': [mv[14]],
    'Movimentação 16': [mv[15]],
    'Movimentação 17': [mv[16]],
    'Movimentação 18': [mv[17]],
    'Movimentação 19': [mv[18]],
    'Movimentação 20': [mv[19]],
    #Movimentações 2

    })



    print('Digesto.xlsx')
    print('Estou passando por aqui')
    dfDiges = pd.read_excel('Digesto.xlsx', sheet_name = 'Digesto')
    dff = dfDiges.append(p, ignore_index=False)
    dff.to_excel('Digesto.xlsx', sheet_name = 'Digesto', index=False)
    print(df_final)
