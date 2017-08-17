import sys
from config import myconfig
from app.models.user import User
from app.utils.authz import login
from app.utils.notification_manager import process_notification
from app.bottle import run, get, post, view, static_file, request
import logging

logging.basicConfig(format='localhost - - [%(asctime)s] %(message)s', level=logging.DEBUG)
log = logging.getLogger(__name__)


@post('/notification')
def notification():
    """Receive a notification"""
    username = post_get('username', '')
    password = post_get('password', '')
    user     = User(username, password)
    
    if login(user):
        message = post_get('message', '')
        light   = post_get('light', 1)
        sound   = post_get('sound', 1)
        return_code  = process_notification(user, message, light, sound)
        msg = "Notification created"
    else:
        msg = "Invalid username or password"
        return_code = False
        
    return dict(ok=return_code, msg=msg)
    
@get('/')
@view('app/views/root')
def index():
    """Show simple form to send a notification"""
    return {}

# Static Routes
@get("/public/<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root="public")
    
## Bottle methods ##
def postd():
    return request.forms

def post_get(name, default=''):
    return request.POST.get(name, default).strip()

###### Web application main ######
def start_server():
    # Start the Bottle webapp
    run(port=myconfig.PORT, quiet=False, reloader=False)

