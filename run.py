# pip3 install Flask for install the framework in gitpod
# import the Flask class (capital F means class name)
from flask import Flask

# the convention requires that the instance will be stored in a variable called app
# the first argument is the name of the application module/ package
# since this is a singe module, it can be used __name__ --> built in variable
# this is required because flask need to know where to look for templates and static files

app = Flask(__name__)

#using the app route decorator (@ -> called decorator / way of wrapping functions)
# browse to the root directory and trigger the index function
@app.route("/")
def index():
    return "hello World!"