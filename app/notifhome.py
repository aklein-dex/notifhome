import sys
from config import myconfig
from app.models.user import User
from bottle import route, run, template
import bottle
from beaker.middleware import SessionMiddleware
import logging
from datetime import datetime


logging.basicConfig(format='localhost - - [%(asctime)s] %(message)s', level=logging.DEBUG)
log = logging.getLogger(__name__)
bottle.debug(True)

app = bottle.app()
session_opts = {
    'session.cookie_expires': True,
    'session.encrypt_key': 'please use a random key and keep it secret!',
    'session.httponly': True,
    'session.timeout': 3600 * 24,  # 1 day
    'session.type': 'cookie',
    'session.validate_key': True,
}
app = SessionMiddleware(app, session_opts)


@bottle.get('/login')
@bottle.view('app/views/login')
def login():
    """Serve login form"""
    return {}
	
@bottle.post('/login')
def login():
    """Authenticate users"""
    username = post_get('username')
    password = post_get('password')
    # if authenticated then redirect to "/", otherwise stay here.
    
@bottle.route('/')
@bottle.view('app/views/home')
def index():
    """Only authenticated users can see this"""
    # if not authenticated, then redirect to "/login".
    current_user = User("alex", "pwd", "admin")
    return dict(
        current_user = current_user,
        notifications = []
    )

## Bottle methods ##
def postd():
    return bottle.request.forms

def post_get(name, default=''):
    return bottle.request.POST.get(name, default).strip()

###### Web application main ######
def start_server():
    # Start the Bottle webapp
    bottle.run(app=app, port=myconfig.PORT, quiet=False, reloader=False)

