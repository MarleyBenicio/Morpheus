def ler():
    arquivo = open("services.txt","r")
    texto = arquivo.read()
    print(texto[0])
    arquivo.close()
ler()

