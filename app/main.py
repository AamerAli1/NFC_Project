from flask import Flask , render_template
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('landing.html')

@app.route('/amer_alkazemi')
def aamer():
   return render_template('aamer.html')

@app.route('/adnan_khesheh')
def adnan():
   return render_template('adnan.html')

@app.route('/hussain_yamani')
def hussain():
   return render_template('hussain.html')