#!/bin/bash
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install python3 -y
sudo apt-get install python3-pip -y
sudo apt-get install git -y
sudo apt-get install libasound2-dev -y
sudo apt-get install swig -y
sudo apt-get install libpulse-dev -y
sudo apt-get install espeak -y
sudo apt-get install sox -y
sudo apt-get install pulseaudio -y
sudo pip3 install wikipedia
sudo pip3 install pyttsx3
sudo pip3 install pyowm
sudo python3 -m pip install --upgrade setuptools wheel
wget https://files.pythonhosted.org/packages/cd/4a/adea55f189a81aed88efa0b0e1d25628e5ed22622ab9174bf696dd4f9474/pocketsphinx-0.1.15.tar.gz
tar -xvf pocketsphinx-0.1.15.tar.gz
cd pocketsphinx-0.1.15/
sudo python3 setup.py install
cd ..
rm pocketsphinx-0.1.15.tar.gz
chmod 777 Steve.py
echo "Install Complete run ./Steve.py to start setup"
