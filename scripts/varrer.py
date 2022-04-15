import os, configparser, sys, getpass
from icmplib import ping
'''
>>> host = ping('1.1.1.1', count=10, interval=0.2)

>>> host.address            # The IP address of the host that responded
'1.1.1.1'                   # to the request

>>> host.min_rtt            # The minimum round-trip time
12.2

>>> host.avg_rtt            # The average round-trip time
13.2

>>> host.max_rtt            # The maximum round-trip time
17.6

>>> host.packets_sent       # The number of packets transmitted to the
10                          # destination host

>>> host.packets_received   # The number of packets sent by the remote
9                           # host and received by the current host

>>> host.packet_loss        # Packet loss occurs when packets fail to
0.1                         # reach their destination. Returns a float
                            # between 0 and 1 (all packets are lost)
>>> host.is_alive           # Indicates whether the host is reachable
True
'''

from scripts import menu

def rede():
    if sys.platform != "linux":
        print("\33[33m"+"Este módulo só funciona em "+"\33[34m"+"Linux."+"\33[31m"+" Saindo...")
        time.sleep(3)
        sys.exit()

    info = configparser.ConfigParser()
    info.read("Configs/Configs.ini")
    qtd = info.get('Rede','pings')
    prefixo = info.get('Rede','prefixip')
    faixa = info.get('Rede','faixaip')
    mostraoff = info.get('Outros','showoffline')
    intervalo = info.get('Rede','timeout')
    faixadeip = int(input("Faixa de IP: "))

    ip = int(input("IP inicial: "+prefixo+"."+str(faixadeip)+"."))

    if (ip < 1):
        print("\33[33m"+"\nEndereço IP inválido!.")
    ipfinal = int(input("IP final: "+prefixo+"."+str(faixadeip)+"."))

    if ipfinal > 254:
        print("Endereço IP inválido!")
        print("\33[33m"+"O IP final não deve ser maior que 254, portanto, o programa verificará até o 254.")
    if ip > ipfinal:
        print("\33[31m"+"O IP inicial não pode ser maior que o final.")
        rede()
    print("\n")
    print("\33[5m"+"Varrendo rede..."+"\33[0m")
    print("\n")
    user = getpass.getuser()
    if user != "root":
        print("**********************************************************************")
        print("* Você não tem privilégios suficientes para isto, execute como sudo. *")
        print("**********************************************************************")
        menu.opcoes()
    for cont in range(ip, ipfinal+1):
        host = ping(prefixo+'.'+str(faixadeip)+'.'+str(cont), count=int(qtd), interval=float(intervalo))
        if host.is_alive == True:
            print("\33[0m")
            print("*"*32)
            print("* "+"\33[36m"+prefixo+"."+str(faixadeip)+"."+str(cont)+"\33[32m"+" ✔️  Host online *")
        else:
            if (mostraoff == "true"):
                print("\33[37m"+prefixo+"."+str(faixadeip)+"."+str(cont)+"\33[31m"+" ❌️ Host offline")
            elif (mostraoff == "false"):
                pass
            elif ((mostraoff != "true") and (mostraoff != "false")):
                print("Valor incorreto na configuração")
                menu.opcoes()
    if os.path.exists("echo.txt"):
        os.remove("echo.txt")
    menu.opcoes()
