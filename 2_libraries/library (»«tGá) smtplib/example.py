
class SendMail:
    class Example:
        @staticmethod
        def example_send_email(subject='subj', text='text'):
            host = 'smtp.yandex.ru'
            port = '465'
            login = 'eevee.cycle'
            password = '31284bogdan'
            writer = 'eevee.cycle@yandex.ru'
            recipient = 'eevee.cycle@yandex.ru'

            message = f"""From: {recipient}\nTo: {writer}\nSubject: {subject}\n\n{text}"""

            smtpobj = smtplib.SMTP_SSL(host=host, port=port)
            smtpobj.ehlo()
            smtpobj.login(user=login, password=password)
            smtpobj.sendmail(from_addr=writer, to_addrs=recipient, msg=message)
            smtpobj.quit()