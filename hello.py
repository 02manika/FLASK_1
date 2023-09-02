# Q1. What is Flask Framework? What are the advantages of Flask Framework?

'''It is a pythonic library , that is used to build API or in other words we can say , it helps in web development in python.
-> The advantages of FLASK framework are :
    1) It is a lightweight framework that offers easy development.
    2) Provide flexibility to the developer to experiment with their modules or architecture.
    3) It is suitable for small projects.
    4) Offers a built-in development server and fast debugger.'''
    
    
#Q2. Create a simple Flask application to display ‘Hello World!!’. Attach the screenshot of the output in Jupyter Notebook.

from flask import Flask
app = Flask(__name__) 

@app.route("/")
def hello_world():
    return "<h1>Hello World!</h1>"

if __name__=="__main__":
    app.run(host="127.0.0.1", debug=True) 
    
    
    
# Q3. What is App routing in Flask? Why do we use app routes?
'''App Routing means mapping the URLs to a specific function that will handle the logic for that URL.
App routing is the technique used to map the specific URL with the associated function intended to perform some task.
The Latest Web frameworks use the routing technique to help users remember application URLs. 
It is helpful to access the desired page directly without navigating from the home page. '''

