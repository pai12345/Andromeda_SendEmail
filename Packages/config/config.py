import os


def get_env():
    return {
        # "SENDER_ADDRESS": os.environ['SENDER_ADDRESS'],
        # "SENDER_PASS": os.environ['SENDER_PASS'],
        # "RECEIVER_ADDRESS": os.environ['RECEIVER_ADDRESS'],
        "SMTP_PORT": os.environ['SMTP_PORT']
    }
