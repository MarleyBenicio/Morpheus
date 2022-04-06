#!/bin/bash

clear
figlet Morpheus
pathlocal=$(pwd)
sleep 2
echo "Verificando instalação de requisitos..."
requisito=$(apt show dialog)
if [ $requisito="WARNING: Package(s) not found:" ]


sudo apt install dialog -y -q
dialog --infobox 'Instalando requisitos...' 12 40 --beep-after
dialog --infobox 'Instalando requisitos...\nfiglet' 12 40
sudo apt install figlet -y -q
dialog --infobox 'Instalando requisitos...\nfiglet\npython3-pip' 12 40
sudo apt install python3-pip -y -q

dialog --infobox 'Instalando requisitos python\ntkinter' 12 40
sudo apt install python3-tk -y -q
dialog --infobox 'Instalando requisitos python\ntkinter\nrequests' 12 40
sudo pip3 install requests
dialog --infobox 'Instalando requisitos python\ntkinter\nrequests\nglob' 12 40
sudo pip3 install glob
dialog --infobox 'Instalando requisitos python\ntkinter\nrequests\nglob\nbs4' 12 40
sudo pip3 install bs4
dialog --infobox 'Instalando requisitos python\ntkinter\nrequests\nglob\nbs4\nplatform' 12 40
sudo pip3 install platform
dialog --infobox 'Instalando requisitos python\ntkinter\nrequests\nglob\nbs4\nplatform\nrandom' 12 40
sudo pip3 install random
dialog --infobox 'Instalando requisitos python\ntkinter\nrequests\nglob\nbs4\nplatform\nrandom\ntime' 12 40
sudo pip3 install time
dialog --infobox 'Instalando requisitos python\ntkinter\nrequests\nglob\nbs4\nplatform\nrandom\ntime\nconfigparser' 12 40
sudo pip3 install configparser
dialog --infobox 'Instalando requisitos python\ntqdm' 12 40
sudo pip3 install tqdm
dialog --infobox 'Instalando requisitos python\ntqdm\nurllib' 12 40
sudo pip3 install urllib.request
dialog --infobox 'Instalando requisitos python\ntqdm\nurllib\nwsgiref.simple_server' 12 40
sudo pip3 install wsgiref.simple_server
dialog --infobox 'Instalando requisitos python\ntqdm\nurllib\nwsgiref.simple_server\npyramid' 12 40
sudo pip3 install pyramid
dialog --infobox 'Instalando requisitos python\ntqdm\nurllib\nwsgiref.simple_server\npyramid\npyfiglet' 12 40
sudo pip3 install pyfiglet -y
dialog --infobox 'Instalando requisitos python\ntqdm\nurllib\nwsgiref.simple_server\npyramid\npyfiglet\nicmplib' 12 40
sudo pip3 install icmplib  -y
dialog --infobox 'Instalando requisitos python\ntqdm\nurllib\nwsgiref.simple_server\npyramid\npyfiglet\nicmplib\nalive_progress' 12 40
sudo pip3 install alive_progress -y
dialog --infobox 'Instalando requisitos\nRequisitos instalados\nLimpando...' 7 40
sudo apt clean -y
dialog --infobox 'Instalando requisitos\nRequisitos instalados\nLimpando...\nAcessando /bin' 7 40
sleep 1
cd /bin
dialog --infobox 'Instalando requisitos\nRequisitos instalados\nLimpando...\nAcessando /bin\nCriando comando morpheus' 7 40
sleep 1
sudo touch morpheus
dialog --infobox 'Instalando requisitos\nRequisitos instalados\nLimpando...\nAcessando /bin\nCriando comando morpheus\nAlterando permissões' 7 40
sleep 1
sudo chmod 777 morpheus
dialog --infobox 'Instalando requisitos\nRequisitos instalados\nLimpando...\nAcessando /bin\nCriando comando morpheus\nAlterando permissões\nCriando script' 7 40
sleep 1
sudo echo "#!/bin/bash" > /bin/morpheus
sudo echo "clear" >> /bin/morpheus
sudo echo "cd $pathlocal" >> /bin/morpheus
sudo echo "clear" >> /bin/morpheus
sudo echo "python3 morpheus.py" >> /bin/morpheus
sudo echo "#By_Marley_Benicio" >> /bin/morpheus

dialog --infobox 'Criando comando morpheusserver' 7 40
sleep 1
sudo touch morpheusserver
dialog --infobox 'Criando comando morpheusserver\nAlterando permissões' 7 40
sleep 1
sudo chmod 777 morpheusserver
dialog --infobox 'Criando comando morpheusserver\nAlterando permissões\nCriando script' 7 40
sleep 1
sudo echo "#!/bin/bash" > /bin/morpheusserver
sudo echo "clear" >> /bin/morpheusserver
sudo echo "cd $pathlocal"
sudo echo "clear" >> /bin/morpheusserver
sudo echo "python3 serverclone.py" >> /bin/morpheusserver
sudo echo "#By_Marley_Benício" >> /bin/morpheusserver
dialog --infobox 'Criando comando morpheusserver\nAlterando permissões\nCriando script\nSaindo...' 7 40
sleep 2
clear
sudo morpheus

exit 0
