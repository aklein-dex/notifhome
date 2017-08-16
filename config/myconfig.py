# Simple property file

PORT=9090

DATE_FORMAT="%Y-%m-%d %H:%M:%S"

SESSION_KEY="change me"

# File containing the list of users
USERS_FILE="/home/alex/workspace/notifhome/config/users.authz"

# Folder containing unread notifications.
# In this folder, 1 file is 1 notification.
# When a notification is read, then the file is deleted.
NOTIF_FILE="/home/alex/workspace/notifhome/queue"