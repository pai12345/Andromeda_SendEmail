import asyncio
from Packages.email.email import oServe_email

sendEmail = oServe_email.sendEmail()
asyncio.run(sendEmail)
