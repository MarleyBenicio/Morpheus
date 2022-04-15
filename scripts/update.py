import os, configparser

from scripts import menu

def updates():

	config = configparser.ConfigParser()
	config.read("Configs/Configs.ini")
	portaupdates = config.get("Rede","portupdate")
	serverupdate = config.get("Rede","serverupdate")

	versao = open("ver.txt","r")
	vrs = versao.read()
	versao.close()

	vrsn = open("ver.txt","r")
	vr = float(vrsn.read())
	try:
		if (os.path.exists("Files/downloads/update.ver") == True):
			os.remove("Files/downloads/update.ver")
			os.remove("Files/downloads/files.txt")
		else:pass
		print("Verificando atualizações...")

		try:
			os.system("wget -o Files/echo.txt -P Files/downloads "+serverupdate+":"+portaupdates+"/updates/update.ver")
			os.system("wget -o Files/echo.txt -P Files/downloads "+serverupdate+":"+portaupdates+"/updates/files.txt")
			os.system("wget -o Files/echo.txt -P Files/downloads "+serverupdate+":"+portaupdates+"/updates/description.txt")
		except:
			print("Ops, ocorreu um erro ao baixar")

		filetxt = open("Files/downloads/files.txt","r")
		arquivoUpd = filetxt.read()
		fl_update = open("Files/downloads/update.ver","r")
		file_updt = float(fl_update.read())
		if(file_updt > vr):
			print("\033[31m"+"Removendo arquivo antigo...")
			try:
				os.system("rm scripts/"+arquivoUpd)
			except:
				print("Arquivo não encontrado!")
			print("\033[33m"+"Baixando atualizações...")

			os.system("wget -q -nd -r -P /updates/scripts -A py "+serverupdate)

			print("\033[33m"+"Módulo atualizado.")
			atual = open("ver.txt","w")
			atual.write(str(file_updt))
			atual.close()
		elif(file_updt < vr):
			print("\033[31m"+"Erro de versão! | Você está usando uma versão incorreta.")
		else:
			print("\033[33m"+"Programa atualizado!")
	except:
		print("\033[31m"+"\nNão foi possivel buscar por atualizações!"+"\33[5m"+"⚠️")
		print("\33[0m")
	finally:
		menu.opcoes()
		vrsn.close()
		fl_update.close()
