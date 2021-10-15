# The Best Laptop - Alif Abdullah, Kevin Cao, Jonathan Wu
# SoftDev
# K14 -- To be able to integrate forms and render responses on template files
# 2021-10-14

from flask import Flask, render_template, request 
app = Flask(__name__)

@app.route("/")
def login_form():
    return render_template("login.html",tnpg="The Best Laptop: Alif Abdullah, Kevin Cao, Jonathan Wu")

@app.route("/auth")
def response():
    req_method = ""
    if request.method == 'POST':
        req_method = 'post'
    elif request.method == 'GET':
        req_method = 'get'
    return render_template("response.html", tnpg="The Best Laptop: Alif Abdullah, Kevin Cao, Jonathan Wu",username=request.args['username'], greeting="We apologize for the inconvenience, your Exaltedness.",request_method=req_method)
    
if __name__ == "__main__":
    app.debug = True
    app.run()