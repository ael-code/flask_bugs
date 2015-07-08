from flask import Flask, Blueprint, render_template


app = Flask(__name__)
app.config.update(DEBUG=True)


# this route return the rendered template `templates/index.html`

@app.route('/mhome')
def mhome():
    return render_template('index.html')



myblueprint = Blueprint('myblueprint', __name__, template_folder="blue/templates")


# this route should return the rendered template taken from `blue/templates/index.html`
# but it actually render the one of the main app `templates/index.html`

@myblueprint.route('/bhome')
def bhome():
    return render_template('index.html')


# this return the rendered template `blue/templates/index2.html`

@myblueprint.route('/bhome2')
def bhome2():
    return render_template('index2.html')


app.register_blueprint(myblueprint, url_prefix="/blue")


if __name__ == '__main__':
    app.run(host="0.0.0.0", use_reloader=True)
