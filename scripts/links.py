import requests, sys, glob, os, time, configparser

tipoManipulacao = configparser.ConfigParser()

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

#coresTerminal = configparser.ConfigParser()
#coresTerminal.read("Configs/Configs.ini")
#cor = coresTerminal.get("cores","")

def capturaLinks():

	from scripts import menu

	from bs4 import BeautifulSoup #, SoupStrainer

	tipoManipulacao.read("Configs/Configs.ini")

	valorStringParser = tipoManipulacao.get("Outros","tipomanipulacao")

	print(Azul+"***************************".center(80))
	print(Azul+"* Digite a URL principal. *".center(80))
	print(Azul+"***************************".center(80))
	print(Amarelo+"Digite 's' para sair.".center(80))
	url = str(input(": "))
	if url == 's':
		sys.exit()
	else:
		try:
			#print(Negrito+Amarelo+"O processo pode ser um pouco demorado.".center(80))
			page = requests.get("http://"+url)
			data = page.text
			soup = BeautifulSoup(data, features=valorStringParser)
			save = open("Files/Capturas/"+url+".txt","w")
			save_html = open("Files/Capturas/html/"+url+".html","a")
			print("*************************************************".center(80))
			print("* Você deseja salvar os links capturados?   [N] *".center(80))
			print("*************************************************".center(80))
			opcao = input(": ")
			if(opcao == ''):
				for link in soup.find_all('a'):
					print("URL: "+link.get('href'))
			else:
				for link in soup.find_all('a'):
					print("URL: "+link.get('href'))
					save.write("\nURL: "+link.get('href'))
     ###### - MELHORAR ESSA PARTE - ######
					save_html.write("<head>")
					save_html.write("<title>Links capturados</title>")
					save_html.write("</title>")
					save_html.write("<body>")
					save_html.write("a href="+link.get('href')+"\n")
					save_html.write("</body>")
			save.close()
			save_html.close()
			saveLink = open("Files/URL.txt","w")
			verificar = saveLink.read()
			if(verificar in saveLink):pass
			else:
				saveLink.write(url+"\n")
				saveLink.close()
		except:
			print("Algo deu errado.".center(80))
			capturaLinks()
		finally:
			menu.opcoes()
