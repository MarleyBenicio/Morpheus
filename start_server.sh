#!/bin/bash
#Autor: Marley Benício
#start_server.sh
#
#
#Script responsável por iniciar o servidor do Morpheus

clear

python3 serverclone.py || clear ; echo "Erro ao iniciar servidor!" ; sudo python3 morpheus.py

exit 0
