from bottle import Bottle, run, get, post, route, request # or route
from bottle import static_file
import os

cwd = os.path.dirname(__file__)
os.chdir(cwd + "/..")
print(os.getcwd())

@route('/hello')
def hello():
    return "Hello World!"

@route('/index.html')
def index():
    return static_file('index.html', root='static')

@route('/styles.css')
def index():
    return static_file('styles.css', root='static')

@route('/')
def default_page():
    return static_file('index.html', root='static')

run(host='localhost', port=8080, debug=True)