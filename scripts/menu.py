import os, sys, platform, time, getpass

from scripts import update
from scripts.deepScan import deepScan

#Cores
Preto = "\033[30m"
Vermelho = "\033[31m"
Verde = "\033[32m"
Amarelo = "\033[33m"
Azul = "\033[34m"
Magenta = "\033[35m"
Ciano = "\033[36m"
Branco = "\033[37m"

Cororiginal = "\033[0:0m"

Negrito = "\033[1m"
Reverso = "\033[2m"
Blink = "\33[5m"

Fundopreto = "\033[40m"
Fundovermelho = "\033[41m"
Fundoverde = "\033[42m"
Fundoamarelo = "\033[43m"
Fundoazul = "\033[44m"
Fundomagenta = "\033[45m"
Fundociano = "\033[46m"
Fundobranco ="\033[47m"

def sysErrors():
    print("************************".center(80))
    print("* Sistema incompatível *".center(80))
    print("************************".center(80))
    sair = input("Deseja sair? [S/n]")
    if (sair == '' or sair == 's'):
        sys.exit()
    else:
        exibeMenu()

def opcoes():
    from scripts import links
    from scripts import scanPort
    from scripts import sitecloner
    from scripts import varrer
    from scripts import honeypot

    import random, os

    print(Negrito)

    try:
        versao = open("ver.txt","r")
        vrs = versao.read()
        versao.close()
        numero = random.randint(1,4)
        ip = open("Files/net/ipwan.txt","r")
        ipwan = ip.read()
        ip.close()
        ip = open("Files/net/iplan.txt","r")
        iplan = ip.read()
        ip.close()
    except:
        print("Erro na leitura das informações de rede e versão.")
        time.sleep(3)
        print("Não será possível exibir IP LAN e WAN.")
        time.sleep(3)
        print("E/Ou não será possível atualizar.")
        time.sleep(3)
        print("O programa irá fechar. Bye!")
        time.sleep(3)
        sys.exit()
    print(Cororiginal)

    print(Ciano+"***********************")
    print(Ciano+"*"+Verde+"[1] Clonar site     "+Ciano+" * "+"Versão atual: "+Branco+str((vrs)+"            "+Azul))
    print(Ciano+"*"+Verde+"[2] Web crawler     "+Ciano+" * "+"Sistema: "+Branco+sys.platform.title()+"               "+Azul)
    print(Ciano+"*"+Verde+"[3] Escanear portas "+Ciano+" * "+"Tipo: "+Branco+os.name.title()+"                  "+Azul)
    print(Ciano+"*"+Verde+"[4] Modo gráfico    "+Ciano+" * "+"Nome de rede: "+Branco+platform.node()+" "+Azul)
    print(Ciano+"*"+Verde+"[5] Varrer rede     "+Ciano+" * "+"Compilador python: "+Branco+platform.python_compiler()+" "+Azul)
    print(Ciano+"*"+Verde+"[6] Honeypot        "+Ciano+" * "+"Versão python: "+Branco+platform.python_version()+"         "+Azul)
    print(Ciano+"*"+Verde+"[7] Atualizações    "+Ciano+" * "+"Máquina: "+Branco+platform.machine()+"              "+Azul)
    print(Ciano+"*"+Verde+"[8] Change log      "+Ciano+" * "+"Implementação python: "+Branco+platform.python_implementation()+""+Azul)
    print(Ciano+"*"+Verde+"[9] Sair (Ctrl+C)   "+Ciano+" * "+"Release system: "+Branco+platform.release()+" "+Azul)
    print(Ciano+"***********************")

    usr = getpass.getuser()
    print(Amarelo+"Usuário: %s" % Branco+usr+"\n")

    if(len(ipwan) != 0):
        print(Verde+"IP WAN: "+Amarelo+ipwan)
    else:
        print(Verde+"IP WAN: Interrompido pelo usuário"+Amarelo)
    print(Verde+"IP LAN: "+Amarelo+iplan)

    def callInterface():
        if os.path.exists("scripts/interface.py"):
            from scripts import interface
            interface.iniciar()

    try:
        opt = int(input("Morpheus ~> "))
        while((opt < 1) or (opt > 10)):
            opcoes()
        if(opt == 1):
            sitecloner.htmlcopy()
        elif(opt == 2):
            links.capturaLinks()
        elif(opt == 3):
            scanPort.scannerP()
        elif(opt == 4):
            if os.path.exists("scripts/interface.py"):
                callInterface()
            else:
                print("Interface gráfica não instalada!")
                opcoes()
        elif(opt == 5):
            varrer.rede()
        elif(opt == 6):
            honeypot.honeypot()
        elif(opt == 7):
            update.updates()
        elif(opt == 8):
            try:
                updt_desc = open("Files/downloads/description.txt","r")
                desc = updt_desc.read()
                os.system("clear")
                print("\033[33m"+"|_ Última atualização _|".center(80))
                print("\033[0m"+"*"*len(desc))
                print(desc)
                print("*"*len(desc))
                updt_desc.close()
                opcoes()
            except:
                print("\033[33m"+"Ocorreu um erro.".center(80))
            finally:
                opcoes()
        elif(opt == 9):
            sys.exit()
        elif(opt == 10):
            deepScan()
    except KeyboardInterrupt:
        print("Interrompido pelo usuário.".center(80))
        sys.exit()
    except ValueError:
        print("\33[31m"+"Digite apenas números".center(80))
        opcoes()
