#!/bin/bash

if [ -d "env" ] 
then
    echo "Python virtual environment exists." 
else
    sudo apt-get install python3-pip -y
    sudo apt install python3-virtualenv -y
#     sudo pip3 install virtualenv  -y 
    virtualenv env
    

    

fi


source env/bin/activate

pip3 install -r requirements.txt 

if [ -d "logs" ] 
then
    echo "Log folder exists." 
else
    mkdir logs
    touch logs/error.log logs/access.log
fi

sudo chmod -R 777 logs
sudo chmod 777 ./front 
sudo chmod 777 ./front/react.sh

echo "env ended"
