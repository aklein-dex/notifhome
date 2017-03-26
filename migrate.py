from cork import Cork
from cork.backends import SQLiteBackend
import os
import sys
import myconfig

# Remove the file if it exists
def remove_database():
    if os.path.isfile(myconfig.DB_NAME):
        os.remove(myconfig.DB_NAME) 
        
# Initialize the db with some values.
# Default login/pwd is admin/admin.
def initialize_database():
    db = SQLiteBackend(myconfig.DB_NAME, initialize=True)
    db.connection.executescript("""
        INSERT INTO users (username, email_addr, desc, role, hash, creation_date) VALUES
        (
            'admin',
            'admin@localhost.local',
            'admin test user',
            'admin',
            'cLzRnzbEwehP6ZzTREh3A4MXJyNo+TV8Hs4//EEbPbiDoo+dmNg22f2RJC282aSwgyWv/O6s3h42qrA6iHx8yfw=',
            '2012-10-28 20:50:26.286723'
        );
        INSERT INTO roles (role, level) VALUES ('admin', 100);
        INSERT INTO roles (role, level) VALUES ('user',   50);
        CREATE TABLE notifications
             (id INTEGER PRIMARY KEY, username TEXT, message TEXT, sent_at TEXT, read_at TEXT, light INTEGER, sound INTEGER);
        CREATE TABLE templates
			 (id INTEGER PRIMARY KEY, message TEXT, light_on INTEGER, sound_on INTEGER);
	    CREATE TABLE version (id INTEGER);
	    INSERT INTO version VALUES (1);
    """)

def print_usage():
	print "\nCall this script with an action:"
	print "  init:    to create the DB. If a DB already exists, then it will delete it first."
	print "  upgrade: to upgrade the FB.\n"
	print "For example: python migrate.py init"
	print "\n"
	
if __name__ == '__main__':
	if len(sys.argv) != 2:
		print_usage()
	
	if sys.argv[1] == "init":
		remove_database()
		initialize_database()
	elif sys.argv[1] == "upgrade":
		# upgrade
		print "todo"
	else:
		print_usage()
	

