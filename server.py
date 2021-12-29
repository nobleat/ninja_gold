from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


# @app.route('/process_money')
# def roll():
#     return



if __name__=="__main__":
    app.run(debug=True)