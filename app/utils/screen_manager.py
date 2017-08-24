from OmegaExpansion import oledExp
from app.models.notification import Notification
from config import myconfig

DATE_FORMAT = myconfig.DATE_FORMAT

# From the oledExp:
#   All functions follow the same pattern with return values:
#   If the function operation is successful, the return value will be 0.
#   If the function operation is not successful, the function will return 1.

# a line is 21 characters long
LINE_LENGTH = 21

is_init = False

def init_screen():
    global is_init
    is_init = not oledExp.driverInit()
    if is_init:
        # show a welcome sign for 2 sec, create thread?
        x = 2
    else:
        print "Problem initializing screen"
    
    return is_init
    
    
def print_screen(notification):
    """Print notification on the screen"""

    if not is_init:
        return False
    
    if not notification.is_valid():
        return False

    
    # TODO: set the cursor at the correct position
    status = oledExp.write(getHeader(notification));
    status = oledExp.write(notification.message);
    
    return True


def getHeader(notification):
    """Format the header. It will look like that:
       admin   Dec 12, 12:00
       ---------------------
    """
    # spaces is the number of space between the username and the date.
    spaces = LINE_LENGTH - len(notification.sent_at_formated(DATE_FORMAT))
    short_username = notification.short_username(spaces - 1)
    spaces = spaces - len(short_username)
    # TODO: if spaces is negative, then should abreviate the name
    return short_username + spaces*" " + notification.sent_at_formated(DATE_FORMAT) + "\n" + LINE_LENGTH*"-"

