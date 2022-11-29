#!/bin/bash

if [ -d "node_modules" ] 
then
    echo "dependecies exit " 
else
   sudo apt install php-cli unzip -y
   curl -sS https://getcomposer.org/installer -o /tmp/composer-setup.php
   HASH=`curl -sS https://composer.github.io/installer.sig`
   sudo php /tmp/composer-setup.php --install-dir=/usr/local/bin --filename=composer
   sudo apt install npm -y 
   sudo npm install
    

fi



echo "front is ready "