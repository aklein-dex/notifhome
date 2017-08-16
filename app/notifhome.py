import sys
from config import myconfig
from app.models.user import User
from app.utils.authz import Authz
from bottle import route, run, template
import bottle
import logging
from datetime import datetime

authz = Authz(myconfig.USERS_FILE)

logging.basicConfig(format='localhost - - [%(asctime)s] %(message)s', level=logging.DEBUG)
log = logging.getLogger(__name__)
bottle.debug(True)

app = bottle.app()

@bottle.post('/notification')
def notification():
    """Authenticate users"""
    username = post_get('username', '')
    password = post_get('password', '')
    
    if authz.login(username, password):
        message = post_get('message', '')
        light   = post_get('light', 1)
        sound   = post_get('sound', 1)
        sent_at = datetime.now().strftime(myconfig.DATE_FORMAT)
        flash   = "Notification created"
        print(message, light, sound, sent_at, username, password)
    else:
        print(username, password)
        flash = "Invalid username or password"
        
    return {flash}
    
@bottle.route('/')
@bottle.view('app/views/root')
def index():
    """Show simple form to send a notification"""
    return {}

## Bottle methods ##
def postd():
    return bottle.request.forms

def post_get(name, default=''):
    return bottle.request.POST.get(name, default).strip()

###### Web application main ######
def start_server():
    # Start the Bottle webapp
    bottle.run(app=app, port=myconfig.PORT, quiet=False, reloader=False)

