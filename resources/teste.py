from flask import Flask, make_response
from flask_restful import Resource, reqparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
import time as time
import pandas as pd
from datetime import datetime
from entrar import login
from entrar import senhaEntrar
from time import sleep
import pyautogui
import smtplib
from senha import senha
from senha import email
from selenium.webdriver.common.by import By
class Teste(Resource):
    def get(self):
        options = Options()
        options.add_argument("no-sandbox")
        options.add_argument("--disable-extensions")
        options.add_argument("--headless")
        browser = webdriver.Chrome(options=options)
        url = "https://outlook.office.com/mail/inbox/id/AAQkAGEzNjI1ODA4LTk2MzktNDNhZS04MGIyLWJjZmRkZDhjOWFmNgAQAFlkZ7rDvPBLoXih4RZe%2B%2Fo%3D"
        browser.get(url)
        time.sleep(5)
        escreva = browser.find_element_by_name("loginfmt")
        escreva.send_keys(login)  #ele vai no login e coloca o email
        clicar = browser.find_element_by_xpath('//*[@id="idSIButton9"]')
        clicar.click() # e clica para entrar
        sleep(3)
        entrarSenha = browser.find_element_by_xpath('//*[@id="i0118"]')
        entrarSenha.send_keys(senhaEntrar)  #coloca a senha
        sleep(3)
        e = browser.find_element_by_id('idSIButton9')
        sleep(2)
        e.click() #entrar
        sleep(2)
        #Caso aparecer a tela "Continuar conectado ele vai no try"
        try:
            sleep(1)
            confirmar = browser.find_element_by_id('idSIButton9')
            sleep(2)
            confirmar.click()
        except:
            pass
        print("Logado no email com Sucesso, proximo passo, vou Abrir o digesto para fazer o login nele!!")
        sleep(3)
        print("Vou abrir o digesto")
        browser.get('https://www.digesto.com.br/')
        print("Olha so entrei no digesto")
        browser.find_element_by_xpath('/html/body/app-root/app-home/app-header/header/div/div[1]/div[2]/div/ul/li[5]/a').click()
        sleep(2)
        browser.find_element_by_xpath('/html/body/app-root/app-home/app-header/header/div/div[1]/div[2]/form/div/div[1]/input').click()

        browser.find_element_by_xpath('/html/body/app-root/app-home/app-header/header/div/div[1]/div[2]/form/div/div[1]/input').send_keys(login) #coloca o email
        sleep(2)
        browser.find_element_by_xpath('/html/body/app-root/app-home/app-header/header/div/div[1]/div[2]/form/div/div[2]/button').click() #Clica em entrar
        sleep(2)
        browser.get(url)
        #logo apos ter colocado seu email para fazer o login
        #Ele vai acessar o email novamente e esperar 10 segundos para o email chegar
        sleep(10)
        #o email chegando ele vai clicar no email
        email = browser.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div[2]/div/div/div/div/div/div/div[1]/div[2]/div/div/div/div/div/div[1]/div/div/div[1]/div[2]/div[1]/div[1]/span')
        sleep(2)
        print("Passei")
        email.click()
        #login feito com sucesso!
        sleep(2)
        entrarD = browser.find_element_by_xpath('//*[@id="x_templateBody"]/tbody/tr/td/pre').text
        print(entrarD)
        browser.get(entrarD)
        print("Olha só loguei")
        sleep(5)
        browser.find_element_by_xpath('/html/body/div[3]/div/a').click()
        sleep(2)
        browser.find_element_by_xpath('//*[@id="e2e-monitored-distr"]/span[1]').click()
        sleep(2)
        browser.find_element_by_xpath('//*[@id="monitored-person-sets"]/div[1]/div[1]/div/div[2]/div/button/span').click()
        sleep(2)
        browser.find_element_by_xpath('//*[@id="monitored-person-sets"]/div[1]/div[1]/div/div[2]/div/div/input').click()
        sleep(2)
        mes1 = browser.find_element_by_xpath('//*[@id="monitored-person-sets"]/div[1]/div[1]/div/div[2]/div/div/input')
        mes1.send_keys(1)
        sleep(1)
        #aqui ele vai clicar para abaixar a planilha do digesto de 1 mes
        browser.find_element_by_xpath('//*[@id="button-addon2"]').click()
        sleep(2)
        browser.get("https://outlook.office.com/mail/")
        print("Estou no outlook, proximo passo, clicar no 1 email")
        sleep(20)
        entrar1Em = browser.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div[2]/div/div/div/div/div/div/div[1]/div[2]/div/div/div/div/div/div[1]/div/div/div[1]/div[2]/div[1]/div[1]/span')
        sleep(2)
        entrar1Em.click()
        sleep(4)
        print("entrei no 1 email, agora vou abaixar a planilha!")
        sleep(3)
        emailb = browser.find_element_by_class_name('We09X')
        emailb.click()
        sleep(4)
        print("Entrei na planilha agora estou pronto para abaixar")
        sleep(3)

        browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div/div[2]/div[2]/div[2]/div[1]/div[3]/div/div/div/div[1]/div[1]/div/span/button[1]/span').click()

        print("Acabei de clicar em editar")
        sleep(3)

        print("Estou preparado para clicar em abaixar, sera que agora vai?")
        sleep(5)
        browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div/div[2]/div[2]/div[2]/div[1]/div[3]/div/div/div/div[1]/div/button/span/i').click()
        sleep(2)
        browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div/div[2]/div[2]/div[2]/div[1]/div[3]/div/div/div/div[1]/div/button/span/span/span').click()
        sleep(2)
        browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div/div[2]/div[2]/div[2]/div[1]/div[3]/div/div/div/div[1]/div').click()
        sleep(2)
        browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div/div[2]/div[2]/div[2]/div[1]/div[3]/div/div/div/div[1]/div/button').click()
        print("Até que enfim, depois de tanto tempo, abaixado com sucesso!")
        ddd = "Sucesso!!!"
        my_resp = make_response(ddd)
        my_resp.status_code = 200
        return my_resp
