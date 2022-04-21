from random import Random
from django.core.mail import send_mail

from back.settings import EMAIL_FROM
from myapp.models import EmailVerificationCode


def random_code(randomlength=8):
    code = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        code += chars[random.randint(0, length)]
    return code


def send_code(email):
    email_record = EmailVerificationCode()
    code = random_code(16)
    email_record.code = code
    email_record.email = email
    email_record.save()
    email_title = "PetCharm邮箱激活"
    email_body = "你的验证码为：{0}".format(code)
    send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
    if send_status:
        pass
