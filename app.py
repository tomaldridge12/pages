import os
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    images = os.listdir('static/imgs/')
    return render_template('index.html', image_files=images)

if __name__ == "__main__":
    app.run()