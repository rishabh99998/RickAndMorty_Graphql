from flask import Flask, url_for, render_template,request 
from api.RAM import RickAndMorty
from api.Exception import RAM_Exception
from api.characterInfo import characterInfo

app = Flask(__name__)

@app.route('/home')
def index():
    results = RickAndMorty().graphData()
    return render_template('index.html',results=results)

@app.route('/home/<int:characterId>',methods=['GET'])
def Info(characterId):
    results = characterInfo().infoData(characterId)
    return render_template('characterInfo.html',results=results)

@app.errorhandler(RAM_Exception)
def handle_api_error(error):
    return render_template('error.html',message=error)
