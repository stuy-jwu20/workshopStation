# Crashing Waves: Jonathan Wu (Loki), Roshani Shrestha (Pete)
# SoftDev pd0
# K19: A RESTful Journey Skyward
# 2021-11-24t
# time spent: 1 hour

from flask import Flask, render_template
import json
import ssl
import urllib.request

app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def api():
    '''
        For those who get the ssl error involving certifcates being invalid,
        this is a temporary solution that will bypass it until you resolve it on
        your machine.
    '''
    # ssl._create_default_https_context = ssl._create_unverified_context
    '''
        This opens the key_nasa.txt file with the API key and then reads the
        key inside of it.
    '''
    f = open("key_nasa.txt", "r")
    api_key = f.read()
    '''
        Appends the API key to the url to access said API key for use later on
        in the code.
    '''
    url = "https://api.nasa.gov/planetary/apod?api_key=" + api_key
    '''
        Opens the url, then reads the data requested from that url, decodes
        it into a usable dictionary, and then we process the data given onto
        our website.
    '''
    data = urllib.request.urlopen(url)
    read_data = data.read()
    d_data = read_data.decode('utf-8')
    p_data = json.loads(d_data) # dictionary of all the API information
    # print(p_data['url'])
    # print(p_data['explanation'])
    return render_template("main.html", pic = p_data['url'], comment = p_data['explanation'])

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
