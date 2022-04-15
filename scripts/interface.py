from tkinter import *

import sys, configparser

from scripts import interfacecloner

def inicio():

    #Configurações da janela
    configuracoes = configparser.ConfigParser()
    configuracoes.read("Configs/Configs.ini")
    titulo = configuracoes.get('window','titlewindow')
    tamanho = configuracoes.get('window','sizewindow')
    cordefundo = configuracoes.get('window','backgroundwindow')
    redimensionarl = configuracoes.get('window','resizablewidth')
    redimensionara = configuracoes.get('window','resizableheight')

    janela.title(titulo)
    janela.geometry(tamanho)
    janela.configure(background = cordefundo)
    janela.resizable(width=redimensionarl, height=redimensionara)

    #Configurações do labelframe1
    lf_texto = configuracoes.get('labelframe','text')
    lf_width = configuracoes.get('labelframe','width')
    lf_height = configuracoes.get('labelframe','height')
    lf_bg = configuracoes.get('labelframe','background')
    lf_fg = configuracoes.get('labelframe','foreground')
    lf_x = configuracoes.get('labelframe','x')
    lf_y = configuracoes.get('labelframe','y')

    labelframe = LabelFrame(
    text = lf_texto,
    width = lf_width,
    height = lf_height,
    bg = lf_bg,
    fg = lf_fg)
    labelframe.place(x = lf_x, y = lf_y)

    #Configurações do labelframe2
    lf2_texto = configuracoes.get('labelframe2','text')
    lf2_width = configuracoes.get('labelframe2','width')
    lf2_height = configuracoes.get('labelframe2','height')
    lf2_bg = configuracoes.get('labelframe2','background')
    lf2_fg = configuracoes.get('labelframe2','foreground')
    lf2_x = configuracoes.get('labelframe2','x')
    lf2_y = configuracoes.get('labelframe2','y')

    labelframe2 = LabelFrame(
    text = lf2_texto,
    width = lf2_width,
    height = lf2_height,
    bg = lf2_bg,
    fg = lf2_fg)
    labelframe2.place(x = lf2_x, y = lf2_y)

    #Configurações do botão "Clonar site"
    bt_clonarsite_fr = configuracoes.get('buttonclonesite','frame')
    bt_clonarsite_ab = configuracoes.get('buttonclonesite','activebackground')
    bt_clonarsite_tx = configuracoes.get('buttonclonesite','text')
    bt_clonarsite_cmd = configuracoes.get('buttonclonesite','command')
    bt_clonarsite_st = configuracoes.get('buttonclonesite','state')
    bt_clonarsite_bd = configuracoes.get('buttonclonesite','border')
    bt_clonarsite_bg = configuracoes.get('buttonclonesite','background')
    bt_clonarsite_fg = configuracoes.get('buttonclonesite','foreground')
    bt_clonarsite_wd = configuracoes.get('buttonclonesite','width')
    bt_clonarsite_x = configuracoes.get('buttonclonesite','x')
    bt_clonarsite_y = configuracoes.get('buttonclonesite','y')

    clonarsite = Button(
    labelframe,
    width = bt_clonarsite_wd,
    activebackground = bt_clonarsite_ab,
    text = bt_clonarsite_tx,
    command = interfacecloner.cloner,
    state = bt_clonarsite_st,
    bd = bt_clonarsite_bd,
    bg = bt_clonarsite_bg,
    fg = bt_clonarsite_fg)
    clonarsite.place(x = bt_clonarsite_x, y = bt_clonarsite_y)

    #Configurações do botão "Capturar links"
    bt_capturarlinks_fr = configuracoes.get('capturelinks','frame')
    bt_capturarlinks_ab = configuracoes.get('capturelinks','activebackground')
    bt_capturarlinks_tx = configuracoes.get('capturelinks','text')
    bt_capturarlinks_cmd = configuracoes.get('capturelinks','command')
    bt_capturarlinks_st = configuracoes.get('capturelinks','state')
    bt_capturarlinks_bd = configuracoes.get('capturelinks','border')
    bt_capturarlinks_bg = configuracoes.get('capturelinks','background')
    bt_capturarlinks_fg = configuracoes.get('capturelinks','foreground')
    bt_capturarlinks_x = configuracoes.get('capturelinks','x')
    bt_capturarlinks_y = configuracoes.get('capturelinks','y')

    capturarlinks = Button(
    labelframe,
    width = 50,
    activebackground = bt_capturarlinks_ab,
    text = bt_capturarlinks_tx,
    state = bt_capturarlinks_st,
    bd = bt_capturarlinks_bd,
    bg = bt_capturarlinks_bg,
    fg = bt_capturarlinks_fg)
    capturarlinks.place(x = bt_capturarlinks_x, y = bt_capturarlinks_y)

    #Configurações do botão "Escanear portas"
    bt_escanearportas_ab = configuracoes.get('scanports','activebackground')
    bt_escanearportas_tx = configuracoes.get('scanports','text')
    bt_escanearportas_cmd = configuracoes.get('scanports','command')
    bt_escanearportas_st = configuracoes.get('scanports','state')
    bt_escanearportas_bd = configuracoes.get('scanports','border')
    bt_escanearportas_bg = configuracoes.get('scanports','background')
    bt_escanearportas_fg = configuracoes.get('scanports','foreground')
    bt_escanearportas_x = configuracoes.get('scanports','x')
    bt_escanearportas_y = configuracoes.get('scanports','y')

    escanearportas = Button(
    labelframe,
    width = 50,
    activebackground = bt_escanearportas_ab,
    state = bt_escanearportas_st,
    text = bt_escanearportas_tx,
    bd = bt_escanearportas_bd,
    bg = bt_escanearportas_bg,
    fg = bt_escanearportas_fg)
    escanearportas.place(x = bt_escanearportas_x, y = bt_escanearportas_y)

    #Configurações do botão "Varrer rede"
    bt_varrerrede_ab = configuracoes.get('buttonscannetwork','activebackground')
    bt_varrerrede_tx = configuracoes.get('buttonscannetwork','text')
    bt_varrerrede_cmd = configuracoes.get('buttonscannetwork','command')
    bt_varrerrede_st = configuracoes.get('buttonscannetwork','state')
    bt_varrerrede_bd = configuracoes.get('buttonscannetwork','border')
    bt_varrerrede_bg = configuracoes.get('buttonscannetwork','background')
    bt_varrerrede_fg = configuracoes.get('buttonscannetwork','foreground')
    bt_varrerrede_x = configuracoes.get('buttonscannetwork','x')
    bt_varrerrede_y = configuracoes.get('buttonscannetwork','y')

    varrerrede = Button(
    labelframe,
    width = 50,
    activebackground = bt_varrerrede_ab,
    text = bt_varrerrede_tx,
    bd = bt_varrerrede_bd,
    state = bt_varrerrede_st,
    bg = bt_varrerrede_bg,
    fg = bt_varrerrede_fg)
    varrerrede.place(x = bt_varrerrede_x, y = bt_varrerrede_y)

    def saida(self):
        from tkinter import messagebox
        resposta = messagebox.askquestion("Confirmar saída","Tem certeza?")
        if resposta == "yes":
            sys.exit()

    #Configurações do botão "Sair"
    bt_sair_ab = configuracoes.get('buttonexit','activebackground')
    bt_sair_tx = configuracoes.get('buttonexit','text')
    bt_sair_cmd = configuracoes.get('buttonexit','command')
    bt_sair_st = configuracoes.get('buttonexit','state')
    bt_sair_bd = configuracoes.get('buttonexit','border')
    bt_sair_bg = configuracoes.get('buttonexit','background')
    bt_sair_fg = configuracoes.get('buttonexit','foreground')
    bt_sair_x = configuracoes.get('buttonexit','x')
    bt_sair_y = configuracoes.get('buttonexit','y')

    sair = Button(
    labelframe,
    width = 50,
    text = bt_sair_tx,
    state = bt_sair_st,
    command = sys.exit,
    bg = bt_sair_bg,
    fg = bt_sair_fg,
    bd = bt_sair_bd)
    sair.place(x = bt_sair_x, y = bt_sair_y)

    #Configurações do Texto da versão
    txVersao_rlf = configuracoes.get('textoversao','relief')
    txVersao_bg = configuracoes.get('textoversao','background')
    txVersao_fg = configuracoes.get('textoversao','foreground')
    txVersao_x = configuracoes.get('textoversao','x')
    txVersao_y = configuracoes.get('textoversao','y')
    txVersao_wd = configuracoes.get('textoversao','width')

    varVersao = StringVar()
    textoVersao = Message(labelframe2,
    textvariable = varVersao,
    relief = txVersao_rlf,
    bg = txVersao_bg,
    fg = txVersao_fg,
    width = txVersao_wd)
    ver = open("ver.txt","r")
    versao = ver.read()
    ver.close()
    varVersao.set("Versão: %s" % versao)
    textoVersao.place(x = txVersao_x, y = txVersao_y)

    #Configurações do Texto sistema
    txSistema_rlf = configuracoes.get('textsystem','relief')
    txSistema_bg = configuracoes.get('textsystem','background')
    txSistema_fg = configuracoes.get('textsystem','foreground')
    txSistema_x = configuracoes.get('textsystem','x')
    txSistema_y = configuracoes.get('textsystem','y')
    txSistema_wd = configuracoes.get('textsystem','width')

    varSistema = StringVar()
    textoSistema = Message(
    labelframe2,
    textvariable = varSistema,
    relief = txSistema_rlf,
    bg = txSistema_bg,
    fg = txSistema_fg,
    width = txSistema_wd)
    sistema = sys.platform
    varSistema.set("Sistema: %s" % sistema)
    textoSistema.place(x = txSistema_x, y = txSistema_y)

    def sobre():
        from PIL import Image
        from tkinter import messagebox
        import os
        try:
            imagem = Image.open("Files/sobre.png")
            imagem.show()
        except FileNotFoundError:
            messagebox.showerror("Erro","Arquivo não encontrado!")
        except:
            messagebox.showwarning("Ops","Algo deu errado.")

    #Configurações do botão Sobre
    bt_sobre_ab = configuracoes.get('buttonabout','activebackground')
    bt_sobre_tx = configuracoes.get('buttonabout','text')
    bt_sobre_bg = configuracoes.get('buttonabout','background')
    bt_sobre_fg = configuracoes.get('buttonabout','foreground')
    bt_sobre_cmd = configuracoes.get('buttonabout','command')
    bt_sobre_st = configuracoes.get('buttonabout','state')
    bt_sobre_bd = configuracoes.get('buttonabout','border')
    bt_sobre_x = configuracoes.get('buttonabout','x')
    bt_sobre_y = configuracoes.get('buttonabout','y')
    bt_sobre_wd = configuracoes.get('buttonabout','width')

    botaoSobre = Button(
    labelframe,
    text = bt_sobre_tx,
    bg = bt_sobre_bg,
    fg = bt_sobre_fg,
    command = sobre,
    state = bt_sobre_st,
    bd = bt_sobre_bd,
    activebackground = bt_sobre_ab,
    width = bt_sobre_wd)
    botaoSobre.place(x = bt_sobre_x, y = bt_sobre_y)

    janela.bind("<Escape>",saida)

janela = Tk()
inicio()
janela.mainloop()
