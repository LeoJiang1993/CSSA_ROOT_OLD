from django.db import models, DatabaseError
from account.storage import AccountImageStorage
from account.util.verify_code import generate_verify_code


class Account(models.Model):
    ACCOUNT_GROUPS = (
        (-2, r'locked'),
        (-1, r'unchecked'),
        (0, r'normal'),
        (1, r'admin'),
    )
    user_name = models.CharField(max_length=20)
    nick_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    photo = models.ImageField(upload_to="static/accountImage", null=False, storage=AccountImageStorage())
    group = models.IntegerField(choices=ACCOUNT_GROUPS)
    created = models.DateTimeField(auto_now_add=True)
    last_visit = models.DateTimeField(auto_now=True)
    email = models.EmailField()
    verify_code = models.CharField(max_length=128)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    @staticmethod
    def sign_in(user_name, password):
        account = Account.objects.filter(user_name=user_name, password=password)
        if account.count() == 1:
            return account[0]
        else:
            return None

    @staticmethod
    def create_account(user_name, password, nick_name, photo, email, last_name, first_name):
        if (not Account.is_nick_name_exist(nick_name)) & (not Account.is_user_name_exist(user_name)) & (
                not Account.is_email_exist(email)):
            verify_code = generate_verify_code()
            while Account.objects.filter(verify_code=verify_code):
                verify_code = generate_verify_code()
            new_account = Account(user_name=user_name, password=password, nick_name=nick_name, photo=photo,
                                  group=-1, last_name=last_name, first_name=first_name,
                                  email=email, verify_code=verify_code)
            new_account.save()
            return Account.objects.filter(user_name=user_name).first()
        else:
            return None

    @staticmethod
    def verify_account(code):
        user = Account.objects.filter(verify_code=code).first()
        if user is not None:
            # todo 判断一下是不是已经确认过了
            user.group = 0
            user.save()
            return user
        else:
            return None

    @staticmethod
    def is_user_name_exist(user_name):
        return not (Account.objects.filter(user_name=user_name).count() == 0)

    @staticmethod
    def is_nick_name_exist(nickname):
        return not (Account.objects.filter(nick_name=nickname).count() == 0)

    @staticmethod
    def is_email_exist(email):
        return not Account.objects.filter(email=email).count() == 0

    @staticmethod
    def modify_account(id, nick_name, photo, first_name, last_name):
        user = Account.objects.get(id=id)
        user.nick_name = nick_name
        if photo is not None:
            user.photo = photo
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return user

    @staticmethod
    def forget_password(email):
        account = Account.objects.filter(email=email)
        if account.count() == 0:
            return None
        account = account[0]
        while True:
            try:
                code = VerifyCode(code=generate_verify_code(), perpose=2,account_id=account.id)
                code.save()
                return code
            except DatabaseError:
                pass

    @staticmethod
    def check_password(password):
        # todo:检查password合法性
        return True

    @staticmethod
    def request_change_password(code):
        code = VerifyCode.objects.filter(code=code, perpose=2, valid=True)
        print(code.count())
        if code.count() == 0:
            return None
        else:
            account = code[0].account
            code.update(valid=False)
            return account

    @staticmethod
    def change_password(account_id,new_password):
        account = Account.objects.filter(id=account_id)
        account.update(password=new_password)
        return account[0]


class VerifyCode(models.Model):
    PERPOSE = (
        (1, r'Email'),
        (2, r'Password'),
    )
    code = models.CharField(max_length=128, unique=True)
    perpose = models.IntegerField(choices=PERPOSE)
    account = models.ForeignKey(Account)
    valid = models.BooleanField(default=True, blank=True)
