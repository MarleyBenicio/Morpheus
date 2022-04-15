import configparser

def registro():

    reg = configparser.ConfigParser()
    reg.read("Configs/Configs.ini")
    gravador = open("Files/Logs/regconfigs/registro.html","w")
    gravador.write("<html><body><header><title>Registro de configs</title></header>")
    gravador.write("<table border=1>")

    gravador.write("<tr><td><center><b>Rede</b></center></td></tr>")
    #<p style=”color:blue”>Azul</p>
    gravador.write("<tr><td><br><b><p style=color:blue>Prefixo de IP:</b> "+reg.get("Rede","prefixip")+"</br></td></tr>")
    gravador.write("<tr><td><br><b>Faixa de IP:</b> "+reg.get("Rede","faixaip")+"</br></tr></td>")
    #gravador.write("<tr><td><br><b>Quantidade de pings:</b> "+reg.get("Rede","pings")+"</br></tr></td>")
    gravador.write("<tr><td><br><b>Tempo de espera:</b> "+reg.get("Rede","timeout")+"</br></tr></td>")
    gravador.write("<tr><td><br><b>Servidor de status:</b> "+reg.get("Rede","serverstatus")+"</br></tr></td>")
    gravador.write("<tr><td><br><b>Porta de status:</b> "+reg.get("Rede","portstatus")+"</br></tr></td>")
    gravador.write("<tr><td><br><b>Porta local:</b> "+reg.get("Rede","portaserverlocal")+"</br></tr></td>")

#    gravador.write("<tr><td><center><b><i>Som</i></b></center></tr></td>")

#    gravador.write("<tr><td><br><b>Tocar som:</b> "+reg.get("Som","play")+"</br></tr></td>")
#    gravador.write("<tr><td><br><b>Volume:</b> "+reg.get("Som","volume")+"</br></tr></td>")
#    gravador.write("<tr><td><br><b>Path de sons:</b> "+reg.get("Som","path")+"</br></tr></td>")
#    gravador.write("<tr><td><br><b>Som de início:</b> "+reg.get("Som","starting")+"</br></tr></td>")
#    gravador.write("<tr><td><br><b>Som de notificação:</b> "+reg.get("Som","notifysound")+"</br></tr></td>")
#    gravador.write("<tr><td><br><b>Som de falha:</b> "+reg.get("Som","fail")+"</br></tr></td>")
#    gravador.write("<tr><td><br><b>Som de scan:</b> "+reg.get("Som","scanning")+"</br></tr></td>")

    gravador.write("<tr><td><center><b>Log em HTML</b></center></tr></td>")

    gravador.write("<tr><td><br><b>Cor de fundo:</b> "+reg.get("log-html","background")+"</br></tr></td>")
    gravador.write("<tr><td><br><b>Cor do texto:</b> "+reg.get("log-html","text")+"</br></tr></td>")
    gravador.write("<tr><td><br><b>Tamanho do texto:</b> "+reg.get("log-html","sizetext")+"</br></tr></td>")
    gravador.write("<tr><td><br><b>Tamanho da borda:</b> "+reg.get("log-html","bordertable")+"</br></tr></td>")

    gravador.write("</body></html>")

    gravador.close()

registro()
