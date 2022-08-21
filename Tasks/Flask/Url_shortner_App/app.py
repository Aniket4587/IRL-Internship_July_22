import pyshorteners
from flask import Flask, render_template, request

app = Flask(__name__)

####################################
@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/',methods=["GET","POST"])
def index():
    shorter = ""
    if request.method == 'POST':
        url = request.form['name']
        s=pyshorteners.Shortener()
        shorter = s.tinyurl.short(url)
        print(shorter)
    return render_template('url.html',ss=shorter)


####################################################

if __name__ == '__main__':
    app.run(debug=True)
    
