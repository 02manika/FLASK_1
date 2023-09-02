'''Q4. Create a “/welcome” route to display the welcome message “Welcome to ABC Corporation” and a “/”
route to show the following details:
Company Name: ABC Corporation
Location: India
Contact Detail: 999-999-9999'''

from flask import Flask
app = Flask(__name__) 

@app.route("/welcome")
def welcome_mssg():
    return "<h1> <center> Welcome to ABC Corporation </center> </h1>"

@app.route("/")
def details():
    return "Company Name: ABC Corporation <br> Location: India <br> Contact Detail: 999-999-9999"

if __name__=="__main__":
    app.run(host="127.0.0.1", debug=True) 