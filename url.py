# Q5. What function is used in Flask for URL Building? Write a Python code to demonstrate the working of the url_for() function.

'''The url_for() function is used to build a URL to the specific function dynamically.'''


from flask import Flask
app = Flask(__name__) 

@app.route("/mssg")
def hello_world():
    return "<h1>Hiiiiiii!</h1>"

if __name__=="__main__":
    app.run(host="127.0.0.1",debug=True) 