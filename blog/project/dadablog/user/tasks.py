from dadablog.celery import app
from tools.sms import YunTongXin

@app.task
def send_sms_c(phone, code):
    config = {
        'accountSid': '8aaf0708825efdb20182664c8fd001cf',
        'accountToken': 'a96e4bae59324ac1b1f7a229886c7f5f',
        'appId': '8aaf0708825efdb20182664c90fa01d6',
        'templateId': '1'
    }

    yun = YunTongXin(**config)
    res = yun.run(phone, code)
    return res
