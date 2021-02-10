import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from Packages.config.config import get_env
from Packages.helper.helper import oServe_helper


class Email:
    async def sendEmail(self):
        try:
            # Validate all configuration values
            payload = get_env()
            validate = oServe_helper.validate(payload)

            if(validate["status"] == "success"):

                # The mail addresses and password
                sender_address = validate["message"]["SENDER_ADDRESS"]
                sender_pass = validate["message"]["SENDER_PASS"]
                receiver_address = validate["message"]["RECEIVER_ADDRESS"]

                # Setup the MIME & subject line
                message = MIMEMultipart()
                message['From'] = sender_address
                message['To'] = receiver_address
                message['Subject'] = "Andromeda Customer Feedback"

                # The body and the attachments for the mail
                mail_content = """ Thank you, we really appreciate your feedback. Your feedback will help ous provide a better Experience in Andromeda"""
                message.attach(MIMEText(mail_content, 'plain'))

                # Create SMTP session for sending the mail
                # use gmail with port
                session = smtplib.SMTP(
                    'smtp.gmail.com', validate["message"]["SMTP_PORT"])
                session.starttls()  # enable security

                # login with mail_id and password
                session.login(sender_address, sender_pass)
                text = message.as_string()
                session.sendmail(sender_address, receiver_address, text)
                session.quit()
                return "Success"
            else:
                return validate
        except BaseException as error:
            return error


oServe_email = Email()
