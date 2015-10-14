from flask import Flask, render_template, session, redirect
from flask.ext.mobility import Mobility
from flask.ext.mobility.decorators import mobile_template

app = Flask(__name__)
Mobility(app)

app.secret_key = 'CHANGE_ME'

### ROUTING ###
@app.route('/')
@mobile_template('{mobile/}index.html')
def index(template):
    form = NameForm(request.form)
    if request.method == 'POST' and form.validate():
    	session["name"] = form.first_name.data
    return render_template(template, form=form)

#clears the session and then redirects back to index
@app.route('/logout')
def index():
	session["name"] = ""
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)