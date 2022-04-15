
def configs():
    from scripts import menu
    from scripts import regconfigs

    import configparser

    print("*****************************".center(80))
    print("* Configurações do programa *".center(80))
    print("*****************************".center(80))
    try:
        setts = configparser.ConfigParser()
        pre = input("\33[34m"+"Digite o prefixo do IP. "+"\33[33m"+"(Geralmente 192.168): ")
        fx = input("\33[34m"+"Digite a faixa de IP."+"\33[33m"+" (Geralmente 0 ou 1, após o prefixo): ")
        qtdd= input("\33[34m"+"Digite a quantidade de pings de verificação."+"\33[31m"+" (Recomendado: 1): ")
        timeout = input("\33[33m"+"Digite o timeout do socket (em segundos): ")
        server = input("\33[33m"+"Digite o servidor de verificação de status da conexão: ")
        portastatus = input("\33[33m"+"Digite a porta para verificação de status: ")
        localport = input("\33[33m"+"Digite a porta local: ")
        setts['Rede'] = {'prefixip':str(pre),'faixaip':str(fx),'pings':(qtdd),'timeout':(timeout),'serverstatus':str(server),'portstatus':int(portastatus),'portaserverlocal':int(localport)}
        with open("Configs/Configs.ini","r+") as settings:
            setts.write(settings)
    except:
        print("\33[31m"+"\nNão foi possível gravar as informações.\n")
        menu.opcoes()
    finally:
        menu.opcoes()
    regconfigs.registro()


def reset():

    from scripts import menu
    from scripts import regconfigs

    import configparser, tqdm, time, os
    resposta = input("Tem certeza que deseja redefinir tudo para o padrão? [S/n]")
    if((resposta != 's') and (resposta != 'S') and (resposta != 'n') and (resposta != 'N')):
        print("Resposta inválida, digite 's' ou 'S', para sim, 'n' ou 'N', para não. Deixando em branco e dando enter, a resposta padrão será, Sim.")
    if ((resposta == '') or (resposta == 's') or (resposta == 'S')):
        try:
            print("Instanciando arquivo...")
            resetar = configparser.ConfigParser()
            resetar.read("Configs/Configs.ini")
            print("Redefinindo...")
            print("Limpando registros do sistema...")
            for item in os.listdir("Files/Logs/"):
                if (item.endswith(".html")) or (item.endswith(".log")):
                    os.remove("Files/Logs/"+item)
            print("Apagando registros de capturas de links...")
            for cptrs in os.listdir("Files/Capturas/"):
                if(cptrs.endswith(".txt")):
                    os.remove("Files/Capturas/"+cptrs)
            print("Apagando registros de portas abertas...")
            for portas in os.listdir("Files/Logs/Portas/"):
                if portas.endswith(".log"):
                    os.remove("Files/Logs/Portas/"+portas)
            print("Apagando sites baixados...")
            for sites in os.listdir("Files/net/"):
                print(sites)
                os.rmdir("Files/net/"+sites)
            print("Redefinindo configurações de rede...")
            resetar['Rede'] = {'prefixip':str('192.168'),'faixaip':str('0'),'pings':str('1'),'timeout':str('5')
            ,'serverstatus':str('www.google.com'),'portstatus':str('80'),'portaserverlocal':str('8080')}
            resetar['Som'] = {'play':str('true'),'volume':'0.7','path':'Files/sounds','starting':'starting.mp3','notifysound':'notific.mp3','fail':'error.mp3','scanning':'scanner.mp3'}
            resetar['log-html'] = {'background':str('#000000'),'text':str('#ffff00'),'sizetext':str('h3'),'bordertable':'2'}
            with open("Configs/Configs.ini","r+") as sets:
                resetar.write(sets)
                print("Redefinido para o padrão!")
            rst = open("00","w")
            rst.close()
        except:
            print("Não foi possível redefinir.")
            menu.opcoes()
        finally:
            regconfigs.registro()
            menu.opcoes()
    elif((resposta == 'n') or (resposta == 'N')):
        menu.opcoes()
