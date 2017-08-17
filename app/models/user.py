class User:
    """A simple user class"""
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def is_valid(self):
        if self.username and self.password:
            return True
        return False

    def matches(self, username, password):
        if self.username == username and self.password == password:
            return True
        return False
