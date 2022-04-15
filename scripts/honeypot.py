def honeypot():
    import socket, time, configparser, pyfiglet, os

    from datetime import datetime

    from scripts import menu

    conf = configparser.ConfigParser()
    conf.read("Configs/Configs.ini")

    requestsNumber = conf.get("Rede","requests")
    banner = conf.get("banners","honeypot")

    result = pyfiglet.figlet_format("Honeypot", font = banner)
    print("\n")
    print(result)

    port = int(input("Digite a porta de escuta: "))
    os.system("notify-send -t 5000 -i face-devilish 'Iniciando honeypot' "+str(port))
    log = open("Files/Logs/log.log","a")
    try:
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("\33[34m"+"\33[33m"+"Criar socket     "+"\33[34m"+"\33[34m"+"  [Ok]")
       	log.write("Criar socket honeypot: %s" % time.asctime())
    except:
        print("\33[34m"+"\33[33m"+"Criar socket "+"\33[34m"+"\33[31m"+"[Falha]")
        print("Retornando ao menu...")
        time.sleep(3)
    try:
        host = socket.gethostname()
        print("\33[34m"+"\33[33m"+"Obter nome local "+"\33[34m"+"\33[35m"+"  [Ok]")
       	log.write("\nObter nome local: %s" % host)
    except:
        print("\33[34m"+"\33[33m"+"Obter nome local "+"\33[34m"+"\33[31m"+"[Falha]")
        print("Retornando ao menu...")
        time.sleep(3)

        menu.opcoes()

    print("\33[33m"+"Conectando...      [??]")
    try:
        serversocket.bind((host, port))
        print("\33[34m"+"\33[33m"+"Conectado        "+"\33[34m"+"\33[36m"+"  [Ok]")
        log.write("\nConectado: %s" % time.asctime())
    except OSError:
        print("Esta porta pode já estar sendo usada, tente outra.")
        log.write("\nPorta já usada por outro processo: %s" % port)
        print("\33[34m"+"\33[33m"+"Falha"+"\33[34m"+"\33[31m"+" Não conectado.")
        time.sleep(3)
        honeypot()
    serversocket.listen(int(requestsNumber))
    log = open("Files/Logs/honeypot_log/log.txt","a")
    print("\33[33m"+"Aguardando conexão [!!]\n")
    try:
        while True:
            clientsocket,addr = serversocket.accept()
            print("\n"+"\33[34m"+"["+"\33[33m"+"Ok"+"\33[34m"+"]"+"\33[37m"+" Tentativa de conexão.__")
            print("                           |")
            print("                           v")
            print("\33[33m"+"|-----------------------------------------------|")
            print("\33[33m"+"|Tentativa de conexão:"+"\33[33m"+"\33[41m"+"\33[1m"+str(addr)+"\33[0m")
            print("\33[33m"+"|-----------------------------------------------|")
            #os.system("notify-send -t 5000 -i face-devilish 'Tentativa de conexão'"+str(addr) )
            #clientsocket.close()
            try:
                log.write("\nHost: "+str(addr)+"\n")
                #log.write("Hora: "+str(datetime.now()))
            except FileNotFoundError:
                print("Arquivo de log não encontrado!")
            except:
                print("|")
                print("--> Erro ao gravar no log.\n")
            clientsocket.close()
    except:
        print("\33[34m"+"["+"\33[33m"+"Falha"+"\33[34m"+"]"+"\33[31m"+" Conexão não estabelecida.")
        menu.opcoes()
        log.close()
