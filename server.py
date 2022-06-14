from distutils.log import debug
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'hush'

@app.route('/')
@app.route('/counter', methods=["GET", "POST"])
def button():
    if "num_of_clicks" in session:
        session["num_of_clicks"] +=1
    else:
        session["num_of_clicks"] = 1
    if request.method == "POST":
        return render_template("index.html")
    return render_template("index.html")

@app.route('/destroy_session', methods=["POST"])
def destroy_session():
    session["num_of_visits"] = 0
    return render_template("index.html")

# @app.route('/destroy_session')
# def destroy():
#     if "num_of_clicks" in session:
#         session.clear()
#     if request.method == "POST":
#         return session.clear()
#     return render_template("form.html")


if __name__=="__main__":
    app.run(debug=True)