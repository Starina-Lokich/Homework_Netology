import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Mail_Client:
    '''
    Класс для отправки и приема электронных писем.
    '''
    def __init__(self, login: str, password: str, gmail_smtp: str, gmail_imap: str):
        '''
        Инициализация класса.
        '''
        self.login = login
        self.password = password
        self.gmail_smtp = gmail_smtp
        self.gmail_imap = gmail_imap

    def send_message(self, recipients: list, message: str, subject: str) -> None:
        '''
        Отправка сообщения электронного письма адресатам.

        Args:
            recipients (list): Список получателей.
            message (str): Текст письма.
            subject (str): Тема письма.
        '''
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))
        
        with smtplib.SMTP(self.gmail_smtp, 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(self.login, self.password)
            smtp.sendmail(self.login, recipients, msg.as_string())

    def receive_message(self, header=None):
        """
        Получение электронного письма.

        Args:
            header (str): Заголовок письма для поиска.

        Returns:
            email.message.Message: Полученное письмо.
        """
        with imaplib.IMAP4_SSL(self.gmail_imap) as mail:
            mail.login(self.login, self.password)
            mail.list()
            mail.select("inbox")
            criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
            result, data = mail.uid('search', None, criterion)
            assert data[0], 'There are no letters with current header'
            latest_email_uid = data[0].split()[-1]
            result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
            raw_email = data[0][1]
            email_message = email.message_from_string(raw_email)
            return email_message
        

if __name__ == '__main__':
    client = Mail_Client(
        login='login@gmail.com', 
        password='qwerty',
        gmail_smtp='smtp.gmail.com', 
        gmail_imap='imap.gmail.com'
    )
    
    client.send_message(
        recipients=['vasya@email.com', 'petya@email.com'], \
        message='Message', 
        subject='Subject'
    )
    
    client.receive_message()