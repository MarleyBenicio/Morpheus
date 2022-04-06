from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from PIL import Image

import os, configparser, pyfiglet, time, qrcode

def servidor(request):
    #print("✔️")
    try:
        return Response('<html><title>Server '+vers+'</title><body style="background-color:black;"><meta http-equiv="refresh" content="3;"><center><h3 style="color:yellow;">Algo deu errado...<br>''</br></h3></center><p></body></html>')
    except:
        pathsite = open("Files/net/path.txt","r")
        caminho = pathsite.read()
        if(len(caminho) == 0):
            html = open(pathsite,"r")
            source = html.read()
            return Response(source)
            html.close()
        else:
            html = open(caminho,"r")
            source = html.read()
            return Response(source)
            html.close()

if __name__ == "__main__":

    result = pyfiglet.figlet_format("Server", font = "banner3-D")
    print(result)

    print("\33[32m"+"Lendo configurações...")
    try:
        configuracoes = configparser.ConfigParser()
        configuracoes.read("Configs/Configs.ini")
        portaserver = configuracoes.get('Rede','portaserverlocal')
        print("Configurações [Ok]")
    except:
        print("Erro ao ler configurações!")
        print("Saindo em 3 segundos...")
        time.sleep(3)
        exit
    try:
        print("\33[33m"+"Inicializando...")
        config = Configurator()
        config.add_route('raiz', '/')
        config.add_view(servidor, route_name='raiz')
        app = config.make_wsgi_app()
        print("Inicialização [Ok]")
    except:
        print("Erro inicializar servidor!")
        print("Saindo em 3 segundos...")
        time.sleep(3)
        exit
    print("\33[34m"+"Iniciando servidor...")
    try:
        print("\33[34m"+"Endereço local: http://localhost:"+portaserver)
        server = make_server('0.0.0.0',int(portaserver), app)
        #print("\33[36m"+"Servidor iniciado!")
        print("Servidor iniciado [Ok]")
        qrc = input("Gerar QRCode? [s/n]")
        if (qrc == 's'):
            print("1 - Gerar do IP LAN\n2 - Gerar do IP WAN")
            opcIP = int(input(": "))
            if (opcIP == 1):
                try:
                    ipFile = open("Files/net/iplan.txt","r")
                    ip = ipFile.read()
                    imgQrcode = qrcode.make("http://"+str(ip)+':'+portaserver)
                    imgQrcode.save("QRcode_IP_LAN.png")
                    imagem = Image.open("QRcode_IP_LAN.png")
                    imagem.show()
                except:
                    print("Ocorreu um erro!")
            elif (opcIP == 2):
                try:
                    ipFile = open("Files/net/ipwan.txt","r")
                    ip = ipFile.read()
                    imgQrcode = qrcode.make("http://"+str(ip)+':'+portaserver)
                    imgQrcode.save("QRcode_IP_WAN.png")
                    imagem = Image.open("QRcode_IP_WAN.png")
                    imagem.show()
                except:
                    print("Ocorreu um erro!")
        elif (qrc != 's'):pass
        server.serve_forever()
        
    except KeyboardInterrupt:
        os.system("clear")
        print("\nO servidor foi encerrado".center(80))
    except OSError:
        print("Está porta já está sendo usada por outro processo?")
        print("Saindo em 53 segundos...")
        time.sleep(3)
        exit
    except:
        servidor()
#    finally:
