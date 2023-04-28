from app import app
from flask import render_template, request


@app.route("/")
def index():

    args =  None
    if request.args:

        args =  request.args #going to give is key:value

        return render_template('public/index.html', args=args)
    else:
        return render_template('public/index.html', args=args)