# Base class
class Notification:
    def send_message(self):
        print("Sending notification")


# Subclass 1
class EmailNotification(Notification):
    def send_message(self):
        print("Message sent via Email")


# Subclass 2
class SMSNotification(Notification):
    def send_message(self):
        print("Message sent via SMS")


# Subclass 3
class AppNotification(Notification):
    def send_message(self):
        print("Message sent via Mobile App")


# Creating objects
n1 = EmailNotification()
n2 = SMSNotification()
n3 = AppNotification()

# Polymorphism demonstration
notifications = [n1, n2, n3]

for n in notifications:
    n.send_message()