import smtplib
from email.message import EmailMessage
class Send_alert:
    def send_alert(self,body_message):
        msg=EmailMessage()
        msg['Subject']="System Health Alert: RAM Usage High!"
        msg['From']="Email"
        msg['To']="Email"
        msg.set_content(body_message)

        with smtplib.SMTP_SSL("smtp.gmail.com",465) as server:
            server.login("Email","Password")
            server.send_message(msg)
            print("Email Sent Successfully")