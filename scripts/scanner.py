def scan():
    from scripts import menu
    from scripts import scanPort

    import socket

    print("\33[34m"+"**************************")
    print("\33[34m"+"*"+"\33[33m"+"[1] - Verificar portas. "+"\33[34m"+"*")
    print("\33[34m"+"*"+"\33[33m"+"[2] - Voltar."+"\33[34m"+"           *")
    print("\33[34m"+"**************************")
    opcao = int(input(": "))

    while ((opcao < 1) or (opcao > 3)):
        scan()
    if(opcao == 1):
        scanPort.scannerP()
    elif(opcao == 2):
        menu.opcoes()
