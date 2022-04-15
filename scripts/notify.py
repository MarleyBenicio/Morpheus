from pygame import mixer

import configparser

def start():
    som = configparser.ConfigParser()
    som.read("Configs/Configs.ini")
    tocar = som.get("Som","play")
    if(tocar == "true"):
        mixer.init()
        caminho = som.get("Som","path")
        arquivo = som.get("Som","starting")
        mixer.music.load(caminho+"/"+arquivo)
        volume = som.get("Som","volume")
        mixer.music.play()
    else:pass

def notification():
    som = configparser.ConfigParser()
    som.read("Configs/Configs.ini")
    tocar = som.get("Som","play")
    if(tocar == "true"):
        mixer.init()
        caminho = som.get("Som","path")
        arquivo = som.get("Som","notifysound")
        mixer.music.load(caminho+"/"+arquivo)
        volume = som.get("Som","volume")
        mixer.music.play()
    else:pass

def falha():
    som = configparser.ConfigParser()
    som.read("Configs/Configs.ini")
    tocar = som.get("Som","play")
    if(tocar == "true"):
        mixer.init()
        caminho = som.get("Som","path")
        arquivo = som.get("Som","fail")
        mixer.music.load(caminho+"/"+arquivo)
        volume = som.get("Som","volume")
        mixer.music.play()
    else:pass

def scanning():
    som = configparser.ConfigParser()
    som.read("Configs/Configs.ini")
    tocar = som.get("Som","play")
    if(tocar == "true"):
        mixer.init()
        caminho = som.get("Som","path")
        arquivo = som.get("Som","scanning")
        mixer.music.load(caminho+"/"+arquivo)
        volume = som.get("Som","volume")
        mixer.music.play()
    else:pass
start()
