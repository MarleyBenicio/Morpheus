def servidor():
    import socket, configparser, sys, time

    from scripts import menu

    horaLog = open("Files/Logs/Registro.log","a")
    horaLog.write("\n*** Servidor iniciado. ***")
    horaLog.write("\nHora: "+str(time.asctime()))
    horaLog.write("\n**************************")
    config = configparser.ConfigParser()
    config.read("Configs/ConfigsServer.ini")
    porta = config.getint("Server","Port")
    comandoFim = config.get("Server","commandend")
    senhaserver = config.get("Server","senha")
    mensagem = config.get("Server","msg")
    print("Porta: ",porta)
    if(porta < 1024):
        print("A porta definida não pode ser menor que 1024.".center(80))
        horalog.write("\nO usuário tentou definir uma porta menor que 1024")
        servidor()
    else:
        try:
            horaLog.write("\nPorta conectada: %i" % porta)
            host = socket.gethostname()
            horaLog.write("\nHost: %s" % host)
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind((host, porta))
            server.listen(5)
            recebe = ''
            loop = 0
            while recebe != senhaserver:
                loop += 1
                try:
                    print("\033[1m"+"\033[32m"+"+---------------------+".center(80))
                    print("\033[1m"+"\033[32m"+"|Aguardando conexão...|".center(80))
                    print("\033[1m"+"\033[32m"+"+---------------------+".center(80))
                    horaLog.write("\nServidor iniciado e aguardando conexão.")
                    con, cliente = server.accept()
                    print("Conectado".center(80))
                    horaLog.write("\nCliente conectado.")
                    con.send(mensagem.encode("utf-8"))
                    print("\033[1m"+"\033[34m"+"Aguardando comando...".center(80))
                    recebe = con.recv(1024)
                    if recebe == "":pass
                    else:
                        print("\033[1m"+"\033[33m"+"Comando recebido: "+str(recebe.decode("utf-8")))
                        horaLog.write("\nComando recebido: %s" % recebe)
                    if str(recebe) != str(senhaserver.encode("utf-8")):
                        print("\033[1m"+"\033[34m"+"Encerrado pelo servidor.".center(80))
                        horaLog.write("\nO servidor encerrou a conexão.")
                        server.close()
                        sys.exit()
                        break
                    else:pass
                    if comandoFim.encode("utf-8") == recebe.decode("utf-8"):
                        server.close()
                        menu.opcoes()
                except KeyboardInterrupt:
                    #print("\033[1m"+"\033[31m"+"Interrompido pelo usuário.".center(80))
                    server.close()
                    menu.opcoes()
                if loop >= 2:
                    print("Conexão encerrada pelo servidor.")
                    server.close()
                    sys.exit()
        except OSError:
            print("\nEndereço ainda em uso? Espere alguns segundos e tente novamente.")
            server.close()
        finally:
            horaLog.close()

