class User:
    """A simple user class"""
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def is_valid(self):
        if self.username and len(self.username) > 0 and self.password and len(self.password) > 0:
            return True
        return False

    def matches(self, username, password):
        if self.username == username and self.password == password:
            return True
        return False