class c(Resource):
    def get(self):
        options = Options()
        #options.add_argument("no-sandbox")
        #options.add_argument("--disable-extensions")
        #options.add_argument("--headless")
        browser = Chrome(options=options)
        url = 'https://op.digesto.com.br/user/login?login_token=gian.silva%40liss.net.br.FXgG3g.Jty7zU8CjXoMmykBncsX_A612hs'

        browser.get(url)
        browser.maximize_window()
        df1 = pd.read_excel('Digesto.xlsx', sheet_name = 'Digesto', usecols = "E")


        df2 = pd.read_excel('extrato_uso_distrib.xlsx', usecols = "E")

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

        #diferencaL = clientev.loc[localidadev['comarca'].isin(localidaded['comarca'])]
        #print(diferencaL)
        #localidade1ist = list(diferencaC['comarca'])
        clientes = pd.read_excel('extrato_uso_distrib.xlsx')
        print(clientes)
        dfCliente = clientes.loc[clientes['Detalhes do recurso'].isin(df4['Detalhes do recurso'])]
        print(dfCliente['Termo monitorado'])
        ClienteT = dfCliente['Termo monitorado'].str.upper()
        ClientesL = list(ClienteT)
        count = -1
        ClienteV4Company = dfCliente['Centro de custo']
        ClienteV4CompanyList = list(ClienteV4Company)
        for processo in processos:
            count = count + 1
            cliente = ClientesL[count]
            print(cliente)
            print(count)
            ClienteV4CompanyFinal = ClienteV4CompanyList[count]
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
            assunto=[]
            virgula = []
            paginas = [1, 2, 3, 4, 5, 6, 7, 8]
            paginas2 = [1, 2, 3, 4, 5, 6, 7 ,1,2,3,4,5,6,7,8]
            paginas3 = [1, 2, 3, 4, 5, 6, 7,1,2,3,4,5,6,7,8,1,2,3,4]

            txtd=browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[1]/div[2]/div[2]').text
            print('estou passando no começo')
            txt =  browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[1]/div[1]/div[1]/h3').text
            x = txt.split()
            print(x)
            dataDia = datetime.today().strftime('%d/%m/%Y')
            print(dataDia)
            #instancia:
            instancia = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[2]/div[1]/div/div/p[1]/span[1]').text
            print(instancia)
            try:
                area = instancia.split()
                areaC1 = area[0]
                instanciaC = area[2]
                instanciaC2 = area[3]
                areaFinal = areaC1.title()
            except:
                area = "_"
            instanciaT = instanciaC + " " + str(instanciaC2)
            instanciaTF = instanciaT.title()
            #pega o tribnal
            sleep(2)
            txt =  browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[1]/div[1]/div[1]/h3').text
            x = txt.split()
            print(x)
            sleep(2)
            tribunal = x[0]
            tribunal
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
            orgaojulgadorF = orgaojulgador.title()
            #classe
            classe = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[2]/div[1]/div/div/p[2]').text
            print(classe)
            classeFinal = classe.title()
            #assunto
            for x in range(20):
                teste=x+1
                try:
                    assunto.append(browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div[2]/div[1]/div/div/p[3]/span['+str(teste)+']').text)
                    virgula.append("; ")
                except:
                    assunto.append(" ")
                    virgula.append(" ")
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
                    virgulaN1 = "; "
                except:
                    nome.append(None)
                    virgulaN1 = " "
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
                    virgulaN2 = "; "
                except:
                    virgulaN2 = " "
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
                    virgulaN3 = "; "
                except:
                    virgulaN3 = " "
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
                    virgulaN4 = "; "
                    pass
                except:
                    virgulaN4 = " "
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
                    virgulaN5 = "; "
                except:
                    virgulaN5 = " "
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

            for x1 in range(3):

                soma = v+6
                try :
                    if( x1 == 0):
                        for x in range(8):
                            t = x+1
                            try:
                                browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div['+str(soma)+']/table/tbody['+str(t)+']/tr[1]/td[4]/div[2]/a').click()
                                sleep(2)
                                data.append(browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div['+str(soma)+']/table/tbody['+str(t)+']/tr[1]/td[1]').text)
                                print(data)
                                sleep(1)
                                tipo.append (browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div['+str(soma)+']/table/tbody['+str(t)+']/tr[1]/td[2]/p').text)
                                print(tipo)
                                sleep(1)
                                mv.append(browser.find_element_by_xpath(' /html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div['+str(soma)+']/table/tbody['+str(t)+']/tr[2]/td/table/tbody/tr/td/p').text)
                                print(mv)
                                sleep(1)
                                print(x1)
                            except:
                                data.append(None)
                                tipo.append(None)
                                mv.append(None)

                    if(x1 == 1):
                        print("estou no if 2")
                        n = "Não passei"
                        browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/nav[1]/ul/li[3]/a').click()
                        for x in range(8):
                            t2 = x+1
                            try:
                                browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div['+str(soma)+']/table/tbody['+str(t2)+']/tr[1]/td[4]/div[2]/a').click()
                                sleep(2)
                                data2.append(browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div['+str(soma)+']/table/tbody['+str(t2)+']/tr[1]/td[1]').text)
                                print(data)
                                sleep(1)
                                tipo2.append (browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div['+str(soma)+']/table/tbody['+str(t2)+']/tr[1]/td[2]/p').text)
                                print(tipo)
                                sleep(2)
                                mv2.append(browser.find_element_by_xpath(' /html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div['+str(soma)+']/table/tbody['+str(t2)+']/tr[2]/td/table/tbody/tr/td/p').text)
                                print(mv)
                                sleep(1)
                                print(x)
                            except:
                                pass
                    else:
                        for x in range(8):
                            data2.append(None)
                            mv2.append(None)
                            tipo2.append(None)


                    print("Eu sou o X1")
                    print(x1)

                    if(x1 == 2):
                        print("eu sou o novo X")
                        browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/nav[1]/ul/li[5]/a').click()
                        for x in range(8):
                            print("estou no x ==8")
                            t3 = x+1
                            try:
                                t3 = x+1
                                browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div['+str(soma)+']/table/tbody['+str(t3)+']/tr[1]/td[4]/div[2]/a').click()
                                sleep(1)
                                data3.append(browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div['+str(soma)+']/table/tbody['+str(t3)+']/tr[1]/td[1]').text)
                                print(data)
                                sleep(1)
                                tipo3.append (browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div['+str(soma)+']/table/tbody['+str(t3)+']/tr[1]/td[2]/p').text)
                                print(tipo)
                                sleep(1)
                                mv3.append(browser.find_element_by_xpath(' /html/body/div[5]/div[2]/div/div[1]/div/div[1]/div[1]/div['+str(soma)+']/table/tbody['+str(t3)+']/tr[2]/td/table/tbody/tr/td/p').text)
                                print(mv)
                                sleep(1)
                                print(x)
                            except:
                                pass
                    else:
                        for x in range(8):
                            data3.append(None)
                            tipo3.append(None)
                            mv3.append(None)

                except:

                    pass

            try:
                clientefinal = None
                if(cliente == "PESSOAS LISTADAS NA PLANILHA V4 COMPANY"):
                    clientefinal = "V4 Company"
                if(cliente == "CONFIDENCE CORRETORA DE CÂMBIO S/A"):
                    clientefinal = "Confidence"
                if(cliente == "BANCO CONFIDENCE DE CÂMBIO S/A"):
                    clientefinal = "Confidence"
                if(cliente == "TRAVELEX BANCO DE CÂMBIO S/A"):
                    clientefinal = "Confidence"
                if(cliente == "KOIN ADMINISTRADORA DE CARTÕES E PAGAMENTO S.A."):
                    clientefinal = "Koin"
                if ( cliente == "KOIN ADMINISTRADORA DE CARTÕES E MEIOS DE PAGAMENTO"):
                    clientefinal = "Koin"
                if (cliente == "TEMBICI PARTICIPACOES S.A."):
                    clientefinal = "Tembici"
                if(cliente == "KOIN ADMINISTRADORA DE CARTÕES E PAGAMENTO S.A"):
                    clientefinal = "Koin"
                if(cliente == "CABIFY AGÊNCIA DE SERVIÇOS DE TRANSPORTE DE PASSAGEIROS LTDA."):
                    clientefinal = "Cabify"
                if(cliente == "CABIFY AGÊNCIA DE SERVIÇOS DE TRANSPORTE DE PASSAGEIROS LTDA"):
                    clientefinal = "Cabify"
                if(cliente == "EASY TAXI SERVIÇOS LTDA."):
                    clientefinal = "Cabify"
                if(cliente == "EASY TAXI SERVIÇOS LTDA"):
                    clientefinal = "Cabify"
                if(cliente == "ARTUR DAMIÃO FONTES MAIA"):
                    clientefinal = "Tembici"
                if(cliente == "M1 TRANSPORTES SUSTENTÁVEIS LTDA."):
                    clientefinal = "Tembici"
                if(cliente == "M1 TRANSPORTES SUSTENTÁVEIS LTDA"):
                    clientefinal = "Tembici"
                if(cliente == "M2 SOLUÇÕES EM ENGENHARIA LTDA."):
                    clientefinal = "Tembici"
                if(cliente == "M2 SOLUÇÕES EM ENGENHARIA LTDA"):
                    clientefinal = "Tembici"
                if(cliente == "SAMBA TRANSPORTES SUSTENTAVEIS LTDA"):
                    clientefinal = "Tembici"
                if(cliente == "TEMBICI PARTICIPAÇÕES S/A"):
                    clientefinal = "Tembici"
                if(cliente == "BICI COMUNICAÇÃO E ASSESSORIA DE MARKETING S/A"):
                    clientefinal = "Tembici"
                if(cliente == "EDUARDO HENRIQUE MELO DE LIMA"):
                    clientefinal = "Tembici"
                if(cliente == "ANGELO JOSÉ BARROS LEITE"):
                    clientefinal = "Tembici"
                if(cliente == "ISRAEL LEITE DE ARAÚJO"):
                    clientefinal = "Tembici"
                if(cliente == "FLÁVIO DE BARROS LEITE"):
                    clientefinal = "Tembici"
                if(cliente == "LEONARDO JOSÉ CORRÊA NUNES"):
                    clientefinal = "Tembici"
                if(cliente == "RIVALDAVE DE VASCONCELOS"):
                    clientefinal = "Tembici"
                if(cliente == "RUDRIGO DE MELO MACIEL"):
                    clientefinal = "Tembici"
                if(cliente == "WYK NISSEN"):
                    clientefinal = "Tembici"

                if(cliente == "PAG S.A. MEIOS DE PAGAMENTO"):
                    clientefinal = "Will Bank"
                if(cliente == "WILL S.A. MEIOS DE PAGAMENTO"):
                    clientefinal = "Will Bank"
                if(cliente == "WILL S.A. INSTITUIÇÃO DE PAGAMENTO"):
                    clientefinal = "Will Bank"
                if(cliente == "AVISTA S/A CRÉDITO FINANCIAMENTO E INVESTIMENTO"):
                    clientefinal = "Will Bank"
                if(cliente == "AVISTA S/A ADMINISTRADORA DE CARTÃO DE CRÉDITO"):
                    clientefinal = "Will Bank"
                if(cliente == "WILL S/A MEIOS DE PAGAMENTO (PAG S/A)"):
                    clientefinal = "Will Bank"
                if(cliente == "AVISTA S/A ADMINISTRADORA DE CARTÕES DE CRÉDITO"):
                    clientefinal = "Will Bank"
                if(cliente == "AVISTA ADMINISTRADORA DE CARTOES DE CREDITO"):
                    clientefinal = "Will Bank"
                if(cliente == "AVISTA ADMINISTRADORA DE CARTÕES DE CRÉDITO LTDA"):
                    clientefinal = "Will Bank"
                if(cliente == "PAG S/A MEIOS DE PAGAMENTO"):
                    clientefinal = "Will Bank"
                if(cliente == "AVISTA S.A. CRÉDITO FINANCIAMENTO E INVESTIMENTO"):
                    clientefinal = "Will Bank"
                if(cliente == "AVISTA S/A CREDITO FINANCIAMENTO E INVESTIMENTO"):
                    clientefinal = "Will Bank"
                if(cliente == "SUPERNOVA S/A MEIOS DE PAGAMENTO"):
                    clientefinal = "Will Bank"
                if(cliente == "ADM GESTÃO DE NEGOCIOS LTDA"):
                    clientefinal == "V4 Company"
                if(cliente == "ADM GESTAO DE NEGOCIOS LTDA"):
                    clientefinal == "V4 Company"
                if(cliente == "BRUNO DE FREITAS SANTOS"):
                    clientefinal == "V4 Company"
                if(cliente == "LCAS SILVA DOMINGUES" ):
                    clientefinal == "V4 Company"
                if(cliente == "R - MARKETING DIGITAL LTDA"):
                    clientefinal == "V4 Company"
                if(cliente == "GRAZIANO DA SILVA"):
                    clientefinal == "V4 Company"
                if(cliente == "BERBERE"):
                    clientefinal == "V4 Company"
                if(cliente == "UPPER CONSULTORIA"):
                    clientefinal == "V4 Company"
                if(cliente == "VICTOR HUGO SOUZA SANTOS"):
                    clientefinal == "V4 Company"
                if(cliente == "THOMAS ROMANO BERNARDES"):
                    clientefinal == "V4 Company"
                if(cliente == "WELLEOVAN DOS SANTOS"):
                    clientefinal == "V4 Company"
                if(cliente == "V4 Company"):
                    clientefinal == "V4 Company"
                if(cliente == "ANDRE HENRIQUE TEIXEIRA"):
                    clientefinal == "V4 Company"
                if(cliente == "ICARO GABRIEL CRUZ"):
                    clientefinal == "V4 Company"
                if(cliente == "JL ASSESSORIA"):
                    clientefinal == "V4 Company"
                if(cliente == "ANDRE HENRIQUE TEIXEIRA "):
                    clientefinal == "V4 Company"
                if(cliente == "IM Assessoria de Marketing"):
                    clientefinal == "V4 Company"
                if(cliente == "FLAVIO DE ALMEIDA PAVAO"):
                    clientefinal == "V4 Company"
                if(cliente == "GERSSON JUNIOR DE SA"):
                    clientefinal == "V4 Company"
                if(cliente == "BALFRA SOLUCOES"):
                    clientefinal == "V4 Company"
                if(cliente == "BALFRA SOLUCOES"):
                    clientefinal == "V4 Company"
                if(cliente == "RODRIGO BAYER MEDEIROS"):
                    clientefinal == "V4 Company"
                if(cliente == "R - MARKETING DIGITAL LTDA"):
                    clientefinal == "V4 Company"
                if(cliente == "ADM GESTAO DE NEGOCIOS"):
                    clientefinal == "V4 Company"
                if(clientefinal == None):
                    clientefinal = cliente

            except:

                pass
            try:
                ufFinal = None
                if (uf2 == "AC"):
                    ufFinal = "Acre"
                if (uf2 == "RO"):
                    ufFinal = "Rondônia"
                if (uf2 == "AM"):
                    ufFinal = "Amazonas"
                if (uf2 == "RR"):
                    ufFinal = "Roraima"
                if (uf2 == "PA"):
                    ufFinal = "Pará"
                if (uf2 == "AP"):
                    ufFinal = "Amapá"
                if (uf2 == "TO"):
                    ufFinal = "Tocantins"
                if (uf2 == "MA"):
                    ufFinal = "Maranhão"
                if (uf2 == "PI"):
                    ufFinal = "Piauí"
                if (uf2 == "CE"):
                    ufFinal = "Ceará"
                if (uf2 == "RN"):
                    ufFinal = "Rio Grande do Norte"
                if (uf2 == "PB"):
                    ufFinal = "Paraíba"
                if (uf2 == "PE"):
                    ufFinal = "Pernambuco"
                if (uf2 == "AL"):
                    ufFinal = "Alagoas"
                if (uf2 == "SE"):
                    ufFinal = "Sergipe"
                if (uf2 == "BA"):
                    ufFinal = "Bahia"
                if (uf2 == "MG"):
                    ufFinal = "Minas Gerais"
                if (uf2 == "ES"):
                    ufFinal = "Espírito Santo"
                if (uf2 == "RJ"):
                    ufFinal = "Rio de Janeiro"
                if (uf2 == "SP"):
                    ufFinal = "São Paulo"
                if (uf2 == "PR"):
                    ufFinal = "Paraná"
                if (uf2 == "SC"):
                    ufFinal = "Santa Catarina"
                if (uf2 == "RS"):
                    ufFinal = "Rio Grande do Sul"
                if (uf2 == "MS"):
                    ufFinal = "Mato Grosso do Sul"
                if (uf2 == "MT"):
                    ufFinal = "Mato Grosso"
                if (uf2 == "GO"):
                    ufFinal = "Goiás"
                if (uf2 == "Distrito Federal"):
                    ufFinal = "DF"
                if(ClienteV4CompanyFinal == "V4 Company"):
                    clientefinal = "V4 Company"
                if(ufFinal == None):
                    ufFinal = uf2

                dado1F = dado1.title()
                dado2F = dado2.title()
                dado3F = dado3.title()
                dado4F = dado4.title()

                print(dado1F)
                juiz1 = ' '
                juiz2 = ' '
                juiz3 = ' '
                juiz4 = ' '
                juiz5 = ' '
                tipoPolo = '_'
                tipoPolo2 = '_'
                tipoPolo21 = '_'
                tipoPolo22= '_'
                tipoPolo31 = '_'
                tipoPolo33 = '_'
                tipoPolo41 = '_'
                tipoPolo43 = '_'
                if dado1F in ['Relator Juiz', 'Juiz Relator']:
                    juiz1 = nome[0]
                    juiz2 = nome[1]
                    juiz3 = nome[2]
                    juiz4 = nome[3]
                    juiz5 = nome[4]

                if dado2F in ['Relator Juiz', 'Juiz Relator']:
                    juiz1 = nome2[0]
                    juiz2 = nome2[1]
                    juiz3 = nome2[2]
                    juiz4 = nome2[3]
                    juiz5 = nome2[4]

                if dado3F in ['Relator Juiz', 'Juiz Relator']:
                    juiz1 = nome3[0]
                    juiz2 = nome3[1]
                    juiz3 = nome3[2]
                    juiz4 = nome3[3]
                    juiz5 = nome3[4]
                if dado4F in ['Relator Juiz', 'Juiz Relator']:
                    juiz1 = nome4[0]
                    juiz2 = nome4[1]
                    juiz3 = nome4[2]
                    juiz4 = nome4[3]
                    juiz5 = nome4[4]


                if dado1F in ['Polo Ativo', 'Autor Ativo', 'Polo Ativo Principal', 'Principal', 'Reqte', 'Autor','Autora', 'Representante', 'Noticiante', 'Demandante', 'Exectdo', 'Exectda']:
                    tipoPolo = dado1F
                    print(tipoPolo)
                    print('tipo Polo')
                if dado1F in ['Polo Passivo', 'Reu Passivo', 'Polo Passivo Principal', 'Principal', 'Reqdo', 'Reqda', 'Réu Ré','Reu', 'Ré', 'Representado a', 'Demandado', 'Exeqte']:
                    tipoPolo2 = dado1F
                    print(tipoPolo2)

                if dado2F in ['Polo Ativo', 'Autor Ativo', 'Polo Ativo Principal', 'Principal', 'Reqte', 'Autor','Autora', 'Representante', 'Noticiante', 'Demandante', 'Exectdo', 'Exectda']:
                    tipoPolo21 = dado2F
                    print(tipoPolo21)
                    print('tipo Polo')

                if dado2F in ['Polo Passivo',  'Reu Passivo', 'Polo Passivo Principal', 'Principal', 'Reqdo', 'Reqda', 'Réu Ré','Reu', 'Ré', 'Representado a', 'Demandado', 'Exeqte']:
                    tipoPolo22 = dado2F

                if dado3F in ['Polo Ativo', 'Autor Ativo', 'Polo Ativo Principal', 'Principal', 'Reqte', 'Autor','Autora', 'Representante', 'Noticiante', 'Demandante', 'Exectdo', 'Exectda']:
                    tipoPolo31 = dado3F
                    print(tipoPolo31)
                    print('tipo Polo')

                if dado3F in ['Polo Passivo', 'Reu Passivo', 'Polo Passivo Principal', 'Principal', 'Reqdo' ,'Reqda', 'Réu Ré','Reu', 'Ré', 'Representado a', 'Demandado', 'Exeqte']:
                    tipoPolo33 = dado3F
                    print(tipoPolo33)

                if dado4F in ['Polo Ativo', 'Autor Ativo', 'Polo Ativo Principal', 'Principal', 'Reqte', 'Autor','Autora', 'Representante', 'Noticiante', 'Demandante', 'Exectdo', 'Exectda']:
                    tipoPolo41 = dado4F
                    print(tipoPolo41)
                    print('tipo Polo')

                if dado4F in ['Polo Passivo', 'Reu Passivo', 'Polo Passivo Principal', 'Principal', 'Reqdo' ,'Reqda', 'Réu Ré','Reu', 'Ré', 'Representado a', 'Demandado', 'Exeqte']:
                    tipoPolo43 = dado4F
                    print(tipoPolo43)
            except:
                pass

            p = pd.DataFrame({
            'Detalhes do recurso': [processo],



            })
            add = pd.DataFrame ({'Data': [dataDia],
            'Cliente': [clientefinal],
            'Processo': [processo],
            'Tribunal': [tribunal],
            'UF': [uf2],
            'Localidade': [ufFinal],
            'Área': [areaFinal],
            'Instancia': [instanciaTF],
            'Órgão Julgador': [orgaojulgadorF],
            'Classe': [classeFinal],
            'Assuntos': [assunto[0].title() + str(virgula[0]) + str(assunto[1].title()) + str(virgula[1]) + str(assunto[2].title()) + str(virgula[2]) + str(assunto[3].title())
            + str(virgula[3]) + str(assunto[4].title()) + str(virgula[4]) + str(assunto[5].title()) + str(virgula[5]) + str(assunto[6].title()) + str(virgula[6])
            + str(assunto[7].title()) + str(virgula[7]) + str(assunto[8].title()) + str(virgula[8]) + str(assunto[9].title())],
            'Comarca':[comarca],
            'Data de Distribuição': [dataDistribuição],
            'Audiencias': [audiencias],
            'Valor da causa': [valorCausa],
            #Posição 1
            'Relator Juiz': [juiz1 + juiz2 + juiz3 + juiz4],

            'Polo Ativo 1': [tipoPolo],
            'Polo Passivo 1': [tipoPolo2],
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
            'Polo Ativo 2': [tipoPolo21],
            'Polo Passivo 2': [tipoPolo22],
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
            'Polo ativo 3': [tipoPolo31],
            'Polo Passivo 3': [tipoPolo33],
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
            'Polo ativo 4': [tipoPolo41],
            'Polo Passivo 4': [tipoPolo43],
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
            'Data 9': [data2[0]],
            'Data 10': [data2[2]],
            'Data 11': [data2[4]],
            'Data 12': [data2[6]],
            'Data 13': [data2[8]],
            'Data 14': [data2[10]],
            'Data 15': [data2[12]],
            'Data 16': [data2[14]],
            'Data 17':[data3[0]],
            'Data 18':[data3[2]],
            'Data 19':[data3[4]],
            'Data 20':[data3[6]],
            'tipo 1': [tipo[0]],
            'tipo 2': [tipo[1]],
            'tipo 3': [tipo[2]],
            'tipo 4': [tipo[3]],
            'tipo 5': [tipo[4]],
            'tipo 6': [tipo[5]],
            'tipo 7': [tipo[6]],
            'tipo 8': [tipo[7]],
            'tipo 9': [tipo2[0]],
            'tipo 10': [tipo2[2]],
            'tipo 11': [tipo2[4]],
            'tipo 12': [tipo2[6]],
            'tipo 13': [tipo2[8]],
            'tipo 14': [tipo2[10]],
            'tipo 15': [tipo2[12]],
            'tipo 16': [tipo2[14]],
            'tipo 17': [tipo3[0]],
            'tipo 18': [tipo3[2]],
            'tipo 19': [tipo3[4]],
            'tipo 20': [tipo3[6]],
            'Movimentação 1': [mv[0]],
            'Movimentação 2': [mv[1]],
            'Movimentação 3': [mv[2]],
            'Movimentação 4': [mv[3]],
            'Movimentação 5': [mv[4]],
            'Movimentação 6': [mv[5]],
            'Movimentação 7': [mv[6]],
            'Movimentação 8': [mv[7]],
            'Movimentação 9': [mv2[0]],
            'Movimentação 10': [mv2[2]],
            'Movimentação 11': [mv2[4]],
            'Movimentação 12': [mv2[6]],
            'Movimentação 13': [mv2[8]],
            'Movimentação 14': [mv2[10]],
            'Movimentação 15': [mv2[12]],
            'Movimentação 16': [mv2[14]],
            'Movimentação 17': [mv3[0]],
            'Movimentação 18': [mv3[2]],
            'Movimentação 19': [mv3[4]],
            'Movimentação 20': [mv3[6]],
            #Movimentações 2

            })

            print('Movimentações')
            df = pd.read_excel("Movimentações.xlsx")
            print('Estou passando por aqui')
            df_final = df.append(add, ignore_index=False)
            df_final.to_excel('Movimentações.xlsx', index=False)
            print(df_final)

            print('Digesto.xlsx')
            print('Estou passando por aqui')
            dfDiges = pd.read_excel('Digesto.xlsx', sheet_name = 'Digesto')
            dff = dfDiges.append(p, ignore_index=False)
            dff.to_excel('Digesto.xlsx', sheet_name = 'Digesto', index=False)
            print(df_final)
        ddd="sucesso!"

        my_resp = make_response(ddd)
        my_resp.status_code = 200
class baixarP(Resource):
    def get(self):
        options = Options()
        options.add_argument("no-sandbox")
        options.add_argument("--disable-extensions")
        options.add_argument("--headless")
        browser = webdriver.Chrome(options=options)
        url = "https://outlook.office.com/mail/inbox/id/AAQkAGEzNjI1ODA4LTk2MzktNDNhZS04MGIyLWJjZmRkZDhjOWFmNgAQAFlkZ7rDvPBLoXih4RZe%2B%2Fo%3D"
        browser.get(url)
        time.sleep(5)
        escreva = browser.find_element_by_name("loginfmt")
        escreva.send_keys(login)  #ele vai no login e coloca o email
        clicar = browser.find_element_by_xpath('//*[@id="idSIButton9"]')
        clicar.click() # e clica para entrar
        sleep(3)
        entrarSenha = browser.find_element_by_xpath('//*[@id="i0118"]')
        entrarSenha.send_keys(senhaEntrar)  #coloca a senha
        sleep(3)
        e = browser.find_element_by_id('idSIButton9')
        sleep(2)
        e.click() #entrar
        sleep(2)
        #Caso aparecer a tela "Continuar conectado ele vai no try"
        try:
            sleep(1)
            confirmar = browser.find_element_by_id('idSIButton9')
            sleep(2)
            confirmar.click()
        except:
            pass
        sleep(5)
        print("vou entrar no 1 email")

        entrar1Em = browser.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div[2]/div/div/div/div/div/div/div[1]/div[2]/div/div/div/div/div/div[1]/div/div/div[1]/div[2]/div[1]/div[1]/span')
        sleep(2)
        entrar1Em.click()
        sleep(4)
        print("entrei no 1 email, agora vou abaixar a planilha!")
        sleep(3)
        emailb = browser.find_element_by_class_name('We09X')
        emailb.click()
        sleep(4)
        print("Entrei na planilha agora estou pronto para abaixar")
        sleep(3)

        browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div/div[2]/div[2]/div[2]/div[1]/div[3]/div/div/div/div[1]/div[1]/div/span/button[1]/span').click()

        print("Acabei de clicar em editar")
        sleep(3)
        print("Estou preparado para clicar em abaixar, sera que agora vai?")
        sleep(5)
        browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div/div[2]/div[2]/div[2]/div[1]/div[3]/div/div/div/div[1]/div/button/span/i').click()
        sleep(2)
        browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div/div[2]/div[2]/div[2]/div[1]/div[3]/div/div/div/div[1]/div/button/span/span/span').click()
        sleep(2)
        browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div/div[2]/div[2]/div[2]/div[1]/div[3]/div/div/div/div[1]/div').click()
        sleep(2)
        browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div/div[2]/div[2]/div[2]/div[1]/div[3]/div/div/div/div[1]/div/button').click()
        print("Até que enfim, depois de tanto tempo, abaixado com sucesso!")
