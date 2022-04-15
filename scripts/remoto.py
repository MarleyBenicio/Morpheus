import socket, sys, os

def remoto():
    try:
        print("\33[33m"+"Para sair, aperte Ctrl+C")
        host = input("\nServidor: ")
        resposta = os.system("ping -c1 "+host+" > echo.txt ; rm echo.txt")
        print(bin(resposta))
        if resposta != 0:
            print("O servidor parece estar offline.".center(80))
            remoto()
        else:
            porta = int(input("Porta: "))
            print("Criando socket...")
            tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("Conectando...")
            tcp.connect((host,porta))
            print("Conectado.")
    except KeyboardInterrupt:
        print("\33[33m"+"\nDesconectado".center(80))
        tcp.close()
    except ConnectionRefusedError:
        print("\33[31m"+"Hum... parece que o servidor remoto recusou a conexão.".center(80))
        tcp.close()
        sys.exit()
    except:
        print("Desconectado.")
        tcp.close()
        remoto()
#remoto()
