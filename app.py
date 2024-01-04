from flask import (
    Flask, render_template, request, jsonify, redirect, url_for, flash)
# from flask_behind_proxy import FlaskBehindProxy

# create Flask App
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route("/about", methods=['GET', 'POST'])
def about():
    return render_template('about.html')

@app.route('/projects', methods=['GET', 'POST'])
def projects():
    return render_template('projects.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='1020')