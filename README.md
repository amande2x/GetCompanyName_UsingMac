# GetCompanyName_UsingMac

Introduction: This program will get the MAC addrees from user as input and return the company assosiated with that MAC address.  

Prerequisites: 

Ubuntu 18.04.2 LTS

Install Docker using below commands:

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo apt-key fingerprint 0EBFCD88

sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"

sudo apt-get update

sudo apt-get install docker-ce

Usage: 

1. Clone the github repo.
2. cd to dockerfile directory.
3. Build docker image using command: sudo docker build -t getname .
4. run docker image using command: sudo docker run --rm -it getname "44:38:39:ff:ef:57"

"44:38:39:ff:ef:57" is the mac address here

5. User can pass any mac address here and as output this docker container will run and get the company name using API provided by https://macaddress.io/ 


