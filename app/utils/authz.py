import sys
import bottle
from app.models.user import User
from datetime import datetime

class Authz:
    def __init__(self, users_file, session_key_name):
        self.users_file       = users_file
        self.session_key_name = session_key_name or 'beaker.session'
        
    def login(self, username, password):
        # Read the users file
        with open(self.users_file, 'r')  as file:
            for line in file:
                split = line.split(":")
                if split[0] == username and split[1] == password:
                    self._setup_cookie(username)
                    return True
        return False
    
        
    def _setup_cookie(self, username):
        """Setup cookie for a user that just logged in"""
        session = self._beaker_session
        session['username'] = username
        if self.session_domain is not None:
            session.domain = self.session_domain

        self._save_session()
    
    @property
    def current_user(self):
        """Current autenticated user
        :returns: User() instance, if authenticated
        :raises: AuthException otherwise
        """
        session = self._beaker_session
        username = session.get('username', None)
        if username is None:
            raise AuthException("Unauthenticated user")
        if username is not None and username in self._store.users:
            return User(username, self, session=session)
        raise AuthException("Unknown user: %s" % username)
    
    @property
    def _beaker_session(self):
        """Get session"""
        print('req: {0}'.format(bottle.request))
        print('env: {0}'.format(bottle.request.environ))
        return bottle.request.environ.get(self.session_key_name)

    def _save_session(self):
        self._beaker_session.save()
