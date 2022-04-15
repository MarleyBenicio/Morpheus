import os, time, sys, platform, socket, configparser, pyfiglet, getpass

from scripts import menu
from scripts import regconfigs
from scripts import update

from random import randint
from time import sleep
from alive_progress import alive_bar

#Cores
Preto = "\033[30m"
Vermelho = "\033[31m"
Verde = "\033[32m"
Amarelo = "\033[33m"
Azul = "\033[34m"
Magenta = "\033[35m"
Ciano = "\033[36m"
Branco = "\033[37m"

Cororiginal = "\033[0m"

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

letras = [Preto, Vermelho, Verde, Amarelo, Azul, Magenta, Ciano, Branco]
efeitos = [Negrito, Reverso]


def start():
    from tqdm import tqdm
    
    userStart = getpass.getuser()
    if userStart != "root":
        print("Algumas funções você só conseguirá usar, se executar o Morpheus como sudo.")

    def bannerFiglet():
        try:
            fonts = randint(1,14)

            letraBanner = randint(0, len(letras))
            efeitoSelec = randint(0, len(efeitos))

            regconfigs.registro()
            banner = configparser.ConfigParser()
            banner.read("Configs/Configs.ini")
            textoBanner = banner.get("window","titlewindow")
            fonteBanner = banner.get("banners",str(fonts))
            result = pyfiglet.figlet_format(textoBanner, font = str(fonteBanner))
            print(letras[letraBanner]+efeitos[efeitoSelec]+result+Cororiginal)
        except ValueError:
            os.system("clear")
            bannerFiglet() 
        except:
            bannerFiglet()

    bannerFiglet()

    spins = randint(1,39)

    configs = configparser.ConfigParser()
    configs.read("Configs/Configs.ini")    
    host = configs.get("Rede","serverStatus")
    porta = configs.get("Rede","portStatus")
    autoupdt = configs.get("Outros","autoupdate")
    spin = configs.get("spinners", str(spins))
    try:
        with alive_bar(100, title = "Iniciando...", bar = 'bubbles', spinner = spin) as bar:
            for i in range(100):
                sleep(0.02)
                bar()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as verifica:
            try:
                verifica.connect((host,int(porta)))
                print("\033[32m"+"\n[Ok] Conexão com o servidor"+"\033[37m"+"\33[5m"+" ✔️"+"\33[0m")
            except:
                print("\033[31m"+"\n[Falha] Conexão com o servidor"+"\033[37m"+"\33[5m"+" ⚠️"+"\33[0m")
            finally:
                verifica.close()
                print("[Ok] Registrando IP WAN (Ctrl+C para cancelar)")
                os.system("curl ifconfig.me -s > Files/net/ipwan.txt")
                print("[Ok] Registrando IP LAN... ")
                os.system("hostname -I > Files/net/iplan.txt")
    except ValueError:
        os.system("clear")
        start()
    try:
        config = configparser.ConfigParser()
        config.read("Configs/Configs.ini")
        cordefundo = config.get("log-html","background")
        cordotexto = config.get("log-html","text")
        tamanhodotexto = config.get("log-html","sizetext")
        bordadatabela = config.get("log-html","bordertable")
        portaupdates = config.get("Rede","portupdate")
        serverupdate = config.get("Rede","serverupdate")

        log = open("Files/Logs/"+time.asctime()+".html","w")
        log.write("<html><body><head><title> Registro de abertura </title></head>")
        log.write("<center><div><h1>Horário</h1></div></center>")
        log.write("<body bgcolor="+cordefundo+" text="+cordotexto+" </body>")
        log.write("<table border="+bordadatabela+">")
        log.write("<tr><td><"+tamanhodotexto+"><br>Hora: %s " % time.asctime()+"</h3></br></td></tr>")
        log.write("</table>")
        log.write("<h3><center><a href=regconfigs/registro.html>Exibir configurações do programa</a></center></h3>")
        log.write("<h3><center><a href=regconfigs/sobre.html>Sobre o programa</a></center></h3>")
        log.write("</body></html>")
        log.close()

        log = open("Files/Logs/"+time.asctime()+".log","w")
        log.write("* PLATAFORMA: %s *" % platform.platform()+"\n")
        log.write("* SISTEMA: %s *" % sys.platform.title()+"\n")
        log.write("\nINFO KERNEL: %s" % str(os.uname())+"\n")
        log.write("\nNOME: %s " % os.name)
        log.close()
    except:
        print("Erro no arquivo de configurações!")
    if sys.platform != "linux":
        print("\33[31m"+"Algumas funções podem não funcionar corretamente.".center(80))
        print("Saia da matrix e venha para o linux".center(80))
    else:pass
    if(autoupdt == "true"):
        update.updates()
    elif(autoupdt == "false"):
        menu.opcoes()
    else:
        print("\033[41m"+"\033[33m"+"Parâmetro incorreto na configuração (autoupdate)."+"\033[0m")
start()
