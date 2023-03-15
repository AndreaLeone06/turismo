from flask import Flask,render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def site():
    return render_template("citta.html")

@app.route('/mappa', methods=['GET'])
def mappa():
    return render_template("mappa.html")

@app.route('/mappa/<width>', methods=['GET'])
def mappaWidth(width):
    return render_template("mappa.html", dimensione=width)

@app.route('/template', methods=['GET'])
def template():
    return render_template("sito2/index.html")

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)