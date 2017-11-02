from CSSA_ROOT.util.email import *


def send_confirmation_email(user):
    email_account = EmailAccount(
        'Account Admin',
        "account.admin@stevenscssa.org",
        'accountAdmin17'
    )
    subject = "[DO NOT REPLY] Email Confirmation"
    try:
        email_content = "Dear " + user.nick_name + ":<br/><br/>"
        email_content += "Please click on the following link to confirm your email address.<br/>"
        email_content += "<a href=\'http://127.0.0.1:8000/account/verify_email?code=" + user.verify_code + "\'>Confirm Email " \
                                                                                                    "Address</a><br/><br/>"
        email_content += "If you CANNOT click on the link, please copy the following address to the Explorer Address " \
                         "Bar. <br/>"
        email_content += "http://127.0.0.1:8000/account/verify_email?code=" + user.verify_code + "<br/><br/>"
        email_content += "This is A System Generated mailbox. DO NOT REPLY.<br/><br/>"
        email_content += "BEST REGARDS,<br/>STEVENS CSSA Website Support Team"
        send_email(email_account, user.email, email_content, subject)
        return True
    except():
        print("Confirmation Email Send Failed.")
        return False
