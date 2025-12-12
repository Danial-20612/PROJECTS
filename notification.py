# notification
class Notification:
    def push_notification(self):
        print("notification send: ")
class Email(Notification):
    def notification(self):
        print("Notification send via Email: ")
class SMS(Notification):
    def notification(self):
        print("Notification send via SMS: ")

email = Email()
sms = SMS()
    
response = input("What is the notification: ")
send = input("How would you like to send the notification [Email / sms]: ").capitalize()
if send == "Email":
    email.notification()
elif send == "Sms":
    sms.notification()
    

