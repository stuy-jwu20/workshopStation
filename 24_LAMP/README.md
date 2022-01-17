# how-to :: CREATE A DIGITAL OCEAN DROPLET WITH UBUNTU, FLASK, AND APACHE
---
## Overview
Guide to creating an ubuntu 20.04 virtual machine ("droplet") and installing Apache2 web server on it, as well as being able to serve Flask applications.

### Estimated Time Cost: 30 Minutes

### Prerequisites:

- You should have your droplet created already on DigitalOcean before starting these steps, AND having generated a ssh-key generated already on the school linux machines.
- These instructions assume that you're creating your droplet from the school's CS Lab machines.
- To get into the school's CS labs, just
  ```
    ssh <stuy user>@149.89.160.1XX <XX being a number from 01-30>
  ```

### Instructions to Install  

1.  Step One  
    ```
    ssh root@<your_server_ip>
    adduser <your_username>
    usermod -aG sudo <your_username>
    ufw allow OpenSSH
    ufw enable
    rsync --archive --chown=<your_username>:<your_username> ~/.ssh /home/<your_username>
    ```
2.  Try logging into your user account  

    ```
    ssh <my_username>@<your_server_ip>
    ```

3.  If that's successful, exit both the root and your connection so that you're back into your CS Lab machine terminal.  

SSH back into your user account  

    ```
    ssh <my_username>@<your_server_ip>
    ```

4.  
    ```
    sudo service ssh restart
    sudo apt update
    sudo apt install apache2
    sudo ufw allow 'Apache'
    sudo ufw allow 5000
    ```

5. Testing out if your server can serve a very simple flask app.  
    ```
    sudo apt-get update
    sudo apt-get upgrade
    sudo apt-get install python3-pip
    sudo apt-get install python3-dev
    sudo apt-get install python3-setuptools
    sudo apt-get install python3-venv
    sudo apt-get install build-essential libssl-dev libffi-dev
    ```

    ```
    cd ~
    mkdir <directory_name>
    cd <directory_name>
    python3.8 -m venv env
    source env/bin/activate
    pip install wheel
    pip install flask
    pip install uwsgi
    pip install requests
    nano __init__.py
    ```

6. The code to put into the __init__.py  
    ```python
    from flask import Flask
    app = Flask(__name__)

    @app.route("/")
    def index():
        return "<h1>Hi there!</h1>"

    if __name__ == "__main__":
        app.run(host='0.0.0.0')
    ```    

7. Run it!  
    ```
    python __init__.py
    ```

### Resources
* https://www.digitalocean.com/community/questions/error-permission-denied-publickey-when-i-try-to-ssh
* https://www.digitalocean.com/community/questions/secure-ubuntu-server-for-non-root-user-using-only-ssh-keys?answer=22286
* https://www.digitalocean.com/docs/droplets/how-to/
* https://www.digitalocean.com/community/questions/error-permission-denied-publickey-when-i-try-to-ssh?answer=44730
* https://www.digitalocean.com/docs/droplets/how-to/connect-with-ssh/putty/
* https://www.digitalocean.com/docs/droplets/how-to/add-ssh-keys/create-with-openssh/
* https://www.digitalocean.com/docs/droplets/how-to/connect-with-ssh/openssh/
* https://pythonforundergradengineers.com/flask-app-on-digital-ocean.html
---

Accurate as of (last update): 2022-01-17

#### Contributors:  
Jonathan Wu, pd2  
Thomas Yu, pd2  
Mark Zhu, pd2

_Note: the two spaces after each name are important! ( <--burn after reading)  _
