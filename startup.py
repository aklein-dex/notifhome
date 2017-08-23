from app import notifhome
from app.utils.notification_manager import init_hardware

if __name__ == "__main__":
    init_hardware()
    notifhome.start_server()
