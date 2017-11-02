from CSSA_ROOT.util.email import *


def send_password_reset_email(code):
    email_account = EmailAccount(
        'Account Admin',
        "account.admin@stevenscssa.org",
        'accountAdmin17'
    )
    subject = "[DO NOT REPLY] Password Reset"
    try:
        email_content = "Dear " + code.account.nick_name + ":<br/><br/>"
        email_content += "Please click on the following link to reset your password.<br/>"
        email_content += "<a href=\'http://127.0.0.1:8000/account/reset_password?code=" + code.code + "\'>Confirm Email " \
                                                                                                           "Address</a><br/><br/>"
        email_content += "If you CANNOT click on the link, please copy the following address to the Explorer Address " \
                         "Bar. <br/>"
        email_content += "http://127.0.0.1:8000/account/reset_password?code=" + code.code + "<br/><br/>"
        email_content += "This is A System Generated mailbox. DO NOT REPLY.<br/><br/>"
        email_content += "BEST REGARDS,<br/>STEVENS CSSA Website Support Team"
        send_email(email_account, code.account.email, email_content, subject)
        return True
    except():
        print("Confirmation Email Send Failed.")
        return False
