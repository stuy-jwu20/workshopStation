#Team Untitled - Jonathan W. , Liesel W. , Loki , King Hagrid
#SoftDev
#K12 -- or The Only Constant is Change/jinja and Flask/We observed the behaviors of flask and jinja together and noted anything if there was.
#2021-10--07

from flask import Flask, render_template #Q0: What happens if you remove render_template from this line?
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "No hablo queso!"

coll = [0,1,1,2,3,5,8]

@app.route("/my_foist_template") #Q1: Can all of your teammates confidently predict the URL to use to load this page?
def test_tmplt():
    return render_template( 'model_tmplt.html', foo="fooooo", collection=coll) #Q2: What is the significance of each argument?

if __name__ == "__main__":
    app.debug = True
    app.run()
