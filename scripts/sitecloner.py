import urllib.request, socket, os, time

def htmlcopy():

	from scripts import menu
	from scripts import serverclone

	from tqdm import tqdm

	import time

	site = input("Digite o site desejado: ")
	try:
		log = open("Files/Logs/log.log","a")
		log.write("Hora: %s" % time.asctime())
		log.write("\nSite: %s" % site)
		log.close()
	except PermissionError:
		print("Você não tem permissões suficientes para isso.")

	if (os.path.exists("Files/net/"+site+"index.html")):
		print("Limpando...")
		os.system("rm -Rf Files/net/"+site)
		print("Concluído.")
		opcao = input(": ")
		if (opcao == 'n'):
			socket.setdefaulttimeout(5)
			print("\33[05m"+"\33[33m"+"Baixando..."+"\033[0m")
			with urllib.request.urlopen("http://"+site) as response:
				try:
					print("Lendo HTML...s")
					html = response.read()
					html = html.decode()
					print("Calculando tamanho...")
					sizesite = len(html)
					print("Salvando...")
					tempo = sizesite/10000000
					for i in tqdm(range(int(sizesite/1024))):
						time.sleep(tempo)
					source = open("Files/net/"+site+"index.html","w")
					source.write(str(html))
					source.close()
					print("\33[34m"+"Download concluído"+"\033[0m")
					serverclone.func_main_server()
				except PermissionError:
					print("Você não tem permissões suficientes para isso.")
				except:
					print("\33[31m"+"Ocurreu um erro ao baixar o site."+"\033[0m")
				finally:
					menu.opcoes()
		elif (opcao != 'n' and opcao != 'S' and opcao != 's'):
			print("Opção inválida!")
			htmlcopy()
		elif (opcao == 'S' or opcao == 's'):
			try:
				pathsite = open("Files/net/path.txt","w")
				pathsite.write("Files/net/"+site)
				pathsite.close()
				print("Sucesso!")
			except PermissionError:
				print("Você não tem permissões suficientes para isso.")
			except:
				print("Ocorreu um erro.")
				menu.opcoes()
			finally:
				menu.opcoes()
	else:
		try:
			print("Limpando...")
			os.system("rm -Rf Files/net/"+site)
			print("Concluído. ️️️✔️")
		except PermissionError:
			print("Você não tem permissões suficientes para isso.")
		except:
			print("Ocorreu um erro ao limpar ❌")
			menu.opcoes()
		os.mkdir("Files/net/"+site)
		linklocal = open("Files/net/path.txt","w")
		linklocal.write("Files/net/"+site+"/index.html")
		linklocal.close()
		socket.setdefaulttimeout(5)
		print("\33[05m"+"\33[33m"+"Baixando..."+"\033[0m")
		with urllib.request.urlopen("http://"+site) as response:
			try:
				print("Lendo HTML...")
				html = response.read()
				html = html.decode()
				print("Calculando tamanho...")
				sizesite = len(html)
				print("Salvando...")
				tempo = sizesite/100000000
				for i in tqdm(range(int(sizesite/1024))):
					time.sleep(tempo)
				source = open("Files/net/"+site+"/index.html","w")
				source.write(str(html))
				source.close()
				print("\33[34m"+"Download concluído ✔️"+"\033[0m")
				#notify.notification()
			except PermissionError:
				print("Você não tem permissões suficientes para isso.")
			except:
				print("\33[31m"+"Ocurreu um erro ao baixar o site. ❌️"+"\033[0m")
			finally:
				try:
					os.system("sudo chmod 777 *.sh")
					os.system("./start_server.sh")
					menu.opcoes()
				except FileNotFoundError:
					print("O arquivo de início do servidor local não foi encontrado!")
				finally:
					menu.opcoes()
