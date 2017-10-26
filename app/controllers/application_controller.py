import sys
import logging
from datetime import datetime

import utils.authz as authz
from models.user import User
from models.notification import Notification
from utils.notification_manager import process_notification, delete_notification, read_notification
from bottle import Bottle, get, post, delete, view, static_file, request, hook, HTTPResponse

def build_application():
    """Application controller."""

    app = Bottle()
    
    @app.post('/notification')
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

    @app.get('/notification')
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

    @app.delete('/notification')
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

    @app.hook('before_request')
    def authenticate():
        """Hook to authenticate user"""
        if request.environ['PATH_INFO'] == "/notification":
            user = getUser()
        
            if user is None:
                raise HTTPResponse(body="Forbidden", status=403)
            
            try:
                if authz.login(user):
                    logging.info('Login success: %s', user.username)
                    return
            except IOError:
                raise HTTPResponse(body="Error reading user file", status=400)
            except Exception as e:
                raise HTTPResponse(body="Unexpected error", status=400)
            
            raise HTTPResponse(body="Invalid username or password", status=401)

    # Static Routes
    @app.get('/')
    @view('app/views/root')
    def action_index():
        """Main page"""
        return {}
        
    @app.get("/public/<filepath:re:.*\.js>")
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

    return app
