import socket, configparser
from icmplib import ping
from icmplib.models import Host

from scripts import menu

file = configparser.ConfigParser()
file.read("Configs/Configs.ini")

def deepScan():
    prefixoIP = str(file.get("Rede","prefixip"))
    faixaDeIp = str(file.get("Rede","faixaip"))
    ipStart = input("Digite o IP inicial: ")
    ipEnd = input("Digite o IP Final: ")
    
    if ((int(ipStart) <= 0) or (int(ipEnd) > 254)):
        print("IP inválido!")
    else:
        for cont in ipEnd:
            cont = int(cont)+1
            hostRemoto = ping(prefixoIP+'.'+faixaDeIp+'.'+str(cont), count = 2, interval=1)
            print(prefixoIP+faixaDeIp+str(cont))
            if hostRemoto.is_alive == True:
                print("Online!")
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as scan:
                    try:
                        temposocket = file.get("Rede","timesocket")
                        socket.setdefaulttimeout(float(temposocket))
                        scan.connect((ip, 5900))
                        print("VNC Ok")
                        scan.close()
                    finally:
                        menu.opcoes()