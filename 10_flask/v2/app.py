# Team Untitled (Jonathan Wu, Liesel Wong, Loki, King Hagrid)
#Soft Dev
#K10 - Putting Little Pieces Together/Flask/Devloping our first Flask thing
#2021-10-04

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")     #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)   #Where will this go?
    return "No hablo queso!"

app.run()

# We think this would print "about to print_name_... and then in the next line in terminal
# it will print _main_. The rest of the code is the same as the homework: It'll print
# no hablo queso! on the website you get from running the program.

# Runtime output: As predicted