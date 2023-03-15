from flask import Flask,render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def citta():
    return render_template("citta.html")

@app.route('/roma', methods=['GET'])
def roma():
    return render_template("roma.html")

@app.route('/milano', methods=['GET'])
def milano():
    return render_template("milano.html")

@app.route('/pisa', methods=['GET'])
def pisa():
    return render_template("pisa.html")

@app.route('/firenze', methods=['GET'])
def firenze():
    return render_template("firenze.html")

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)