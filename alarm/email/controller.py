import smtplib
from email.mime.text import MIMEText
from email.header import Header
from common import log
from common import conf
LOG = log.getlogger()
conf = conf.getconf()
mail_host=conf.get("alarm", "mail_host") 
mail_user=conf.get("alarm", "mail_user")
mail_pass=conf.get("alarm", "mail_pass")
 
 
sender = conf.get("alarm", "mail_sender")
receivers = conf.get("alarm", "mail_receivers") 

sendfrom = conf.get("alarm", "mail_from")
sendto = conf.get("alarm", "mail_to")
subject = conf.get("alarm", "mail_subject")


def sendemail(msg, receivers=receivers,
              sendfrom=sendfrom, sendto=sendto, subject=subject):
    times = conf.getint("alarm", "mail_fail_times")
    ret=True
    while(times):
        try:
            message = MIMEText(msg, 'plain', 'utf-8')
            message['From'] = Header(sendfrom, 'utf-8')
            message['To'] =  Header(sendto, 'utf-8')
            message['Subject'] = Header(subject, 'utf-8')
       
            smtpObj = smtplib.SMTP()
            port = conf.getint("alarm", "mail_port")
            smtpObj.connect(mail_host, port)
            smtpObj.login(mail_user,mail_pass)
            smtpObj.sendmail(sender, receivers, message.as_string())
            smtpObj.quit()  
            LOG.info("send email success")
            times = 0
        except smtplib.SMTPException as e: 
            LOG.error(e)
            LOG.error("Error: cannot send email")
            times -= 1
            ret = False
    return ret

