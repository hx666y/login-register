import os
from django.core.mail import EmailMultiAlternatives

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

if __name__ == '__main__':

    subject, from_email, to = '测试邮件', 'hx666y@163.com', '614045035@qq.com'
    text_content = 'Python和Django技术的分享！'
    html_content = '<p>欢迎访问<a href="http://www.jisuapp.cn" target=blank>www.jisuapp.cn</a>Python、Django和机器学习技术的分享！</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()