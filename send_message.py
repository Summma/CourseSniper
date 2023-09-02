import email, smtplib, ssl
from constants import EMAIL, PASSWORD, NUMBER

PROVIDERS = {
    "AT&T": {"sms": "txt.att.net", "mms": "mms.att.net", "mms_support": True},
    "Boost Mobile": {
        "sms": "sms.myboostmobile.com",
        "mms": "myboostmobile.com",
        "mms_support": True,
    },
    "C-Spire": {"sms": "cspire1.com", "mms_support": False},
    "Cricket Wireless": {
        "sms": "sms.cricketwireless.net ",
        "mms": "mms.cricketwireless.net",
        "mms_support": True,
    },
    "Consumer Cellular": {"sms": "mailmymobile.net", "mms_support": False},
    "Google Project Fi": {"sms": "msg.fi.google.com", "mms_support": True},
    "Metro PCS": {"sms": "mymetropcs.com", "mms_support": True},
    "Mint Mobile": {"sms": "mailmymobile.net", "mms_support": False},
    "Page Plus": {
        "sms": "vtext.com",
        "mms": "mypixmessages.com",
        "mms_support": True,
    },
    "Republic Wireless": {
        "sms": "text.republicwireless.com",
        "mms_support": False,
    },
    "Sprint": {
        "sms": "messaging.sprintpcs.com",
        "mms": "pm.sprint.com",
        "mms_support": True,
    },
    "Straight Talk": {
        "sms": "vtext.com",
        "mms": "mypixmessages.com",
        "mms_support": True,
    },
    "T-Mobile": {"sms": "tmomail.net", "mms_support": True},
    "Ting": {"sms": "message.ting.com", "mms_support": False},
    "Tracfone": {"sms": "", "mms": "mmst5.tracfone.com", "mms_support": True},
    "U.S. Cellular": {
        "sms": "email.uscc.net",
        "mms": "mms.uscc.net",
        "mms_support": True,
    },
    "Verizon": {"sms": "vtext.com", "mms": "vzwpix.com", "mms_support": True},
    "Virgin Mobile": {
        "sms": "vmobl.com",
        "mms": "vmpix.com",
        "mms_support": True,
    },
    "Xfinity Mobile": {
        "sms": "vtext.com",
        "mms": "mypixmessages.com",
        "mms_support": True,
    },
}

def send_sms_via_email(
    number: str,
    message: str,
    provider: str,
    sender_credentials: tuple,
    subject: str = "sent using etext",
    smtp_server: str = "smtp.gmail.com",
    smtp_port: int = 465,
):
    sender_email, email_password = sender_credentials
    receiver_email = f'{number}@{PROVIDERS.get(provider).get("sms")}'

    email_message = f"Subject:{subject}\nTo:{receiver_email}\n{message}"

    with smtplib.SMTP_SSL(
        smtp_server, smtp_port, context=ssl.create_default_context()
    ) as email:
        email.login(sender_email, email_password)
        email.sendmail(sender_email, receiver_email, email_message)

def main():
    number = NUMBER
    message = "hello world!"
    provider = "Verizon"

    sender_credentials = (EMAIL, PASSWORD)

    send_sms_via_email(number, message, provider, sender_credentials)

if __name__ == '__main__':
    main()
