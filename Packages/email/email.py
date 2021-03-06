import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from Packages.config.config import get_env
from Packages.helper.helper import oServe_helper


class Email:
    async def sendEmail(self, request):
        try:
            # SMTP Port Check
            smtp_port = get_env()
            get_smtp_schema = oServe_helper.get_schema("SMTP_PORT")
            if get_smtp_schema != "Invalid":
                validate_smtp = oServe_helper.validate(
                    get_smtp_schema, smtp_port)
                if(validate_smtp["status"] == "success"):

                    # Payload Check
                    get_payload_schema = oServe_helper.get_schema("Payload")
                    for payload in request:
                        validate_payload = oServe_helper.validate(
                            get_payload_schema["Payload"], payload)
                        if(validate_payload["status"] == "success"):
                            # The mail addresses and password
                            sender_address = payload["SenderAddress"]
                            sender_pass = payload["SenderPassword"]
                            receiver_address = payload["ReceiverAddress"]

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
                                'smtp.gmail.com', int(smtp_port["SMTP_PORT"]))
                            session.starttls()  # enable security

                            # login with mail_id and password
                            session.login(sender_address, sender_pass)
                            text = message.as_string()
                            session.sendmail(
                                sender_address, receiver_address, text)
                            session.quit()
                            return "Success"
            else:
                return get_smtp_schema
        except BaseException as error:
            return error


oServe_email = Email()
