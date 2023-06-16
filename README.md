# Sharded Database Project Documentation

This project involves the creation of a sharded database using MaxScale via Docker-Compose containers. The sharding technique allows for splitting large datasets into smaller pieces distributed across multiple databases, enhancing performance and scalability. To demonstrate the easier querying of the newly configured database a custom python script will be used. I will be using a VM running Ubuntu 22.10 for this demonstration. 
(Thank you to Josh Brown, Brian Huang, and Celine for their help with formatting and troubleshooting)

## Prerequisites 
You will need to have Docker installed on your machine, as well as MariaDB.
* Install MySQL Connector 
```
sudo apt install python3-pip  
pip3 install mysql-connector
```
* Install Docker-Compose  
```
sudo apt install docker-compose
```
*Update your Ubuntu VM
```
sudo apt update  
sudo apt upgrade -y
```
*Install MaxScale container – you will need to clone the following repository to ensure proper installation: 
```
git clone https://github.com/zohan/maxscale-docker/ 
```
## Configuration 
* Edit the maxscale.cnf.d/example.cnf file by navigating to the proper directory. Once there modify the configuration to your needs. 
```
sudo nano example.cnf 
```
* Identify the IP address of your MaxScale container.
```
docker inspect maxscale_maxscale_1 
```
* Edit your python script. 
```
sudo nano main.py 
```
* Replace the IP address in the file with the one obtained from the previous step. Remember that if you restart your container your IP address may change, and if so, it will need to be reflected in your python script. 
## Running 
* Start the MaxScale container by navigating to the proper directory. 
```
cd maxscale-docker/maxscale
```
* Then start the container.
```
sudo docker-compose up –d  
```
* Running the previous command with the –d flag will run it in detached mode which allows it to run in the background. For better troubleshooting capabilities you can run it without –d and you will be able to see logs and status updates from the running process.
* Once successfully up verify the status of your servers. 
```
sudo docker-compose exec maxscale maxctrl list servers
```
* You should see output like this:

* Next you should connect to MariaDB to verify proper operation. 
```
mariadb -umaxuser -pmaxpwd -h 127.0.0.1 -P 4000
```
* Output should look similar to this:

* To stop the containers
```
docker-compose down –v
```
## Operation of the main.py script 
* To run the script
```
python3 main.py
```
* I configured my output to appear as tables, you can use any display method you choose. The last 3 queries’ outputs were too large to post cleanly so I just posted the top portions.
## Output for the 4 queries:
### 1.) “The largest zipcode in zipcodes_one” 
### 2.) “All zipcodes where state=KY (Kentucky)” 
### 3.) “All zipcodes between 40000 and 41000” 
### 4.) “The TotalWages column where state=PA”



