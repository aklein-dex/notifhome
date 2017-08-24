from app import notifhome
from app.utils.notification_manager import init_hardware
import logging

if __name__ == "__main__":
    logging.info("Notifhome starting...")
    
    if init_hardware():
        logging.info("Initializing done")
        notifhome.start_server()
    else:
        logging.info("Problem during initialization")
    
