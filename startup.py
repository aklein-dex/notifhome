import sys
sys.path.append('lib')
sys.path.append('app')
import logging

import bottle
from utils.notification_manager import init_hardware
from config import myconfig
import controllers.application_controller as controller

if __name__ == "__main__":
    logging.info("Notifhome starting...")
    
    if init_hardware():
        logging.info("Initializing done")
        app = controller.build_application()
        bottle.run(app, host=myconfig.HOST, port=myconfig.PORT, quiet=False, reloader=False)
    else:
        logging.info("Problem during initialization")
    
