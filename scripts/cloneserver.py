from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

import os, configparser

def servidor(request):
	print("1")
	try:
		return Response('<html><title>Server '+vers+'</title><body style="background-color:black;"><meta http-equiv="refresh" content="3;"><center><h3 style="color:yellow;">Algo deu errado...<br>''</br></h3></center><p></body></html>')
		print("2")
	except:
		html = open("Files/net/index.html","r")
		source = html.read()
		return Response(source)
		html.close()
		print("3")

if __name__ == "__main__":
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
		print("\33[36m"+"Servidor iniciado!")
		print("\33[34m"+"Porta local: ",portaserver)
		server = make_server('0.0.0.0', int(portaserver), app)
		server.serve_forever()
	except KeyboardInterrupt:
		os.system("clear")
		print("\nO servidor foi encerrado".center(80))
		os.system('notify-send -t 5000 -i face-sad -u normal "Atenção" "O servidor foi encerrado manualmente."')
