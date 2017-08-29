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
        message = post_param('message', '')
        light   = post_param('light', 1)
        sound   = post_param('sound', 1)
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

@get('/notification')
def action_show():
    """View the oldest notification """
    user = getUser()
    
    if login(user):
        notification = read_notification()
        if notification is not None:
            return dict(ok=True, msg="ok", notification=notification.to_json())
        else:
            return dict(ok=True, msg="No notification")
    else:
        logging.info('Login failed')
        msg = "Invalid username or password"
        return dict(ok=False, msg=msg)

@delete('/notification')
def action_delete():
    """Delete the oldest notification"""
    user = getUser()
    
    if login(user):
        deleted = delete_notification()
        if deleted:
            return dict(ok=True, msg="Done")
        else:
            return dict(ok=True, msg="Nothing to delete")
    else:
        logging.info('Login failed')
        msg = "Invalid username or password"
        return dict(ok=False, msg=msg)

# Static Routes
@get("/public/<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root="public")

def getUser():
    username = post_param('username', '')
    if username == '':
        username = get_param('username', '')
        password = get_param('password', '')
    else:
        password = post_param('password', '')
    
    return User(username, password)
    
## Bottle methods ##
def postd():
    return request.forms

def post_param(name, default=''):
    return request.POST.get(name, default).strip()
    
def get_param(name, default=''):
    return request.GET.get(name, default).strip()

###### Web application main ######
def start_server():
    # Start the Bottle webapp
    run(host=myconfig.HOST, port=myconfig.PORT, quiet=False, reloader=False)

