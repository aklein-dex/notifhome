from bottle import route, run, template
import bottle
from beaker.middleware import SessionMiddleware
from cork import Cork
from cork.backends import SQLiteBackend
import logging
import myconfig
import sqlite3
from datetime import datetime


logging.basicConfig(format='localhost - - [%(asctime)s] %(message)s', level=logging.DEBUG)
log = logging.getLogger(__name__)
bottle.debug(True)

db = SQLiteBackend(myconfig.DB_NAME, initialize=False)
corkAuth = Cork(backend=db, email_sender='xxx@gmail.com', smtp_url='smtp://smtp.magnet.ie')

db_connection = sqlite3.connect(myconfig.DB_NAME)

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

## Bottle methods ##
def postd():
    return bottle.request.forms

def post_get(name, default=''):
    return bottle.request.POST.get(name, default).strip()


@bottle.post('/notification')
def add_notification():
	"""Only authenticated users can see this"""
	corkAuth.require(fail_redirect='/login')
    
	user    = corkAuth.current_user.username
	message = post_get('message')
	light   = post_get('light')
	sound   = post_get('sound')
	sent_at = datetime.now().strftime(myconfig.DATE_FORMAT)
	cursor  = db_connection.execute("INSERT INTO notifications(message, username, light, sound, sent_at) VALUES (?, ?, ?, ?, ?)", (message, user, light, sound, sent_at))
	db_connection.commit()
	# Show message on OLED
	# Blink LED
	# Bip
	return dict(ok=True, msg='')

	
@bottle.post('/login')
def login():
    """Authenticate users"""
    username = post_get('username')
    password = post_get('password')
    corkAuth.login(username, password, success_redirect='/', fail_redirect='/login')

@bottle.route('/logout')
def logout():
    corkAuth.logout(success_redirect='/login')

@bottle.post('/admin/register')
def register():
    """Send out registration email"""
    corkAuth.register(post_get('username'), post_get('password'), post_get('email_address'))
    return 'Please check your mailbox.'

@bottle.post('/reset_password')
def send_password_reset_email():
    """Send out password reset email"""
    corkAuth.send_password_reset_email(
        username=post_get('username'),
        email_addr=post_get('email_address')
    )
    return 'Please check your mailbox.'


@bottle.route('/change_password/:reset_code')
@bottle.view('password_change_form')
def change_password(reset_code):
    """Show password change form"""
    return dict(reset_code=reset_code)


@bottle.post('/change_password')
def change_password():
    """Change password"""
    corkAuth.reset_password(post_get('reset_code'), post_get('password'))
    return 'Thanks. <a href="/login">Go to login</a>'
    
    
@bottle.route('/')
@bottle.view('home')
def index():
    """Only authenticated users can see this"""
    corkAuth.require(fail_redirect='/login')
    cursor = db_connection.execute("SELECT * FROM notifications")
    return dict(
        current_user=corkAuth.current_user,
        notifications=cursor
    )


# Admin-only pages

@bottle.route('/admin')
@bottle.view('admin_page')
def admin():
    """Only admin users can see this"""
    corkAuth.require(role='admin', fail_redirect='/sorry_page')
    return dict(
        current_user=corkAuth.current_user,
        users=corkAuth.list_users(),
        roles=corkAuth.list_roles()
    )


@bottle.post('/create_user')
def create_user():
    try:
        corkAuth.create_user(postd().username, postd().role, postd().password)
        return dict(ok=True, msg='')
    except Exception, e:
        return dict(ok=False, msg=e.message)


@bottle.post('/delete_user')
def delete_user():
    try:
        corkAuth.delete_user(post_get('username'))
        return dict(ok=True, msg='')
    except Exception, e:
        print repr(e)
        return dict(ok=False, msg=e.message)


@bottle.post('/create_role')
def create_role():
    try:
        corkAuth.create_role(post_get('role'), post_get('level'))
        return dict(ok=True, msg='')
    except Exception, e:
        return dict(ok=False, msg=e.message)


@bottle.post('/delete_role')
def delete_role():
    try:
        corkAuth.delete_role(post_get('role'))
        return dict(ok=True, msg='')
    except Exception, e:
        return dict(ok=False, msg=e.message)
        
        
###### Static pages ######

@bottle.route('/login')
@bottle.view('login_form')
def login_form():
    """Serve login form"""
    return {}


@bottle.route('/sorry_page')
def sorry_page():
    """Serve sorry page"""
    return '<p>Sorry, you are not authorized to perform this action</p>'
        
        
###### Web application main ######
def main():
    # Start the Bottle webapp
    bottle.debug(True)
    bottle.run(app=app, port=myconfig.PORT, quiet=False, reloader=False)

if __name__ == "__main__":
    main()
