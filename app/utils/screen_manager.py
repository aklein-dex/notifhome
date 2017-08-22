from OmegaExpansion import oledExp
from app.models.notification import Notification
from config import myconfig

DATE_FORMAT = myconfig.DATE_FORMAT

# From the oledExp:
#   All functions follow the same pattern with return values:
#   If the function operation is successful, the return value will be 0.
#   If the function operation is not successful, the function will return 1.

# a line is 21 characters long

is_init = False

def init_screen():
    is_init = not oledExp.driverInit()
    
    
def print_screen(notification):
    """Print notification on the screen"""
    
    if not is_init:
        return False
    
    if not notification.is_valid():
        return False

    
    status = oledExp.write(getHeader(notification));
    status = oledExp.write(notification.message);
    
    return True


def getHeader(notification):
    """Format the header"""
    return notification.username() + " " + notification.sent_at_formated(DATE_FORMAT) + "\n--------------"

