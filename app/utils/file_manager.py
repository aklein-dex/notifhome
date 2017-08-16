import os

class FileManager:
    def __init__(self, folder):
        self.folder = folder
        
    def create_notification(self, username, message, timestamp):
        # Read the users file
        if not username:
            return False
        if not message:
            return False
        if not timestamp:
            return False

        filename = timestamp.strftime("%Y%m%d%H%M%S")
		
        # Open a file
        fo = open(self.folder + "/" + filename, "w")
        fo.write(username + ":" + message)

        # Close opend file
        fo.close()
        return True
	
    def delete_notification(self):
        x =2
