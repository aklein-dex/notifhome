import sys
from config import myconfig
from app.models.user import User
from app.models.notification import Notification
from datetime import datetime
from app.utils.authz import login
from app.utils.notification_manager import process_notification, delete_notification, read_notification
from app.bottle import run, get, post, delete, view, static_file, request, hook, HTTPResponse
import logging


@post('/notification')
def action_create():
    """Create a notification"""
    
    notification = build_notification();
    
    try:
        process_notification(notification)
    except IOError:
        raise HTTPResponse(body="Error processing notification IO", status=400)
    except:
        raise HTTPResponse(body="Unexpected error", status=400)
        
    return dict(msg="Notification created")

@get('/notification')
def action_show():
    """View the oldest notification """
    try:
        notification = read_notification()
    except IOError:
        raise HTTPResponse(body="Error reading notification IO", status=400)
    except:
        raise HTTPResponse(body="Unexpected error", status=400)
    
    if notification is not None:
        return dict(msg="", notification=notification.to_json())
    else:
        return dict(msg="No notification")

@delete('/notification')
def action_delete():
    """Delete the oldest notification"""
    try:
        deleted = delete_notification()
    except:
        raise HTTPResponse(body="Unexpected error", status=400)
        
    if deleted:
        return dict(msg="Notification deleted")
    else:
        return dict(msg="No notification to delete")

@hook('before_request')
def authenticate():
    """Hook to authenticate user"""
    if request.environ['PATH_INFO'] == "/notification":
        user = getUser()
    
        if user is None:
            raise HTTPResponse(body="Forbidden", status=403)
            
        if login(user):
            logging.info('Login success: %s', user.username)
        else:
            raise HTTPResponse(body="Invalid username or password", status=401)
    
# Static Routes
@get('/')
@view('app/views/root')
def action_index():
    """Main page"""
    return {}
    
@get("/public/<filepath:re:.*\.js>")
def js(filepath):
    """Root to return files in the public folder"""
    return static_file(filepath, root="public")

## Helper methods ##

def getUser():
    """Create user object with params from POST or GET request"""
    username = post_param('username', '')
    if username == '':
        username = get_param('username', '')
        password = get_param('password', '')
    else:
        password = post_param('password', '')
    
    if username == '':
        return None
    else:
        return User(username, password)

def post_param(name, default=''):
    """Helper to easily get POST parameter"""
    return request.POST.get(name, default).strip()
    
def get_param(name, default=''):
    """Helper to easily get GET parameter"""
    return request.GET.get(name, default).strip()

def build_notification():
    """Return an object notification based on the POST parameters"""
    username = post_param('username', '')
    message  = post_param('message', '')
    light    = post_param('light', 1)
    sound    = post_param('sound', 1)
    notification = Notification(username, message, datetime.now(), light, sound)
    
    if not notification.is_valid():
        raise HTTPResponse(body="Notification invalid", status=400)
    
    return notification

###### Web application main ######
def start_server():
    """Start the Bottle webapp"""
    run(host=myconfig.HOST, port=myconfig.PORT, quiet=False, reloader=False)

