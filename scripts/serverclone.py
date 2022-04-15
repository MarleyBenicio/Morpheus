from wsgiref.simple_server import make_server
#from pyramid import *
from pyramid.config import Configurator
from pyramid.response import Response

import os, configparser, pyfiglet, time
def func_main_server():
    def servidor(request):
        print("✔️")
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

    if True:
    #if __name__ == "__main__":

        result = pyfiglet.figlet_format("Server", font = "banner3-D")
        print(result)

        print("\33[32m"+"Lendo configurações...")
        configuracoes = configparser.ConfigParser()
        configuracoes.read("Configs/Configs.ini")
        portaserver = configuracoes.get('Rede','portaserverlocal')
        print("\33[33m"+"Inicializando...")
        config = Configurator()
        config.add_route('raiz', '/')
        config.add_view(servidor, route_name='raiz')
        app = config.make_wsgi_app()
        print("\33[34m"+"Iniciando servidor...")
        try:
            print("\33[34m"+"Porta local: ",portaserver)
            server = make_server('0.0.0.0', int(portaserver), app)
            print("\33[36m"+"Servidor iniciado!")
            server.serve_forever()
        except KeyboardInterrupt:
            os.system("clear")
            print("\nO servidor foi encerrado".center(80))
            #os.system("rm -Rf "+pathsite)
        except:
            servidor()
