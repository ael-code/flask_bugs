from flask import Flask, Blueprint, render_template


app = Flask(__name__)
app.config.update(DEBUG=True)

@app.route('/mhome')
def mhome():
    return render_template('index.html')


myblueprint = Blueprint('myblueprint', __name__, template_folder="blue/templates")

@myblueprint.route('/bhome')
def bhome():
    return render_template('index.html')

@myblueprint.route('/bhome2')
def bhome2():
    return render_template('index2.html')

app.register_blueprint(myblueprint, url_prefix="/blue")


if __name__ == '__main__':
    app.run(host="0.0.0.0", use_reloader=True)
