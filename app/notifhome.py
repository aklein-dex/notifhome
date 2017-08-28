import sys
from config import myconfig
from app.models.user import User
from app.utils.authz import login
from app.utils.notification_manager import process_notification, delete_notification, read_notification
from app.bottle import run, get, post, delete, view, static_file, request
import logging


@post('/notification')
def action_create():
    """Receive a notification"""
    user = getUser()
    
    if login(user):
        logging.info('Login success: %s', user.username)
        message = post_get('message', '')
        light   = post_get('light', 1)
        sound   = post_get('sound', 1)
        return_code  = process_notification(user, message, light, sound)
        if return_code:
            msg = "Notification created"
        else:
            msg = "Problem while creating notification"
    else:
        logging.info('Login failed')
        msg = "Invalid username or password"
        return_code = False
        
    return dict(ok=return_code, msg=msg)
    
@get('/')
@view('app/views/root')
def action_index():
    """Show simple form to send a notification"""
    return {}

@get('/view')
def action_show():
    """View the oldest notification """
    user = getUser()
    
    if login(user):
        notification = read_notification()
        return dict(ok=True, msg=notification)
    else:
        logging.info('Login failed')
        msg = "Invalid username or password"
        return dict(ok=False, msg=msg)

@delete('/delete')
def action_delete():
    """Delete the oldest notification"""
    user = getUser()
    
    if login(user):
        delete_notification()
        return dict(ok=True, msg="Done")
    else:
        logging.info('Login failed')
        msg = "Invalid username or password"
        return dict(ok=False, msg=msg)

# Static Routes
@get("/public/<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root="public")

def getUser():
    username = post_get('username', '')
    password = post_get('password', '')
    return User(username, password)
    
## Bottle methods ##
def postd():
    return request.forms

def post_get(name, default=''):
    return request.POST.get(name, default).strip()
    
def get_get(name, default=''):
    return request.GET.get(name, default).strip()

###### Web application main ######
def start_server():
    # Start the Bottle webapp
    run(host=myconfig.HOST, port=myconfig.PORT, quiet=False, reloader=False)

