from flask import (
    Flask, render_template, request, jsonify, redirect, url_for, flash)
# from flask_behind_proxy import FlaskBehindProxy

# create Flask App
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='1020')