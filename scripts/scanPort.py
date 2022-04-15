def scannerP():
    import socket, sys, os, configparser, time

    from scripts import menu

    #from tqdm import tqdm

    #socket.SOCK_STREAM -> TCP
    #socket.SOCK_DGRAM  -> UDP

    def variasPortas():

        #from scripts import notify

        tempo = configparser.ConfigParser()
        tempo.read("Configs/Configs.ini")
        temposocket = tempo.get('Rede','timeout')
        if temposocket == '':
            print("\33[31m"+"Configuração inválida no tempo do socket.")
            menu.opcoes()
        if sys.platform != "linux":
            print("\33[33m"+"Este módulo só funciona em "+"\33[34m"+"Linux."+"\33[31m"+" Saindo em 3 segundos...")
            time.sleep(3)
            sys.exit()

        cont = 1
        print("\n")
        print("\33[5m"+"Escaneando portas..."+"\33[0m")
        print("\n")
        for cont in range(porta, portaFinal+1):
        # REMOVER ESTE COMENTÁRIO PARA ATIVAR A EXIBIÇÃO DA PORTA ATUAL
            #porcento = (cont*100)/portaFinal
            #print("\033[36m"+"Porta atual: %i" % cont)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as scan:
                try:
                    socket.setdefaulttimeout(float(temposocket))
                    scan.connect((host, cont))
                    print("\33[32m"+" [✔️ ]"+"\33[34m"+" Porta: "+"\33[32m"+"%i" % cont)
                    scan.close()
                    try:
                        logPortasAbertas.write("[Ok] Porta: %i\n" % cont)
                    except:print("\33[33m"+"Não gravado.")
                except KeyboardInterrupt:
                    print("\033[31m"+"\nInterrompido pelo usuário.\n")
                    sys.exit()
                except Exception:pass
                    # REMOVER ESTE COMENTÁRIO PARA ATIVAR A EXIBIÇÃO DE PORTAS FECHADAS
                    #print("\33[31m"+"\n[Falha]"+"\33[34m"+" Porta: "+"\33[33m"+"%i" % cont)
                finally:
                    scan.close()
        logPortasAbertas.close()
        os.system("touch Files/Logs/Portas/"+host+".log")
        verif = open("Files/Logs/Portas/"+host+".log","r")
        txt = verif.read()
        if txt == "":pass
        else:
            print("\33[33m"+"\nPortas abertas gravadas em /Files/Logs/Portas/"+host+".log")
        menu.opcoes()

    host = input("\033[33m"+"Digite o IP: ")
    #verificacao = os.system("ping -c1 "+host+" > echo.txt")
    #os.remove("echo.txt")
    #if verificacao != 0:
    #    print("\33[35m"+"\n-->"+"\33[33m"+"Alvo offline.\n")
    #    menu.opcoes()
    #else:
    host = socket.gethostbyname(host)
    os.system("touch Files/Logs/Portas/"+host+".log")
    logPortasAbertas = open("Files/Logs/Portas/"+host+".log","w")
    print("\33[33m"+"Para verificar apenas uma porta, insira a porta desejada em "+"\33[33m"+"porta inicial "+"\33[33m"+"e "+"\33[33m"+"0"+"\33[33m"+" na porta final")
    porta = int(input("\033[33m"+"Digite a porta inicial: "))
    if porta <= 0:
        print("\33[33m"+"A porta inicial deve ser sempre maior ou igual a 1.")
        variasPortas()
    portaFinal = int(input("\033[34m"+"Digite a porta final: "))

    if portaFinal > 65535:
        print("\33[34m"+"A porta final não pode ser maior que "+"\33[33m"+"65535")
        scannerP()
    if((porta > portaFinal) and (portaFinal > 0)):
        print("\033[33m"+"A porta final sempre deve ser maior que a inicial.")
        scannerP()
    else:
        cont = porta
        if portaFinal == 0:
            def portaUnica():
                if sys.platform != "linux":
                    print("\33[33m"+"Este módulo só funciona em "+"\33[34m"+"Linux."+"\33[31m"+" Saindo...")
                    time.sleep(3)
                    sys.exit()

                from scripts import scanner
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as scan:
                    try:
                        scan.connect((host, porta))
                        print("\033[32m"+"\n[Ok]"+"\033[37m"+"️ Porta: %i\n" % porta)
                        scan.close()
                    except:
                        print("\033[31m"+"Falha na execução.")
                        print("\033[31m"+"\n[Falha]"+"\033[37m"+"️ Porta: %i\n" % porta)
                    finally:
                        scan.close()
                        scanner.scan()
            portaUnica()
        else:
            variasPortas()
