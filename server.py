from distutils.log import debug
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'hush'

@app.route('/')
def button():
    if "num_of_clicks" not in session:
        session["num_of_clicks"] =1
    return render_template("index.html")

@app.route('/counter', methods=["POST"])
def counter():
    session["num_of_clicks"] +=1
    return redirect("/")

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect("/")

# @app.route('/destroy_session')
# def destroy():
#     if "num_of_clicks" in session:
#         session.clear()
#     if request.method == "POST":
#         return session.clear()
#     return render_template("form.html")


if __name__=="__main__":
    app.run(debug=True)